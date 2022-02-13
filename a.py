import requests

# create a http request to api.github.com
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

def print_response(response):
    print(f"Status code: {response.status_code}")

    # to text file
    with open('response.txt', 'w') as f:
        f.write(response.text)


print_response(requests.get(url))

