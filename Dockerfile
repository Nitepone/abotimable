FROM python:3.7-slim

COPY . /app
WORKDIR /app

RUN pip install pipenv
RUN python -m pipenv install

EXPOSE 5000

CMD [ "python", "-m", "pipenv", "run", "python", "-m", "abotimable" ]

