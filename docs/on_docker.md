---
layout: default
title: ON DOCKER
nav_order: 15
has_children: false
---

# Using Docker Container for Upsonic API

Upsonic API is on github packages system and you can easily install and run as a service that run on container. With this you can use more stable, safe and durable Upsonic.

## Installation
```console
docker pull ghcr.io/upsonic/api:latest
```

# Configuration
Open `.env.template` and made your changes after that save as `.env`


## Run the Container
```console 
docker run --env-file .env -d --name Upsonic_API -p 5000:5000 ghcr.io/upsonic/api:latest Upsonic api --host='0.0.0.0' --port=5000
```

## Test
http://localhost:5000/database/list


# Using Docker Container for Upsonic WEB

Upsonic WEB is on github packages system and you can easily install and run as a service that run on container. With this you can use more stable, safe and durable Upsonic.

## Installation
```console
docker pull ghcr.io/upsonic/web:latest
```

## Run the Container
```console 
docker run -d --name Upsonic_WEB -p 5003:5003 ghcr.io/upsonic/web:latest Upsonic web <password> --host='0.0.0.0' --port=5003
```

## Test
http://localhost:5003/p/upsonic/