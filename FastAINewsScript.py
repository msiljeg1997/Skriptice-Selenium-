from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from urllib.parse import urlparse

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)


driver.get("https://news.ycombinator.com/news")
driver.maximize_window()

links = driver.find_elements("xpath", "//a[@href]")
keywords = ["AI", "GPT", "gpt", "artificial intelligence", "Artificial Intelligence" ]
max_clicks = 10
clicks = 0
clicked_urls = set()

for link in links:
    if any(keyword in link.get_attribute("innerHTML") for keyword in keywords):
        link_url = link.get_attribute("href")
        if link_url not in clicked_urls:
            ActionChains(driver).key_down(Keys.COMMAND).click(link).key_up(Keys.CONTROL).perform()
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(1)
            current_url = driver.current_url
            clicked_urls.add(link_url)
            if urlparse(link_url).netloc in urlparse(current_url).netloc:
                clicks += 1
                if clicks >= max_clicks:
                    break
            driver.switch_to.window(driver.window_handles[-1])
            driver.switch_to.window(driver.window_handles[0])
        else:
            break