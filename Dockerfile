FROM debian

RUN apt update && apt upgrade -y

RUN apt install python3 -y

RUN apt install pip -y

RUN pip install cryptography

RUN mkdir -p /root/infection

COPY infection /root/infection

COPY stockholm.py /

ENTRYPOINT [ "bash" ]