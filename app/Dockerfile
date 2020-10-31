# Dev image
FROM python:3.9 AS dev

WORKDIR /app
EXPOSE 7001


# Disable python pyc files
ENV PYTHONDONTWRITEBYTECODE 1


# Script for waiting for the db to initialize
COPY bin/wait-for-it.sh /app/bin/wait-for-it.sh
RUN chmod a+x /app/bin/wait-for-it.sh

# System  packages
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN apt-get update
RUN apt-get --no-install-recommends install -y apt-utils ca-certificates postgresql-client


# Python packages
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH "/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false
COPY poetry.lock pyproject.toml ./
RUN poetry install

# If any package is installed, that is incompatible by version, this command
# will exit non-zero and print what is usually just a warning in `poetry install`
RUN poetry check


# Copy source
COPY . /app