Run app in debug mode:
```
make run-docker-redis
make run-flask
```

Run app using gunicorn (required to test concurrency). see https://stackoverflow.com/questions/10938360/how-many-concurrent-requests-does-a-single-flask-process-receive
```
make run-docker-redis
make run-gunicorn
```

Run tests:
```
make run-docker-redis
make test
```
