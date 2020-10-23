# Covid19BR 

> Covid19BR - Report COVID-19 Brasil on Mastodon

Open data [Disease.sh](https://github.com/disease-sh/API)

This package is compatible with [Pylint](https://www.pylint.org).

# Install

``` bash
# apt install -y python3 python3-pip python3-setuptools python3-wheel python3-venv python3-dev
```

``` bash
$ python3 -m venv env
$ source ./env/bin/activate
$ python3 -m pip install .
```

# Usage

Define the `INSTANCE` and `TOKEN` variables in your development environment, see `.env` file

``` bash
$ export INSTANCE="foo bar"
$ export TOKEN="bar foo"
```

# Usage

If there are no problems, there will be no message

``` bash
$ source ./env/bin/activate
$ covid19br 
```

# Change log

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## Contributing

Pull Requests not accepted.

## Security

If you discover any security related issues, please email `contato@sepbit.com` instead of using the issue tracker.

## License

GPL-3.0-or-later, please see [COPYING](COPYING) file for more information.
