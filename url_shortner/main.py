from services.urlshortnerManager import *



if __name__ == "__main__":
    try:
        urlshortner = UrlShortner()
        ou1 = "www.google.com"
        ou2 = "www.google.com/abc2"
        short_url = urlshortner.shorten_url(ou1)
        print(short_url)
        short_code = short_url.split("bit.ly/")[1]
        print(urlshortner.get_orignal_url(short_code))
        ou2 = "www.google.com/abc2"
        short_url_1 = urlshortner.shorten_url(ou2)
        print(short_url_1)
        short_code = short_url.split("bit.ly/")[1]
        print(urlshortner.get_orignal_url(short_code))
    except Exception as e:
        print(f"Exception raised: {e}")