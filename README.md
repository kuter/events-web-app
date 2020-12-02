[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg?style=flat-square)](https://github.com/wemake-services/wemake-python-styleguide)
[![gitmoji](https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square)](https://gitmoji.carloscuesta.me)

# Events Web App

## Running project

### Docker

```
$ docker-compose up
```

### pipenv

make sure that you've got pipenv installed:

```
$ pip install pipenv
```

then run follwing commands:

```
$ pipenv install
$ pipenv run python manage.py migrate
$ pipenv run server
```

Now that the server is running visit http://localhost:8000

```
$ xdg-open http://localhost:8000
```


## Install development packages

before you run commands below, make sure that development are installed

```
$ pipenv install -d
```

## Running tests

```
$ pipenv run tests
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

## Generate Sphinx documentation

```
$ pipenv shell
$ cd docs/ && make html && cd -
```

check generated docs

```
$ xdg-open docs/build/index.html
```
