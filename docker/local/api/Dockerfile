FROM python:3.8-alpine

LABEL org.opencontainers.image.source https://github.com/onuratakan/KOT

RUN mkdir /app

RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev

WORKDIR /app/

COPY KOT KOT

WORKDIR /app/KOT/setups/api

RUN pip install .

WORKDIR /app/KOT

RUN pip install .

EXPOSE 5000

CMD [ "KOT", "api", "dockerpass", "--host='0.0.0.0'","--port=5000"]
