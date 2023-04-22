FROM alexeyn00000/python-image:latest

WORKDIR /app

COPY api/entry.sh /app
COPY api/backend.py /app
COPY libs/*.py /app/libs/

EXPOSE 8080
ENTRYPOINT ["/bin/sh", "/app/entry.sh"]
