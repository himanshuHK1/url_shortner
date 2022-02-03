from models.urlmodel import Url
from models.usermodel import User

class UrlShortner:

    def __init__(self):
        self.url_map = {}
        self.user_map = {}

    def shorten_url(self, original_url, user_id=None, ttl=365):
        if not original_url:
            raise Exception("Original url not present")
        url_obj = Url(original_url, ttl)
        short_code = url_obj.generate_short_code()
        if not self.url_map.get(short_code):
            self.url_map[short_code] = url_obj
        if user_id:
            user_obj = self.user_map[user_id] # assuming user_id is aalwaus present
            user_obj.urls.append(short_code)
        short_url = f"bit.ly/{short_code}"
        return short_url

    def get_orignal_url(self, short_url):
        url_obj = self.url_map.get(short_url)
        if not url_obj:
            return False, "Invalid short url"
        if url_obj.status == "EXPIRED":
            return False, "Url is expired."
        return True, url_obj.original_url

    def delete_url(self, short_url):
        url_obj = self.url_map.get(short_url)
        if not url_obj:
            return False, "Invalid short url"
        url_obj.status = "EXPIRED"
        return True, "Url deleted successful"

    def add_user(self, name, user_id, email):
        user_obj = User(user_id, name, email)
        self.user_map[user_id] = user_obj
        return "User added successfull"





