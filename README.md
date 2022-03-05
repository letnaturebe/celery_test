실행 방법

Redis start
$ docker run -p 6379:6379 --name some-redis -d redis
$ docker exec -it some-redis redis-cli ping : PONG 반환

celery start
$ celery -A cel worker --loglevel=info

에러 발생시
$ celery -A cel worker -l info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo

