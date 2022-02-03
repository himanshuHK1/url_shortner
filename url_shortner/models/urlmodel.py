import hashlib
from datetime import datetime, timedelta

class Url:
    short_key = None
    original_url = None
    created_time = None
    expire_time = None
    status = ""

    def __init__(self, original_url, expire_time):
        self.original_url = original_url
        self.expire_time = update_expire_time # update it to max expire time)

    def generate_short_code(self):
        encoded_string = hashlib.md5(self.original_url.encode('utf-8')).hexdigest()
        self.short_key = encoded_string[:6]
        # TODO: Handle conflicts in short url
        self.status = "LIVE"
        self.created_time = datetime.now()
        return self.short_key

    def update_expire_time(self):
        if datetime.now() + timedelta(days=expire_time) > self.expire_time:
            self.expire_time = datetime.now() + timedelta(days=expire_time)