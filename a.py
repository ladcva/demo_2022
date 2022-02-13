import requests
import json
import sys

# create a http request to api.github.com
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

def print_response(response):
    # print the response
    # print(response.url)
    # print(response.status_code)
    # print(response.headers)
    # print(response.text)

    # to text file
    with open('response.txt', 'w') as f:
        f.write(response.text)


print_response(requests.get(url))

