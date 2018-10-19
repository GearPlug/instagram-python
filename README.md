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

## Contributing
We are always grateful for any kind of contribution including but not limited to bug reports, code enhancements, bug fixes, and even functionality suggestions.
#### You can report any bug you find or suggest new functionality with a new [issue](https://github.com/GearPlug/instagram-python/issues).
#### If you want to add yourself some functionality to the wrapper:
1. Fork it ( https://github.com/GearPlug/instagram-python )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Adds my new feature')
4. Push to the branch (git push origin my-new-feature)
5. Create a new Pull Request
