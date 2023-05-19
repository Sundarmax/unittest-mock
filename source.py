import requests


def len_user():
    joke = get_user()
    return len(joke)

def get_user():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # print(data,type(data))
        return data['data']
    else:
        return {}


if __name__ == '__main__':
    print(len_user())