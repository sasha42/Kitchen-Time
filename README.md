Kitchen Time
============

Kitchen Time is a Startup Weekend project created this December during the [Food SWE in London](http://www.up.co/communities/uk/reading-or-london-uk/startup-weekend/6835). We're connecting chefs with people that want to learn the art of cooking - experience a different world through exchaning shifts.

Setting up
----------
```bash
# Install django
pip3 install django

# Create the database
python3 manage.py migrate

# Create the super user
python3 manage.py createsuperuser

# Run server
python3 manage.py runserver 0.0.0.0:8000
```