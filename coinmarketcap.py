import pandas as pd
import chrome
import time


def run(chrome):

    data = pd.read_csv('webpages.csv')
    data = data[data.columns[1:]]

    for i, row in data.iterrows():
        if type(row['website']) == 'string':
            continue
        time.sleep(1)

    # data = []
    #
    # chrome.get_url('https://coinmarketcap.com/all/views/all/')
    # table = chrome.load_element('table[@id="currencies-all"]/tbody/tr')
    #
    # for i in range(500):
    #
    #     coin = table[i]
    #
    #     symbol = coin.find_element_by_xpath('td[2]/span/a').text
    #     name = coin.find_element_by_xpath('td[2]/a').text
    #     link = coin.find_element_by_xpath('td[2]/a').get_attribute('href')
    #
    #     data.append({
    #         'symbol': symbol,
    #         'name': name,
    #         'link': link
    #     })
    #
    # for coin in data:

        chrome.get_url(row['link'])
        info = chrome.load_element('div/ul/li')

        for fact in info:
            if fact.text == 'Website':
                website = fact.find_element_by_xpath('a').get_attribute('href')
                data['website'].iloc[i] = website
                continue

    # data = pd.DataFrame(data)
    data.to_csv('webpages.csv')
