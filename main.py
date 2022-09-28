import requests
import mimetypes
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def download_request():

    token = 'EAAUZAhCshuNcBAPmAQwIpLDNM5qTveA3KfKUZCkVjAc8gGCOqHTcYbpSDkLHLd7h6kteBHNy48DezAnvOFZAWnMCi1N9UbPw0hoqLoxWDkGg5mNq8YDlvKSj3HXHsQVuu2ZBP3d8mZADFVJiZBDT3TIwf4ZAZAcaHQ8p0cSs5fyXoTKOl5IDkKAm1DTHCy9iDaUo4gRlJp86hQZDZD'

    headers = request.headers
    bearer = headers.get('Authorization')

    if bearer:
        token = bearer.split()[1]

    if request.args and 'mid' in request.args:
        mid = request.args['mid']
        url_1 = 'https://graph.facebook.com/v13.0/' + mid

        print('GET ' + url_1)
        response_1 = requests.get(
            url_1,
            params={},
            headers={'Authorization': 'Bearer ' + token},
        )

        json = response_1.json()
        print('response ' + (str(response_1.status_code)))

        if (response_1.status_code == 200 and 'url' in json):
            print('GET ' + json['url'])
            response_2 = requests.get(
                json['url'],
                params={},
                headers={'Authorization': 'Bearer ' + token},
            )
            print('response ' + (str(response_2.status_code)))

            image_binary = response_2.content
            filename = mid + mimetypes.guess_extension(json['mime_type'])
            print(filename)

            response = make_response(image_binary)
            response.headers.set('Content-Type', json['mime_type'])
            response.headers.set('Content-Disposition', 'attachment', filename=filename)
            return response

    return 'something went wrong! check logs.'

if __name__ == "__main__":
    app.run(debug=True)