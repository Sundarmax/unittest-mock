import requests


def len_user():
    joke = get_user()
    return len(joke)


def convert_integer(n):
    return int(n)


def get_user():
    url = 'https://reqres.in/api/users?page=2'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # print(data,type(data))
        return data['data']
    elif response.status_code in [500, 504]:
        return 'Connection error was raised'
    else:
        return {}


if __name__ == '__main__':
    print(len_user())