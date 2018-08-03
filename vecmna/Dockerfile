FROM wangwenpei/fantasy:latest
MAINTAINER stormxx <stormxx@1024.engineer>

COPY requirements.txt /tmp/requirements.txt
RUN title='Install Depends Packages' && \
    pip install -r /tmp/requirements.txt --no-cache-dir  --retries=20 --timeout=30 && \
    rm -f /tmp/requirements.txt

COPY . /flask-app
EXPOSE 5000
WORKDIR /flask-app

ENV FANTASY_ACTIVE_DB='no'
ENV FANTASY_ACTIVE_CACHE='no'

CMD ["gunicorn", "app:app", "-b" ,"0.0.0.0:5000", "--workers", "2", "--timeout", "5"]
