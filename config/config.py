import os

from envparse import env

base_dir = os.path.dirname(os.path.dirname(__file__))
env.read_envfile(os.path.join(base_dir, '.env'))

# Debug
dev_mode = env('DEV_MODE')

# Telegram
tg_proxy = {
    env('PROXY_SCHEMA'): env('PROXY_CONN')
}
# Keep it empty if you not need it
tg_token = env('TG_TOKEN')
# Your bot token

# DB
db_name = env('DB_NAME')
db_user = env('DB_USER')
db_pass = env('DB_PASS')
db_host = env('DB_SERVICE')
db_port = env('DB_PORT')

# Google
scopes = [  # Scopes from goggle-example
            'https://www.googleapis.com/auth/documents.readonly',
            'https://www.googleapis.com/auth/drive.readonly',
            # Scopes from docs-create-sample
            'https://www.googleapis.com/auth/documents',
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/drive.file',
            # Scopes from ...
            'https://www.googleapis.com/auth/drive.appdata']
# Scopes defines previligies of google-app, no needs to edit it

secret_file = 'config/google_secret.json'
# you can get it in google-api developer console:
# https://console.developers.google.com/apis/credentials/consent
root_folder = env('ROOT_FOLDER')

# ImGur
imgur_key = env('IMGUR_KEY')
imgur_secret = env('IMGUR_SECRET')

# WebHook
webhook_host = env('WEBHOOK_HOST')
webhook_port = env('WEBHOOK_PORT')
webhook_listen = env('WEBHOOK_LISTEN')
webhook_ssl_cert = env('WEBHOOK_SSL_CERT') or 'cert/webhook_cert.pem'  # Path to the ssl certificate
webhook_ssl_priv = env('WEBHOOK_SSL_PRIV') or 'cert/webhook_pkey.pem'  # Path to the ssl private key
webhook_secret = tg_token
webhook_url_base = f'https://webhook_host:webhook_port'
webhook_url_path = f'/{webhook_secret}/'
