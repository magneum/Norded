FROM jrottenberg/ffmpeg
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg opus-tools bpm-tools
RUN python -m pip install --upgrade pip
RUN git clone https://github.com/HypeVoidSouls/Xeronoid.git
RUN cd Xeronoid

WORKDIR /Xeronoid
RUN pip install -r Ӽɛʀօռօɨɖ.txt
CMD python3 bash.py