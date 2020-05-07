
#from selenium import webdriver

#browser = webdriver.chrome()
#browser.get('http://selenium.dev/')




#tk  import pymongo
#from sys import platform

#print (selenium.__file__)

#Defs



def scrape():
    print("scrape_mars    scrape rtn")
	
	
    #tk moved imports to here
	#Imports
    from splinter import Browser
    from bs4 import BeautifulSoup as bs
    import pandas as pd
    import requests
    import time
    import re

 
    #tk moved to hetk 
	#def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    #tk return Browser("chrome", **executable_path, headless=True)
    browser =  Browser("chrome", **executable_path, headless=False)
	
    #tk browser = init_browser()
    mars_data_scrape = {}


    mars_news = 'https://mars.nasa.gov/news/'
    browser.visit(mars_news)
    time.sleep(2)
    html = browser.html
    news_soup = bs(html, 'html.parser')


#Data Scrape
    print("#Data Scrape")

    news_title = news_soup.find('div', class_='content_title').get_text()
    news_p = news_soup.find('div', class_='article_teaser_body').get_text()
    time.sleep(2)

    mars_data_scrape["data1"] = news_title
    mars_data_scrape["data2"] = news_p



#Paths
    print("#Paths")


#executable_path = {"executable_path": "chromedriver"}
#browser = Browser("chrome", **executable_path, headless=True)
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)
    browser.click_link_by_partial_text('more info')
    time.sleep(2)
    browser.click_link_by_partial_text('.jpg')


#Soup
    print("#Soup")


    html = browser.html
    jpl_soup = bs(html, 'html.parser')

    featured_img_url = jpl_soup.find('img').get('src')

    mars_data_scrape["image"] = featured_img_url



#Weather
    print("#Weather")

    weather_url = 'https://twitter.com/marswxreport?lang=en'
    html = requests.get(weather_url)
    beautiful_soup = bs(html.text, 'html.parser')

    #tk mars_weather = weather_soup.find_all(string=re.compile("Sol"), 
	#tk class_ = "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")[0].text

    #tk mars_data_scrape["weather"] = mars_weather


#SpaceFacts
    print("#SpaceFacts")


    mars_facts_url = 'https://space-facts.com/mars/'
    table_df = pd.read_html(mars_facts_url)[0]
    table_df.columns = ["description", "value"]
    table_df = table_df.set_index('description', drop=True)
    mars_data_scrape["table"] = table_df.to_html()




# In[35]:
    print("#In35")


#executable_path = {"executable_path": "chromedriver.exe"}
#browser = Browser("chrome", **executable_path, headless=True)
    hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hem_url)

    html = browser.html
    hem_soup = bs(html, 'html.parser')


#Final
    print("#Final")


    hem_img_urls = []
    hem_dict = {'title': [], 'img_url': [],}

    x = hem_soup.find_all('h3')


    for i in x:
        t = i.get_text()
        title = t.strip('Enhanced')
        browser.click_link_by_partial_text(t)
        hem_url = browser.find_link_by_partial_href('download')['href']
        hem_dict = {'title': title, 'img_url': hem_url}
        hem_img_urls.append(hem_dict)
        browser.back()

    mars_data_scrape["hemispheres"] = hem_img_urls
    
    #tk added print
    print(mars_data_scrape)
	
    return mars_data_scrape
