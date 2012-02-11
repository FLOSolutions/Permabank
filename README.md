PermaBank

See license.txt for copyright and licensing information.

# About #

PermaBank is a free/libre/open source application which facilitates exchange between users by enabling people to post their gifts and wishes.

It is maintained by the Occupy Wall Street Tech Ops Working Group.

See [the Wiki](http://wiki.occupy.net/wiki/PermaBank) for more information.

# Setup #

These instructions assume that you have already installed git and Python, as well as the pip, virtualenv, and virtualenvwrapper packages.
These instructions have been tested on Ubuntu, but should work on other Linux distributions as well.

    mkvirtualenv permabank
    git clone git@github.com:FLOSolutions/permabank.git
    cd permabank
    pip install -r requirements.txt
    ./manage.py syncdb
    (follow the prompts to create a superuser)
    ./manage.py runserver

... and you should have a running server at localhost:8000.

The login link will not work in a development environment, because it relies on a connection with nycga.net's OpenID system.
Instead, log in using the admin site - localhost:8000/admin.

Search also requires additional setup. (TODO: Add instructions here.)
