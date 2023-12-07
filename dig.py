from selenium import webdriver
import random

# Base set up. Assumes
# 1) Chromedriver is in path.
# 2) Chrome is installed.

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
options.add_argument('--disable-gpu')  # Disable GPU acceleration
options.add_argument('--no-sandbox')  # Disable sandboxing for Linux
driver = webdriver.Chrome(options=options)

# Data storage initialization 
# A dict to store cookies, and their appearance frequnecy
# Another list to store how many cookies a website has

cookies_stat = {}
website_cookies = []
# URL list to dig

nurls = ["globo.com", "baidu.com", "bilibili.com", "qq.com", "yahoo.co.jp", "docomo.ne.jp", "yandex.ru", "mail.ru", "vk.com", "turbopages.org", "t.me", "samsung.com", "naver.com", "google.com", "wikipedia.com", "facebook.com", "twitter.com", "bing.com", "youtube.com"]
gurls = [ "leboncoin.fr", "orange.fr", "amazon.fr", "google.fr", "free.fr", "caf.fr" , "expressen.se", "google.se", "svt.se", "dn.se", "svtplay.se", "wp.pl", "onet.pl", "allegro.pl", "interia.pl", "o2.pl","google.it", "repubblica.it", "diretta.it", "ansa.it", "mediaset.it"]

# Cut list nurls and list gurls to a random 5 subsection of itself
amount = 15
nurls = random.sample(nurls, amount)
gurls = random.sample(gurls, amount)

ncount = 0;
gcount = 0;
# Dig 
for url in nurls:
    try:
        print("Getting: " + url)
        driver.get("https://" + url)
        cookies = driver.get_cookies()
        website_cookies.append((url, len(cookies)))
        ncount += len(cookies)
        for cookie in cookies:
            if cookie['name'] in cookies:
                cookies_stat[cookie['name']] += 1
            else:
                cookies_stat[cookie['name']] = 1
    except:
        print("Error: " + url)
        continue

for url in gurls:
    #try:
        print("Getting: " + url)
        driver.get("https://" + url)
        cookies = driver.get_cookies()
        website_cookies.append((url, len(cookies)))
        gcount += len(cookies)
        for cookie in cookies:
            if cookie['name'] in cookies:
                cookies_stat[cookie['name']] += 1
            else:
                cookies_stat[cookie['name']] = 1
    #except:
     #   print("Error: " + url)
     #   continue

# Print results

print(gcount)
print(ncount)
print(website_cookies )
