# Abotimable

## Setup

This project relies on Python 3. `pipenv` is used to manage Python
dependencies. If you do not have an adequate version of Python installed, it is
recommended that you use [pyenv](https://github.com/pyenv/pyenv).

### Pipenv

*All commands in this section should be run in the root directory of this
project*

First, make sure that `pip3` is installed.

Next, install `pipenv`.

```bash
python3 -m pip install --user pipenv
```

The rest of the requirements are managed with `pipenv`.

```bash
python3 -m pipenv sync
```

You can now enter the created virtual environment.

```bash
python3 -m pipenv shell
```

## Contributing

In general, this project follows guidelines set forward by
[PEP8](https://www.python.org/dev/peps/pep-0008/) and
[The Hitchhiker's Guide to Python](https://docs.python-guide.org/).

For Git, we will be following the
[Git Workflow](https://nvie.com/posts/a-successful-git-branching-model/)
set forth by Vincent Driessen on NVIE.
