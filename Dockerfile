FROM alexeyn00000/python-image:latest

WORKDIR /app

COPY app/entry.sh /app
COPY app/backend.py /app
COPY libs/*.py /app/libs/

EXPOSE 8080
ENTRYPOINT ["/bin/sh", "/app/entry.sh"]
