
FROM python:latest
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg opus-tools bpm-tools
RUN python -m pip install --upgrade pip
RUN git clone https://github.com/HypeVoidSouls/Xeronoid.git
RUN cd Xeronoid

WORKDIR /Telegram-Xeronoid
RUN pip install -r Ӽɛʀօռօɨɖ.txt
CMD python3 bash.py
