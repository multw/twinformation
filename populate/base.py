import os
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'numblog.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'testdb.settings'
import django
django.setup()