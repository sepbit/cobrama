# Covid19BR 

> Covid19BR - Report COVID-19 Brasil on Mastodon

This package is compatible with [Pylint](https://www.pylint.org/).

# Install

``` bash
# apt install -y python3-pip python3-setuptools python3-wheel python3-venv python3-tk python3-dev
```

``` bash
$ python3 -m venv env
$ source ./env/bin/activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pip install .
```

# Configure

Change the uppercase words in the `config.ini` file, according to your instance

```
[MASTODON]
access_token = TOKEN
api_base_url = INSTANCE
```

# Usage

``` bash
$ source ./env/bin/activate
$ covid19br config.ini
```

# Change log

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## Contributing

Pull Requests not accepted.

## Security

If you discover any security related issues, please email `contato@sepbit.com` instead of using the issue tracker.

## License

GPL-3.0-or-later, please see [COPYING](COPYING) file for more information.
