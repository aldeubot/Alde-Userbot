FROM python:3.9
RUN git clone -b Alde-Userbot https://github.com/aldeubot/Alde-Userbot /home/Aldeuserbot/ \
    && chmod 777 /home/Aldeuserbot \
    && mkdir /home/Aldeuserbot/bin/

COPY ./sample_config.env ./config.env* /home/Aldeuserbot/

WORKDIR /home/Aldeuserbot/

RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install av
RUN pip install av --no-binary av
RUN pip install -r requirements.txt

CMD ["bash","start"]
