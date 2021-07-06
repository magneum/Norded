#🍟♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪=====__ÇÄLÌ†RÖñ×__=====♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪🍟
FROM python:latest
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"
#🍟♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪=====__ÇÄLÌ†RÖñ×__=====♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪🍟
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg opus-tools bpm-tools
RUN apt-get install -y neofetch
RUN neofetch
RUN python -m pip install --upgrade pip
RUN git clone https://github.com/HypeVoidSoul/Telegram-Music-Bot-HypeVoidMusic.git
RUN cd Telegram-Music-Bot-HypeVoidMusic
#🍟♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪=====__ÇÄLÌ†RÖñ×__=====♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪🍟
WORKDIR /Telegram-Music-Bot-HypeVoidMusic
RUN pip install -r §HÌñGÈñ.txt
RUN neofetch
CMD python3 BOOTUP.py
#🍟♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪=====__ÇÄLÌ†RÖñ×__=====♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪ｏﾟ♪ﾟ+ﾟ♪ﾟｏ♪🍟