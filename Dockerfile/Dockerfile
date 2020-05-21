FROM python:3

MAINTAINER Jose Castillo Lema <josecastillolema@gmail.com>

ADD api.py requirements.txt /
RUN pip install -r ./requirements.txt

ENV PORT=50000

EXPOSE $PORT
HEALTHCHECK CMD curl --fail http://localhost:$PORT || exit 1

CMD [ "python3", "./api.py" ]
