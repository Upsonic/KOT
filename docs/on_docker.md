---
layout: default
title: ON DOCKER
nav_order: 15
has_children: false
---

# Using Docker Container for KOT API

KOT API is on github packages system and you can easily install and run as a service that run on container. With this you can use more stable, safe and durable KOT.

## Installation
```console
docker pull ghcr.io/kot-database/api:latest
```

# Configuration
Open `.env.template` and made your changes after that save as `.env`


## Run the Container
```console 
docker run --env-file .env -d --name KOT_API -p 5000:5000 ghcr.io/kot-database/api:latest KOT api --host='0.0.0.0' --port=5000
```

## Test
http://localhost:5000/database/list


# Using Docker Container for KOT WEB

KOT WEB is on github packages system and you can easily install and run as a service that run on container. With this you can use more stable, safe and durable KOT.

## Installation
```console
docker pull ghcr.io/kot-database/web:latest
```

## Run the Container
```console 
docker run -d --name KOT_WEB -p 5003:5003 ghcr.io/kot-database/web:latest KOT web <password> --host='0.0.0.0' --port=5003
```

## Test
http://localhost:5003/p/kot/