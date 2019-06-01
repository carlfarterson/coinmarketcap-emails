from chrome import Chrome
import coinmarketcap

if __name__ == '__main__':

    chrome = Chrome()
    coinmarketcap.run(chrome)
    chrome.web.close()
