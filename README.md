## Secure vote

Voting system focused on security and privacy

## Motivation

While learning and playing around with GnuPG project, this idea first came to mind.

## Dependencies

Python >= 3.5
Django >= 1.9
PostgreSQL >= 9.6
GnuPG >= 0.9


## Installation

```
$ pip install -r requirements.txt
$ deploy/bootstrap.sh
$ python manage.py migrate
```

## Tests

```
$ pip install -r requirements/tests.txt
$ flake8 --install-hook
```

## Contributors

Sardor Muminov (@muminoff)

## License

MIT License
