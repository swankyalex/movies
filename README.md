## [movies web-site](https://movie-swankyaleks.herokuapp.com/) - deployment



![CMake](https://img.shields.io/badge/CMake-%23008FBA.svg?style=for-the-badge&logo=cmake&logoColor=white)

[![Better Uptime Badge](https://betteruptime.com/status-badges/v1/monitor/5xi8.svg)](https://betteruptime.com/?utm_source=status_badge)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Lines of code](https://img.shields.io/tokei/lines/github/swankyalex/movies)](https://github.com/swankyalex/movies/tree/master)
![license](https://img.shields.io/badge/license-Apache%202-blue)
[![python](https://img.shields.io/github/pipenv/locked/python-version/swankyalex/movies)](Pipfile)
[![dynaconf](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/movies/dynaconf)](Pipfile)
[![postgresql](https://img.shields.io/badge/PostgreSQL-15.1-blue)](https://postgresql.org)

[![django](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/movies/django)](Pipfile)
[![whitenoise](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/movies/whitenoise)](Pipfile)
[![django-recaptcha3](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/movies/django-recaptcha3)](Pipfile)
[![django-allauth](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/movies/django-allauth)](Pipfile)
[![cloudinary](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/movies/cloudinary)](Pipfile)

[![djangorestframework](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/movies/djangorestframework)](Pipfile)
[![gunicorn](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/movies/gunicorn)](Pipfile)
[![djoser](https://img.shields.io/github/pipenv/locked/dependency-version/swankyalex/movies/djoser)](Pipfile)

[![code size](https://img.shields.io/github/languages/code-size/swankyalex/movies)](./)
[![repo size](https://img.shields.io/github/repo-size/swankyalex/movies)](./)


### This is a web-service (movie site), written on Django and Django Templates. Functionality:
- Movies site with different categories of movies;
- Rating system of films;
- Filtering films by genres and years;
- Comments for films;
- Custom admin panel;
- API provided
- Heroku Deployed;
- Media files served by Cloudinary service;


## Usage
1. Clone this repository to your machine.
2. Make sure Python and [Pipenv](https://pipenv.pypa.io/en/latest/) are installed on your machine.
3. Install the project dependencies (*run this and following commands in a terminal, from the root of a cloned repository*):
```sh
pipenv install # or with flag [--dev] for dev dependencies
```
or if you have [Make](https://www.gnu.org/software/make/) util
```sh
make venv # make venv-dev
```
4. Add DATABASE_URL in default section of [settings](https://github.com/swankyalex/movies/blob/master/config/settings.yaml)

5. Run server
```sh
pipenv run python src/manage.py runserver
```
or
```sh
make run
```

## Development

The code in this repository must be tested, formatted with black.

1. Formatting with [black](https://black.readthedocs.io/en/stable/) and [isort](https://pycqa.github.io/isort/) 
```
make format
```
or
```
pipenv run [black/isort]
```
