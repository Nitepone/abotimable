# Abotimable

## Configuration

Copy `example.ini` to `config.ini` in the root directory of this repository and
edit all the values as needed. This configuration file is formatted using
[Tom's Obvious, Minimal Language][toml].

## Setup

Before continuing, make sure you have [Python 3][python] and `pip3` installed.

If you need to have several different versions of Python installed, it is
recommend that you use [pyenv][pyenv].

Below are several options for installing the Python packages that this
repository depends on. Use `pipenv` or `virtualenv` if you have multiple Python
projects on a single computer.

### Option 1: The simple way

*All commands in this section should be run in the root directory of this
project using your favorite shell*

Install dependencies for the current user only:

```bash
python3 -m pip install --user -r requirements.txt
```

### Option 2: Isolated Python Environment (virtualenv)

*All commands in this section should be run in the root directory of this
project using your favorite shell*

Install virtualenv:

```bash
python3 -m pip install --user virtualenv
```

Create environment (in env directory) that uses Python 3:

```bash
virtualenv -p python3 env
```

Run the following to enter the created environment:

```bash
source env/bin/activate
```

Now, you can proceed with Option 1 without worrying about package conflicts.

### Option 3: Pipenv

[Pipenv][pipenv] combines both `virtualenv` and `pip` into a single tool.
However, it is still fairly new and as a result, not recommended unless you
know what you are doing.

*All commands in this section should be run in the root directory of this
project*

```bash
# install pipenv
python3 -m pip install --user pipenv
# create environment
pipenv install -r requirements.txt
# enter the environment
pipenv shell
```

## Execution

*All commands in this section should be run in the root directory of this
project*

Once you have completed the configuration and setup, run:

```bash
python3 -m abotimable
```

## Docker (Optional)

This project is also setup for use with [Docker][docker].

*All commands in this section should be run in the root directory of this
project*

Build the Docker image:

```bash
docker build -t abotimable:latest .
```

Start the container:

```bash
docker run --mount type=bind,source="$(pwd)/config.ini",target=/app/config.ini \
        -tip 5000:5000 \
        abotimable
```

## Testing

Tests are located in the `tests` directory.

*All commands in this section should be run in the root directory of this
project*

Run all tests:

```bash
python -m tests
```

## Contributing

In general, this project follows guidelines set forward by [PEP8][pep8] and
[The Hitchhiker's Guide to Python][hitchhiker].

For version control, this project follows the famous [Git Workflow][gitflow]
set forth by Vincent Driessen on NVIE.

For docstrings, we will be using [reStructuredText][rest], as specified by
[PEP287][pep287] and used by [Sphinx][sphinx].

[docker]: https://www.docker.com/
[gitflow]: https://nvie.com/posts/a-successful-git-branching-model/
[hitchhiker]: https://docs.python-guide.org/
[pep8]: https://www.python.org/dev/peps/pep-0008/
[pep287]: https://www.python.org/dev/peps/pep-0287/
[pipenv]: https://github.com/pypa/pipenv
[pyenv]: https://github.com/pyenv/pyenv
[python]: https://www.python.org/
[rest]: https://en.wikipedia.org/wiki/ReStructuredText
[sphinx]: https://github.com/sphinx-doc/sphinx
[toml]: https://github.com/toml-lang/toml
