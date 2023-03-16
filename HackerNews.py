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
import sys

# Read keyword from command line argument
if len(sys.argv) < 2:
    print("Usage: python HackerNews.py <keyword>")
    sys.exit(1)
keyword = sys.argv[1]

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)



driver.get("https://news.ycombinator.com/news")
driver.maximize_window()

max_clicks = 10
clicks = 0
clicked_urls = set()
keywords = [keyword]
keyword_counts1 = {keyword: 0 for keyword in keywords}
keyword_counts2 = {keyword: 0 for keyword in keywords}

while True:
    titlelines = driver.find_elements(By.CLASS_NAME, "titleline")
    for titleline in titlelines:
        links = titleline.find_elements(By.TAG_NAME, "a")
        for link in links:
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

while True:
    subtexts = driver.find_elements(By.CLASS_NAME, "subtext")
    for subtext in subtexts:
        links = subtext.find_elements(By.TAG_NAME, "a")
        for link in links:
            if "comments" in link.text:
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

keyword_counts = keyword_counts1.copy()
keyword_counts.update(keyword_counts2)
print("Keyword counts:", keyword_counts)