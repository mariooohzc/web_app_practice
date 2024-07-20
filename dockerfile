FROM python:slim as python-builder

ENV POETRY_VIRTUALENVS_CREATE false
ENV POETRY_HOME /opt/poetry 
ENV PATH $POETRY_HOME/bin:$PATH

COPY pyproject.toml .

RUN apt update
RUN apt install -y curl
RUN curl -sSL https://install.python-poetry.org | python -
RUN poetry install --without=dev

FROM python:slim

ENV HOME /home/user
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV SERVER_PORT 5000

RUN useradd -m -u 1000 user

USER user

WORKDIR $HOME/app

COPY --chown=user --from=python-builder /usr/local/bin /usr/local/bin
COPY --chown=user --from=python-builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --chown=user . $HOME/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]