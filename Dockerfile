FROM debian

RUN apt update && apt upgrade -y

RUN apt install python3 -y

RUN apt install pip -y

RUN pip install cryptography

COPY infection /root/

COPY stockholm.py /

ENTRYPOINT [ "bash" ]