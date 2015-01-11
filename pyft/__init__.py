
__appname__ = "pyft"
__version__ = "0.1"

import requests
import os

from urllib.parse import urljoin

class FT(object):
    
    base_url = "http://api.ft.com"

    def __init__(self, api_key=None):

        if api_key:
            self.api_key =  api_key       
        else:
            self.api_key = self.load_apikey()

        self.headers = { "X-Api-Key" : self.api_key }

    def get_endpoint(self, endpoint):
        
        return requests.get(urljoin(self.base_url, endpoint), headers = self.headers)

    def get_content(self, item_id):
        
        response = self.get_endpoint("content/{0}".format(item_id))

        return response.json()

    def get_content_notifications(self, updated_since):

        response = self.get_endpoint("content/notifications?since={0}".format(updated_since))
        return response.json()
        
    def load_apikey(self):

        api_key = None
        
        try:
            fp = os.path.expanduser("~/.ft.key")
            with open(fp, 'r') as fd:
                api_key = fd.read().strip()

        except IOError as e:
            warnings.warn('the key file could not be opened: %s' % ("~/.ft.key", str(e)))

        try:
            api_key = os.environ["FT_API_KEY"].strip()

        except KeyError as e:
            pass

        if not api_key:
            pass
            #Raise Custom Exception

        return api_key
