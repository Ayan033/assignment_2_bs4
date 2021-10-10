# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


class Currency:

    def get_currency_data(self, currency_name):

        data_list = []

        url = r'https://coinmarketcap.com/currencies/%s' % (currency_name)  # url для второй страницы

        r = requests.get(url)

        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')

            web_data = soup.find('div', class_='sc-16r8icm-0 nds9rn-0 dAxhCK')
            data_table = web_data.div.table

            for j in data_table.find_all("tr"):
                data_list.append(str(j.th.text + ' : ' + j.td.text))

            return data_list
        else:
            return 'Error: ' + str(r.status_code)