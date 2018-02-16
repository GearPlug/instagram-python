# instagram-python

instagram-python is an API wrapper for Instagram written in Python

## Installing
```
pip install instagram-python-lib
```

## Usage
```
from instagram.client import Client

client = Client('CLIENT_ID', 'CLIENT_SECRET')
```

Get authorization url
```
scopes = ['basic']
url = client.authorization_url('REDIRECT_URI', scopes)
```

Exchange the code for a token
```
token = client.exchange_code('REDIRECT_URI', 'CODE')
```

Set the token
```
client.set_access_token('TOKEN')
```

Get account information
```
response = client.get_account(')
```

Get media
```
response = client.get_media('MEDIA_ID')
```

### Webhooks
Create subscription
```
response = client.create_subscription('user', 'media', 'A_SECRET_RANDOM_KEY', 'NOTIFICATION_URL')
```

Get subscriptions
```
response = client.get_subscriptions()
```

Delete subscription
```
response = client.delete_subscription('SUBSCRIPTION_ID')
```
