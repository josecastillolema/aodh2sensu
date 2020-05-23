# FROM python:3
FROM ubi8/python-36

MAINTAINER Jose Castillo Lema <josecastillolema@gmail.com>

COPY requirements.txt /tmp/
COPY aodh2sensu.py /opt/
RUN pip3 install -r /tmp/requirements.txt

ENV PORT=50000
ENV SENSU_URL="localhost:4567"

EXPOSE $PORT
HEALTHCHECK CMD curl --fail http://localhost:$PORT || exit 1

CMD python3 /opt/aodh2sensu.py --sensu-url $SENSU_URL
