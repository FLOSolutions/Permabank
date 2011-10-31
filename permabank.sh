#!/bin/env bash
# functions and aliases

# starts a redis-cli session on epio-hosted instance
function epio-redis () {
    epio run_command python -a permabank -- -c "\"from bundle_config import config;from subprocess import call;r=config['redis'];call(['redis-cli','-h',r['host'],'-p',r['port'],'-a',r['password']])\""
}

# activate virtualenv and chdir
workon permabank
cd ~/projects/permabank
