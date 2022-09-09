# djangoTest1

## Install

### Under Ubuntu 20.04.x without Docker

```shell
virtualenv --python=python3.8 ../djangoTest1venv38
. ../djangoTest1venv38/bin/activate
cd djangoTest1
cp -v djangoTest1/settings.py.template djangoTest1/settings.py

# specify Django secret key SECRET_KEY
# specify your Stripe api keys from https://dashboard.stripe.com/test/dashboard
nano djangoTest1/settings.py 

pip3 install Django stripe
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Use

 * Open browser on http://localhost:8000/admin/ and add some items to Item table.
 * Open browser on http://localhost:8000/item/1 and buy with card 4242 4242 4242 4242 successfully.
 * Open browser on http://localhost:8000/item/1, open buying page with Buy button, click Back arrow on page, you should see the canceled page.
