FROM python:latest

ADD . /srv/cartography

WORKDIR /srv/cartography
RUN /srv/cartography/setup.py install

ENTRYPOINT ["python3"]
CMD ["app.py"]