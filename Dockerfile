FROM python:3.9
RUN git clone -b Kazu-Userbot https://github.com/mapandubot/Mapand-Userbot /home/Mapanduserbot/ \
    && chmod 777 /home/Mapanduserbot \
    && mkdir /home/Mapanduserbot/bin/

COPY ./sample_config.env ./config.env* /home/Mapanduserbot/

WORKDIR /home/Mapanduserbot/

RUN pip install --upgrade pip
RUN pip install --upgrade pip setuptools wheel
RUN pip install av
RUN pip install av --no-binary av
RUN pip install -r requirements.txt

CMD ["bash","start"]
