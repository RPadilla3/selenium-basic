from selenium import webdriver
path = '/Users/Rodolfo/Desktop/chrome-bot/chromedriver'
chrome_path = path

option = webdriver.ChromeOptions()
option.add_argument('--incognito')

ghost = webdriver.Chrome(chrome_path, chrome_options=option)
ghost.get('http://www.lllreptile.com/')
ghost.find_element_by_xpath("""//*[@id="sidebar"]/nav/ul/li[4]/a""").click()
ghost.find_element_by_xpath("""//*[@id="content"]/div/div[2]/div[2]/div/div[1]/h3/a""").click()

posts = ghost.find_elements_by_class_name('product-wrap')

for post in posts:
    print(post.text + '\n')
