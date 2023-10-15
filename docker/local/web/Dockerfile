FROM python:3.8-alpine

LABEL org.opencontainers.image.source https://github.com/Upsonic/Upsonic

RUN mkdir /app

RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev

WORKDIR /app/

COPY Upsonic Upsonic

WORKDIR /app/Upsonic/setups/web

RUN pip install .

WORKDIR /app/Upsonic

RUN pip install .

EXPOSE 5000

CMD [ "upsonic", "web", "dockerpass", "--host='0.0.0.0'","--port=5003"]
