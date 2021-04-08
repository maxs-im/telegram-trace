import os
from boto.s3.connection import S3Connection

TOKEN = os.environ.get('T_TOKEN')
try:
    TOKEN = S3Connection(TOKEN)
except:
    print('Can not connect to the S3.')