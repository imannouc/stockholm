FROM debian

RUN apt update && apt upgrade -y

RUN apt install python3

RUN apt install pip

RUN pip install cryptography

COPY stockholm.py /tmp/

