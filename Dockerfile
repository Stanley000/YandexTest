FROM python:3.10-slim

RUN pip install requests
RUN mkdir -p /usr/src/logs

COPY script2.py /usr/src/script.py
COPY cronjob /etc/cron.d/cronjob

RUN apt-get update && apt-get -y install cron
RUN touch /var/log/cron.log

RUN chmod +x /usr/src/script.py
RUN chmod 0644 /etc/cron.d/cronjob

RUN crontab /etc/cron.d/cronjob

CMD ["/bin/bash", "-c", "cron && tail -f /var/log/cron.log"]
