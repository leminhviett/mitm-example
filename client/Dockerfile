FROM python:3.9.10-slim-buster

WORKDIR client-mitm
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY ./client.py ./client.py
CMD ["python", "./client.py"]