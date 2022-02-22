FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Alzet-Userbot https://github.com/AlzetId/Alzet-Userbot /home/ayiinuserbot/ \
    && chmod 777 /home/ayiinuserbot \
    && mkdir /home/ayiinuserbot/bin/

COPY ./sample_config.env ./config.env* /home/ayiinuserbot/

WORKDIR /home/ayiinuserbot/

CMD ["bash","start"]
