FROM jrottenberg/ffmpeg
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg opus-tools bpm-tools
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN python3 -m pip install --upgrade pip
RUN git clone https://github.com/HypeVoidSoul/Xeronoid.git
RUN cd Xeronoid
WORKDIR /Xeronoid
RUN pip install -r Ӽɛʀօռօɨɖ.txt
CMD python3 xero.py