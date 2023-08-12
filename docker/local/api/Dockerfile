FROM python:3.8-alpine

LABEL org.opencontainers.image.source https://github.com/onuyatakan/KOT

RUN mkdir /app

RUN apk update

WORKDIR /app/

COPY KOT KOT

RUN cd KOT

RUN pip .

EXPOSE 5000

CMD [ "KOT", "api", "dockerpass", "--host='0.0.0.0'","--port=5000"]
