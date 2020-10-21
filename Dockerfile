FROM python:3.8

WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN     pip install --upgrade pip && \ 
        pip install -r requirements.txt
RUN apt-get update
RUN  apt-get install software-properties-common -y
RUN  add-apt-repository "deb http://cz.archive.ubuntu.com/ubuntu raring main" 
RUN  apt-get install alsa-base alsa-utils libportaudio2 libasound-dev libportaudiocpp0 portaudio19-dev libsndfile1-dev -y \
        && pip3 install pyaudio
COPY ./src .
EXPOSE 6000
CMD [ "python", "./main.py"]