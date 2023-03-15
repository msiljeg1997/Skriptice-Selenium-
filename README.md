# Skriptice Selenium

## 1. FAST AI NEWS SCRIPT (FastAINewsScript.py)
## INSTRUCTIONS =>

This script is written in Python and uses the Selenium package to automate web browsing. The script visits the news page at "https://news.ycombinator.com/news" and searches for articles containing any of the specified keywords in their title. It then opens the articles in new tabs, up to a maximum number of clicks.

## Prerequisites
Python 3.x installed
Chrome browser installed
The following Python packages installed: selenium, webdriver_manager

## How to use
Install the required Python packages.
Copy the script code into a Python script file.
Adjust the keywords and max_clicks variables as desired.
Run the script.

## Script explanation
Import required packages: selenium, time, urlparse, webdriver_manager.
Set up Chrome browser with the webdriver_manager package.
Visit the news page at "https://news.ycombinator.com/news".
Find all links on the page.
Loop through all links on the page.
For each link, check if it contains any of the specified keywords.
If the link contains a keyword and has not been clicked before, open it in a new tab.
Check the URL of the newly opened tab to ensure it is on the same domain as the original page.
Keep track of clicked URLs in a set.
If the maximum number of clicks has been reached, exit the loop.
Close the new tab and switch back to the original tab.
If a link has already been clicked before, exit the loop.
