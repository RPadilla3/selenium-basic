from selenium import webdriver
chrome_path = '/Users/Rodolfo/Desktop/chrome-bot/chromedriver'

option = webdriver.ChromeOptions()
option.add_argument('--incognito')

driver = webdriver.Chrome(chrome_path, chrome_options=option)
driver.get('https://washingtondc.craigslist.org/')
driver.find_element_by_xpath("""//*[@id="hhh0"]/li[1]/a""").click()
posts = driver.find_elements_by_class_name('result-row')

for post in posts:
    print(post.text + '\n')

driver.find_element_by_xpath("""//*[@id="searchform"]/div[5]/div[3]/span[2]/a[3]""").click()
posts2 = driver.find_elements_by_class_name('result-row')

for post in posts2:
    print(post.text + '\n')
