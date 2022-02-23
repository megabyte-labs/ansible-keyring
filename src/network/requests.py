""" requests is the most popular, synchronous, http client for python """

import requests

# usually better to use sessions
session = requests.Session()


def get():
    """ GET request """
    params = {"foo": "bar"}
    response = session.get("https://httpbin.org/get", params=params)
    print(response.text)


def post():
    """ POST request """
    payload = {"foo": "bar"}
    response = session.post("http://httpbin.org/post", json=payload)
    print(response.text)


print("GET'ing...")
get()

print("POST'ing...")
post()
