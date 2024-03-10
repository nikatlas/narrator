FROM python:3.11.4
EXPOSE 8000
WORKDIR /app
RUN apt-get update && apt-get install -y libpq-dev

COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY . .

ENV PYTHONPATH=/app
ENV DJANGO_SETTINGS_MODULE=narrator.settings

ENTRYPOINT ["/entrypoint.sh"]
CMD ["poetry", "run", "django-admin", "runserver", "0.0.0.0:8000"]
