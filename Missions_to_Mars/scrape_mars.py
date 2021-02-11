
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo



executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')


# NASA Mars News
news_title = news_soup.find_all('div', class_='content_title')[0].text
news_p = news_soup.find_all('div', class_='article_teaser_body')[0].text

print(news_title)
print("--------------------------------------------------------------------")
print(news_p)


# JPL Mars Space Images - Featured Image
jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'
browser.visit(featured_image_url)
html = browser.html
images_soup = BeautifulSoup(html, 'html.parser')


image_path = images_soup.find_all('img')[-1]["src"]
featured_image_url = jpl_url + image_path
print(featured_image_url)


#Mars Facts
facts_url = 'https://space-facts.com/mars/'
tables = pd.read_html(facts_url)
tables


#Use Pandas to convert the data to a HTML table string
mars_facts_df = tables[2]
mars_facts_df.columns = ["Description", "Value"]
mars_facts_df


mars_html_table = mars_facts_df.to_html()
mars_html_table.replace('\n', '')
print(mars_html_table)


#Mars Hemispheres
usgs_url = 'https://astrogeology.usgs.gov'
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html,'html.parser')


# hemispheres item elements
mars_hems = soup.find('div',class_='collapsible results')
mars_item = mars_hems.find_all('div',class_='item')
hemisphere_image_urls = []


# Loop through each hemisphere item
for item in mars_item:

    try:
        # Extract title
        hem=item.find('div',class_='description')
        title=hem.h3.text
        # Extract image url
        hem_url = hem.a['href']
        browser.visit(usgs_url+hem_url)
        html = browser.html
        soup = BeautifulSoup(html,'html.parser')
        image_src = soup.find('li').a['href']
        if (title and image_src):
            # Print results
            print('-'*50)
            print(title)
            print(image_src)
        # Create dictionary for title and url
        hem_dict = {
            'title':title,
            'image_url':image_src
        }
        hemisphere_image_urls.append(hem_dict)
    except Exception as e:
        print(e)

