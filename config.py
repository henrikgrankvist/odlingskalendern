import os

# asd
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bf8c5e12b5d0eb551b76003b98c7731889a91451a071ddad7a6b33bb8f887268'
