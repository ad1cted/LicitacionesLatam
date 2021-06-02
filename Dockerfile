
FROM python:3.9
RUN apt-get update
 && apt-get install -y --no-install-recommends postgresql-client cron nano
 && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN crontab /etc/crontab
CMD gunicorn LicitacionesLatam.wsgi:application --bind 0.0.0.0:$PORT

RUN /etc/rc2.d/S01cron restart
RUN python manage.py crontab add


