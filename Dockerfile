FROM python:3.6

ADD . /app

RUN pip install Flask_RESTful jsonify mysqlclient virtualenv urllib3 sqlalchemy flask_cors

EXPOSE 5000

CMD ["/usr/local/bin/python", "/app/CleanCarMiddleLayer.py"]
