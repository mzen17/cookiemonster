from selenium import webdriver

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
urls = ["globo.com", "baidu.com", "bilibili.com", "qq.com", "yahoo.co.jp", "docomo.ne.jp", "yandex.ru", "doen.ru", "mail.ru", "vk.com", "turbopages.org", "t.me", "samsung.com", "naver.com", "google.com", "wikipedia.com", "Facebook.com", "twitter.com", "bing.com", "youtube.com"]


# Dig 
for url in urls:
    try:
        print("Getting: " + url)
        driver.get("https://" + url)
        cookies = driver.get_cookies()
        website_cookies.append((url, len(cookies)))
        for cookie in cookies:
            if cookie['name'] in cookies:
                cookies_stat[cookie['name']] += 1
            else:
                cookies_stat[cookie['name']] = 1
    except:
        print("Error: " + url)
        continue

# Print results
print("Website cookies:")
print(website_cookies)
print("Cookie frequency:")
print(cookies_stat)

