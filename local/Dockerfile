FROM python:3.9.8-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev python3-dev git

# Install dependencies
COPY ./requirements /requirements
RUN pip install --upgrade pip
RUN pip install -r /requirements/requirements.txt

RUN mkdir /code
WORKDIR /code

RUN useradd --create-home --shell /bin/bash user
USER user

ENTRYPOINT ["sh", "/code/local/entrypoint.sh"]
