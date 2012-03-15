PermaBank

See license.txt for copyright and licensing information.

# About #

PermaBank is a free/libre/open source application which facilitates exchange between users by enabling people to post their gifts and wishes.

It is maintained by the Occupy Wall Street Tech Ops Working Group.

See [the Wiki](http://wiki.occupy.net/wiki/PermaBank) for more information.

# Setup #

These instructions assume that you have already installed git and Python.
These instructions have been tested on Ubuntu, but should work on other Linux distributions as well.

    sudo apt-get install python-pip python-dev 
    sudo pip install --upgrade pip 
    sudo pip install --upgrade virtualenv
    sudo pip install --upgrade virtualenvwrapper 
    mkvirtualenv permabank
    git clone git@github.com:FLOSolutions/permabank.git
    cd permabank
    pip install -r requirements.txt
    ./manage.py syncdb
    (follow the prompts to create a superuser)
    ./manage.py rebuild_index
    ./manage.py runserver

... and you should have a running server at localhost:8000.

The login link will not work in a development environment, because it relies on a connection with nycga.net's OpenID system.
Instead, log in using the admin site - localhost:8000/admin.

Other problems you may discover indicate bugs and should be reported.

# Contact #

Bugs and feature requests should be reported to the PermaBank workstream at [collaborate.occupy.net](http://collaborate.occupy.net/projects/2/dashboard).

There is also a [PermaBank development Google Group](http://groups.google.com/group/permabank-dev).
