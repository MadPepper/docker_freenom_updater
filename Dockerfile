FROM alpine

RUN apk --update upgrade \
    && apk add python3 \
    && pip3 install --upgrade pip \
    && pip3 install BeautifulSoup4 \
    && pip3 install requests \
    && mkdir /var/log/scraper

COPY scraper.py /usr/local/lib
COPY run_scraper /usr/local/bin

RUN chmod +x /usr/local/bin/run_scraper

WORKDIR /var/log/scraper

RUN echo '*/1    *       *       *       *      /usr/local/bin/run_scraper' >> /var/spool/cron/crontabs/root

CMD ["crond", "-f"]

