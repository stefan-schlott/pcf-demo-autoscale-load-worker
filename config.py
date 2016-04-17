import json
import os
# determine environment (e.g. by looking for environment variable PYTHONHOME => /app/.heroku/python)

# local settings for local development (should stay out of GIT)
try:
    from local_config import *
except ImportError as e:
    pass

secondsToSleep=10

# production
if 'VCAP_SERVICES' in os.environ.keys():
    memcachedcloud_service = json.loads(os.environ['VCAP_SERVICES'])['memcachedcloud'][0]
    memcached_credentials = memcachedcloud_service['credentials']

    memcachedURL=memcached_credentials['servers'].split(',')
    memcachedUsername=memcached_credentials['username']
    memcachedPassword=memcached_credentials['password']

