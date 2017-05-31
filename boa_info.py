from selenium import webdriver

path = '/Users/Rodolfo/Desktop/chrome-bot/chromedriver'
chrome_path = path

option = webdriver.ChromeOptions()
option.add_argument('--incognito')

driver = webdriver.Chrome(chrome_path, chrome_options=option)
driver.get('http://www.lllreptile.com/')
driver.find_element_by_xpath("""//*[@id="sidebar"]/nav/ul/li[1]/a""").click()
driver.find_element_by_xpath("""//*[@id="content"]/div/div[3]/div[2]/div/div[1]/h3/a""").click()
posts = driver.find_elements_by_class_name('product-wrap')

for post in posts:
    print(post.text + '\n')
