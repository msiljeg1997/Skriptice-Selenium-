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

## 2.FASTER AI NEWS SCRIPT (RUN WITH FLAG)
##INSTRUCTIONS

This Python code uses the Selenium WebDriver API to scrape news articles from the website "https://news.ycombinator.com/news". The script is designed to search for a specific keyword provided as a command line argument and count the number of times it appears on each page that it visits.

The code starts by importing necessary libraries such as Selenium WebDriver, options, keys, action chains, time, urllib.parse, exceptions and system.

Then, it checks if the user provided a keyword in the command line argument. If not, it displays a usage message and exits the script.

After that, the script creates an instance of the Chrome WebDriver and navigates to the Hacker News website. It then maximizes the window.

The code loops over the articles on the website and opens each article in a new tab. If the article has not been visited before, the script searches for the provided keyword on the page and increments the keyword count if it is found.

Once the maximum number of articles have been visited or the provided keyword is not found on any of the visited pages, the code loops over the comments on the website and opens each comment section in a new tab. If the comment section has not been visited before, the script searches for the provided keyword on the page and increments the keyword count if it is found.

Finally, the script prints the keyword counts for each keyword provided as the command line argument.

It is important to note that this script is specific to the Hacker News website and may not work on other websites without significant modifications. 
