from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

format = '%a %b %d %H:%M:%S %Y'

today = datetime.datetime.today()
s = today.strftime(format)
print('Stock Time:', s + '\n')

symbols = ['TSLA', 'AMZN', 'AAPL']

for symbol in symbols:
    option = webdriver.ChromeOptions()
    option.add_argument('--incognito')

    browser = webdriver.Chrome(
        '/Users/Rodolfo/Desktop/chrome-bot/chromedriver', chrome_options=option)
    browser.get('https://finance.yahoo.com/quote/' + symbol + '?p=' + symbol)

    titles_element = browser.find_elements_by_xpath("//td[@class='C(black)']")
    titles = [x.text for x in titles_element]

    values_elements = browser.find_elements_by_xpath("//td[@class='Ta(end) Fw(b)']")
    values = [x.text for x in values_elements]

    print(symbol + ' Daily Stock Report:')

    for title, value in zip(titles, values):
        print('\t' + title + ': ' + value)
