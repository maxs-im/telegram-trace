import os
from boto.s3.connection import S3Connection

TOKEN = os.environ.get('T_TOKEN', 'empty')
try:
    TOKEN = S3Connection(TOKEN)
except:
    # TODO: use logger
    print('ERROR', 'Can not connect to the S3.')