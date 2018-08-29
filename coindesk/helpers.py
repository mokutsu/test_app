import requests


def get_coindesk_data():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    r = requests.get(url, params={})
    coindesk_data = r.json()
    coindesk_data_list = {'coindesk_data': coindesk_data}
    return coindesk_data_list
