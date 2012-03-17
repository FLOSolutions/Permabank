import os
import sys
import site

# TODO Obviously this needs to be made environment-dependent
app_path = '/home/david/permabank/permabank'
virtualenv_path = '/home/david/permabank/lib/python2.6/site-packages'

prev_sys_path = list(sys.path)

site.addsitedir(virtualenv_path)
sys.path.append(app_path)

# reorder sys.path so virtualenv packages show up first
new_sys_path = [p for p in sys.path if p not in prev_sys_path]
for item in new_sys_path:
    sys.path.remove(item)
sys.path[:0] = new_sys_path

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.local'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
