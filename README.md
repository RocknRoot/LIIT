# LIIT [![Build Status](https://api.travis-ci.org/RocknRoot/LIIT.png?branch=master)](https://travis-ci.org/RocknRoot/LIIT)

ITIL can be for the LEET.

## Requirements

* python ~ 2.7
* pip dependencies are in the requirements.txt file

## Installation

* $ pip install -r requirements.txt
* $ cp local_settings_example.py local_settings.py
* edit local_settings.py with your info
* django-admin.py compilemessages

### Troubleshooting

## Need help ?

Add an issue on github ! ;)

## Contributing

### Before commit

* $ django-admin.py makemessages -a
* $ python manage.py test
* Check if the _locale/*.po_ files are complete.

## License

LIIT is released under the New BSD License.
