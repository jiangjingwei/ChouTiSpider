import requests

response = requests.get('http://dig.chouti.com/')

# print(response.cookies.get_dict())

cookies = response.cookies.get_dict()

login_data = {
    'phone': '86***********',
    'password': '******',
    'oneMonth': '1',
}

post_response = requests.post(
    url='http://dig.chouti.com/login',
    data=login_data,
    cookies=cookies,
)

vote_post = requests.post(
    url="http://dig.chouti.com/link/vote?linksId=16150731",
    cookies=cookies
)

print(vote_post.text)

