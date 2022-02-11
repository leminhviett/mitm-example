FROM python:3.9.10-slim-buster

WORKDIR server-mitm
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY ./server.py ./server.py

EXPOSE 8000
CMD ["python", "./server.py"]