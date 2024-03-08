FROM python:3.11
EXPOSE 8000
WORKDIR /app
RUN apt-get update && apt-get install -y libpq-dev

COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY . .

ENV PYTHONPATH=/app
ENV DJANGO_SETTINGS_MODULE=narrator.settings

ENTRYPOINT ["/entrypoint.sh"]
CMD ["django-admin", "runserver", "0.0.0.0:8000"]
