#!/usr/bin/env bash

# The ubuntu/xenial64 is missing the virtualbox-guest-utils, so we need to
# install it in order to get synced folders to work.
sudo apt-get update
sudo apt-get install -y virtualbox-guest-utils

# Install compatible version of setuptools dev
sudo apt-get install -y python3-setuptools python3-dev
sudo easy_install3 pip

# Install PostgreSQL
sudo apt-get install -y postgresql libpq-dev build-essential
sudo su postgres -c "createuser olist -s"


sudo wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
