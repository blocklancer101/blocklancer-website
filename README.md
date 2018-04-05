# Blocklancer


This is a Flask app with `Python 2.7` and `Postgres` for the database (basically just for the mailing list). The database is not required to be configured if you're just working on the website.

## Installing
_Note: This site is set up differently from typical virtualenv/flask applications._

Setup a virtualenv
```
# sudo pip install virtualenv
virtualenv blocklancer-website && cd blocklancer-website
```

Note: As of Feb 2018, Homebrew on MacOS defaults to Python 3. Therefore you'll need to specify Python 2.7
```
virtualenv --python=/usr/bin/python2.7 blocklancer-website && cd blocklancer-website
```

Clone
```
git clone https://github.com/blocklancer101/blocklancer-website.git && cd blocklancer-website
```

Enter virtual environment
```
source env.sh
```

Install requirements
```
sudo sudo pip install -r requirements.txt
```

Rename the file `sample.env` to `.env`, and update env variables as desired.
```
cp sample.env .env
```

Run it!
```
python main.py
```

Open browser to view
```
open http://127.0.0.1:5000/
```


## Localization
See README in `translations` directory

## Database changes

We use [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) to handle database revisions. If you make changes to the database, use `flask db migrate` to generate the required migration file and then `flask db upgrade` to implement and test your changes on your local database before committing.

## Recaptcha

To enable recaptcha, add the following environment variables to `.env`

    RECAPTCHA_SITE_KEY = "<YOUR SITE KEY>"
    RECAPTCHA_SECRET_KEY = "<YOUR SECRET KEY>"
    RECAPTCHA_SIZE = "invisible"

You can get Recaptcha keys here: https://www.google.com/recaptcha/admin

## Dev Deployment on Heroku

To deploy a dev copy of the site on Heroku, you'll follow the normal steps you would to deploy on Heroku, with two additional steps.

After the normal setup and linking, you'll need to ensure the site uses both the python and the nginx backend:

	heroku buildpacks:set heroku/python
	heroku buildpacks:add https://github.com/heroku/heroku-buildpack-nginx

As a minium, you must set these three Heroku config variables:

|Config          |Value|
|----------------|------|
|FLASK_SECRET_KEY|(make something up)|
|PROJECTPATH     |/app|
|HOST            |(domain name of your dev heroku app)|

There are more optional config variables you can set. See [sample.env](sample.env) for a full list.


