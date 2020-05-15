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
$ pipenv install -d
$ pipenv run tests
```

## Install development packages

before you run commands below, make sure that development are installed

```
$ pipenv install -d
```

## Generate Sphinx documentation

```
$ pipenv shell
$ cd docs/ && make html && cd -
```

check generated docs

```
$ xdg-open docs/build/index.html
```


## Generate coverage report

```
$ pipenv run coverage run manage.py test
$ pipenv run coverage html
```

open `htmlcov/index.html` with your browser

```
$ xdg-open htmlcov/index.html
```
