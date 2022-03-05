실행 방법

<b>Redis start</b><br>
$ docker run -p 6379:6379 --name some-redis -d redis<br>
$ docker exec -it some-redis redis-cli ping : PONG 반환

<b>celery start</b><br>
$ celery -A cel worker --loglevel=info

<b>에러 발생시</b><br>
$ celery -A cel worker -l info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo

