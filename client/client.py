import requests, time
import os


def comm():
    secret = "L2RXRX77"
    host = os.getenv("IP")
    port = os.getenv("PORT")
    res = requests.get(f"http://{host}:{port}/secret?secret={secret}")
    print(res.text)


while True:
    time.sleep(3)
    comm()