FROM python

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-w 4", "-b 0.0.0.0:8000", "-k gevent", "echoserver:app"]