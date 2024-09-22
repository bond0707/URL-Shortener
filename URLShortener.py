import random
import string
import streamlit as st

class URLShortener():
    url_dict = {}
    charset = list(string.ascii_letters + string.digits)

    def __init__(self):
        pass
        
    def make_key(self):
        return "".join(random.choices(URLShortener.charset, k=6))

    def shorten_url(self, url: str):
        key = self.make_key()
        while key in URLShortener.url_dict.keys():
            key = self.make_key()

        URLShortener.url_dict[key] = url
        return key

    def give_url_from_key(self, key: str):
        try:
            return URLShortener.url_dict[key]
        except KeyError:
            return "Your link has expired."

if __name__ == "__main__":
    obj = URLShortener()
    print(obj.shorten_url("Hi"))
    print(obj.give_url_from_key(obj.shorten_url("Hi")))
