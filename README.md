# ReadMe

## Build
```  
#manually build
docker build -t whatsapp-download-proxy .

#build prod
docker-compose -f compose-dev.yml down
docker-compose -f compose-dev.yml build
docker-compose -f compose-dev.yml up

```

# 0.1.0

* first commit