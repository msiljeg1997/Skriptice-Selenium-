from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from urllib.parse import urlparse
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)



# driver.get("https://news.ycombinator.com/news")
# driver.maximize_window()

# keywords = ["AIs", "AI", "ai", "gpt", "GPT" ]
# max_clicks = 10
# clicks = 0
# clicked_urls = set()
# keyword_counts1 = {keyword: 0 for keyword in keywords}
# keyword_counts2 = {keyword: 0 for keyword in keywords}

# while True:
#     titlelines = driver.find_elements(By.CLASS_NAME, "titleline")
#     for titleline in titlelines:
#         links = titleline.find_elements(By.TAG_NAME, "a")
#         for link in links:
#             link_url = link.get_attribute("href")
#             if link_url not in clicked_urls:
#                 clicked_urls.add(link_url)
#                 driver.execute_script("window.open('{}', '_blank');".format(link_url))
#                 driver.switch_to.window(driver.window_handles[-1])
#                 time.sleep(1)
#                 for keyword in keywords:
#                     if keyword in driver.page_source:
#                         keyword_counts1[keyword] += 1
#                         keyword_counts2[keyword] += driver.page_source.count(keyword)
#                 driver.close()
#                 driver.switch_to.window(driver.window_handles[0])
#     if len(clicked_urls) >= max_clicks:
#         break

# print("Keyword counts 1:", keyword_counts1)
# print("Keyword counts 2:", keyword_counts2)


# driver.get("https://news.ycombinator.com/news")
# driver.maximize_window()

# keywords = ["AIs", "AI", "ai", "gpt", "GPT"]
# max_clicks = 10
# clicks = 0
# clicked_urls = set()
# keyword_counts1 = {keyword: 0 for keyword in keywords}
# keyword_counts2 = {keyword: 0 for keyword in keywords}

# while True:
#     titlelines = driver.find_elements(By.CLASS_NAME, "titleline")
#     for titleline in titlelines:
#         links = titleline.find_elements(By.TAG_NAME, "a")
#         for link in links:
#             link_text = link.text.lower()
#             if "comments" in link_text:
#                 link_url = link.get_attribute("href")
#                 if link_url not in clicked_urls:
#                     clicked_urls.add(link_url)
#                     driver.execute_script("window.open('{}', '_blank');".format(link_url))
#                     driver.switch_to.window(driver.window_handles[-1])
#                     time.sleep(1)
#                     for keyword in keywords:
#                         if keyword in driver.page_source:
#                             keyword_counts1[keyword] += 1
#                             keyword_counts2[keyword] += driver.page_source.count(keyword)
#                     driver.close()
#                     driver.switch_to.window(driver.window_handles[0])
#         for link in links:
#             link_text = link.text.lower()
#             if "comments" not in link_text:
#                 link_url = link.get_attribute("href")
#                 if link_url not in clicked_urls:
#                     clicked_urls.add(link_url)
#                     driver.execute_script("window.open('{}', '_blank');".format(link_url))
#                     driver.switch_to.window(driver.window_handles[-1])
#                     time.sleep(1)
#                     for keyword in keywords:
#                         if keyword in driver.page_source:
#                             keyword_counts1[keyword] += 1
#                             keyword_counts2[keyword] += driver.page_source.count(keyword)
#                     driver.close()
#                     driver.switch_to.window(driver.window_handles[0])
#     if len(clicked_urls) >= max_clicks:
#         break

# print("Keyword counts 1:", keyword_counts1)
# print("Keyword counts 2:", keyword_counts2)

driver.get("https://news.ycombinator.com/news")
driver.maximize_window()

keywords = ["AIs", "AI", "ai", "gpt", "GPT"]
max_clicks = 10
clicks = 0
clicked_urls = set()
keyword_counts1 = {keyword: 0 for keyword in keywords}
keyword_counts2 = {keyword: 0 for keyword in keywords}

while True:
    titlelines = driver.find_elements(By.CLASS_NAME, "titleline")
    for titleline in titlelines:
        links = titleline.find_elements(By.TAG_NAME, "a")
        for link in links:
            if ("sitebit comhead" in titleline.get_attribute("class")) and ("sitebit" in link.get_attribute("class")):
                continue
            link_url = link.get_attribute("href")
            if link_url not in clicked_urls:
                clicked_urls.add(link_url)
                driver.execute_script("window.open('{}', '_blank');".format(link_url))
                driver.switch_to.window(driver.window_handles[-1])
                time.sleep(1)
                for keyword in keywords:
                    if keyword in driver.page_source:
                        keyword_counts1[keyword] += 1
                        keyword_counts2[keyword] += driver.page_source.count(keyword)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
    if len(clicked_urls) >= max_clicks:
        break

print("Keyword counts 1:", keyword_counts1)
print("Keyword counts 2:", keyword_counts2)