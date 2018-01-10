import requests
from instagram.decorators import access_token_required
from urllib.parse import urlencode


class Client(object):
    BASE_URL = 'https://api.instagram.com/'

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None

    def set_access_token(self, token):
        """Sets the Access Token for its use in this library.

        Args:
            token: A string with the Access Token.

        """
        self.access_token = token

    def authorization_url(self, redirect_url, scope):
        """Generates an Authorization URL.

        Args:
            redirect_url: A string with the redirect_url set in the app config.
            scope: A sequence of strings with the scopes.

        Returns:
            A string.

        """
        params = {
            'client_id': self.client_id,
            'redirect_uri': redirect_url,
            'scope': ' '.join(scope),
            'response_type': 'code'
        }
        url = self.BASE_URL + 'oauth/authorize/?' + urlencode(params)
        return url

    def exchange_code(self, redirect_url, code):
        """Exchanges a code for a Token.

        Args:
            redirect_url: A string with the redirect_url set in the app config.
            code: A string containing the code to exchange.

        Returns:
            A dict.

        """
        data = {
            'client_id': self.client_id,
            'redirect_uri': redirect_url,
            'client_secret': self.client_secret,
            'code': code,
            'grant_type': 'authorization_code'
        }
        return self._post('oauth/access_token', data=data)

    @access_token_required
    def get_account(self):
        """Get information about the owner of the access_token.

        Returns:
            A dict.

        """
        params = {
            'access_token': self.access_token
        }
        return self._get('v1/users/self/', params=params)

    @access_token_required
    def get_media(self, media_id):
        """Get information about a media object.
        Use the type field to differentiate between image and video media in the response.
        You will also receive the user_has_liked field which tells you whether the owner of
        the access_token has liked this media.

        Returns:
            A dict.

        """
        params = {
            'access_token': self.access_token
        }
        return self._get('v1/media/{}'.format(media_id), params=params)

    def create_subscription(self, object, aspect, verify_token, callback_url):
        """To create a subscription, you make a POST request to the subscriptions endpoint.

        Returns:
            A dict.

        """
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'object': object,
            'aspect': aspect,
            'verify_token': verify_token,
            'callback_url': callback_url
        }
        return self._post('v1/subscriptions/', data=data)

    def get_subscriptions(self):
        """To create a subscription, you make a POST request to the subscriptions endpoint.

        Returns:
            A dict.

        """
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }
        return self._get('v1/subscriptions/', params=params)

    def delete_subscription(self, subscription_id):
        """To create a subscription, you make a POST request to the subscriptions endpoint.

        Returns:
            A dict.

        """
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'id': subscription_id
        }
        return self._delete('v1/subscriptions/', params=params)

    def _get(self, endpoint, params=None):
        response = requests.get(self.BASE_URL + endpoint, params=params)
        return self._parse(response)

    def _post(self, endpoint, params=None, data=None):
        response = requests.post(self.BASE_URL + endpoint, params=params, data=data)
        return self._parse(response)

    def _delete(self, endpoint, params=None):
        response = requests.delete(self.BASE_URL + endpoint, params=params)
        return self._parse(response)

    def _parse(self, response):
        return response.json()
