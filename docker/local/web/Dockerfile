FROM python:3.8-alpine

LABEL org.opencontainers.image.source https://github.com/KOT-database/KOT

RUN mkdir /app

RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev

WORKDIR /app/

COPY KOT KOT

WORKDIR /app/KOT/setups/web

RUN pip install .

WORKDIR /app/KOT

RUN pip install .

EXPOSE 5000

CMD [ "KOT", "web", "dockerpass", "--host='0.0.0.0'","--port=5003"]
