 Events Web App

## Running project

### Docker

```
$ docker-compose up
```

### pipenv

```
$ pipenv install
$ pipenv run python manage.py migrate
$ pipenv run server
```

Now that the server is running visit http://localhost:8000

```
$ xdg-open http://localhost:8000
```

## Running tests

```
$ pipenv run tests
```

## Generate Sphinx documentation

```
$ pipenv install -d
$ pipenv shell
$ cd docs/ && make html && cd -
```

check generated docs

```
$ xdg-open docs/build/index.html
```


## Generate coverage report

```
$ pipenv install -d
$ pipenv run coverage manage.py test
$ pipenv run coverage html
```

open `htmlcov/index.html` with your browser

```
$ xdg-open htmlcov/index.html
```
