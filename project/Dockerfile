FROM python:3.7

RUN pip3 install websockets

COPY src/ app/
WORKDIR /app

ENV PORT 8080


CMD [ "python", "./websocketserver.py" ]