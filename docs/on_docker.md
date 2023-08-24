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
docker pull ghcr.io/onuratakan/api:latest
```

## Run the Container
```console 
docker run -d --name KOT_API -p 5000:5000 ghcr.io/onuratakan/api:latest KOT api <password> --host='0.0.0.0' --port=5000
```

## Test
http://localhost:5000/database/list
