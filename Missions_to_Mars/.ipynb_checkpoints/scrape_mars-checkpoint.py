{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "from splinter import Browser\n",
    "from bs4 import BeautifulSoup\n",
    "import pandas as pd\n",
    "import requests\n",
    "import pymongo\n",
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "executable_path = {'executable_path': 'chromedriver'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://mars.nasa.gov/news/'\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "news_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mars Now\n",
      "--------------------------------------------------------------------\n",
      "How two new technologies will help Perseverance, NASA’s most sophisticated rover yet, touch down onto the surface of Mars this month.\n"
     ]
    }
   ],
   "source": [
    "# NASA Mars News\n",
    "news_title = news_soup.find_all('div', class_='content_title')[0].text\n",
    "news_p = news_soup.find_all('div', class_='article_teaser_body')[0].text\n",
    "\n",
    "print(news_title)\n",
    "print(\"--------------------------------------------------------------------\")\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "# JPL Mars Space Images - Featured Image\n",
    "jpl_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'\n",
    "featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg'\n",
    "browser.visit(featured_image_url)\n",
    "html = browser.html\n",
    "images_soup = BeautifulSoup(html, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.htmlhttps://data-class-jpl-space.s3.amazonaws.com/JPL_Space/image/featured/mars2.jpg\n"
     ]
    }
   ],
   "source": [
    "image_path = images_soup.find_all('img')[-1][\"src\"]\n",
    "featured_image_url = jpl_url + image_path\n",
    "print(featured_image_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[                      0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers,\n",
       "   Mars - Earth Comparison             Mars            Earth\n",
       " 0               Diameter:         6,779 km        12,742 km\n",
       " 1                   Mass:  6.39 × 10^23 kg  5.97 × 10^24 kg\n",
       " 2                  Moons:                2                1\n",
       " 3      Distance from Sun:   227,943,824 km   149,598,262 km\n",
       " 4         Length of Year:   687 Earth days      365.24 days\n",
       " 5            Temperature:     -87 to -5 °C      -88 to 58°C,\n",
       "                       0                              1\n",
       " 0  Equatorial Diameter:                       6,792 km\n",
       " 1       Polar Diameter:                       6,752 km\n",
       " 2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       " 3                Moons:            2 (Phobos & Deimos)\n",
       " 4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       " 5         Orbit Period:           687 days (1.9 years)\n",
       " 6  Surface Temperature:                   -87 to -5 °C\n",
       " 7         First Record:              2nd millennium BC\n",
       " 8          Recorded By:           Egyptian astronomers]"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Mars Facts\n",
    "facts_url = 'https://space-facts.com/mars/'\n",
    "tables = pd.read_html(facts_url)\n",
    "tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Description</th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Description                          Value\n",
       "0  Equatorial Diameter:                       6,792 km\n",
       "1       Polar Diameter:                       6,752 km\n",
       "2                 Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                Moons:            2 (Phobos & Deimos)\n",
       "4       Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5         Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                   -87 to -5 °C\n",
       "7         First Record:              2nd millennium BC\n",
       "8          Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Use Pandas to convert the data to a HTML table string\n",
    "mars_facts_df = tables[2]\n",
    "mars_facts_df.columns = [\"Description\", \"Value\"]\n",
    "mars_facts_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<table border=\"1\" class=\"dataframe\">\n",
      "  <thead>\n",
      "    <tr style=\"text-align: right;\">\n",
      "      <th></th>\n",
      "      <th>Description</th>\n",
      "      <th>Value</th>\n",
      "    </tr>\n",
      "  </thead>\n",
      "  <tbody>\n",
      "    <tr>\n",
      "      <th>0</th>\n",
      "      <td>Equatorial Diameter:</td>\n",
      "      <td>6,792 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>1</th>\n",
      "      <td>Polar Diameter:</td>\n",
      "      <td>6,752 km</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>2</th>\n",
      "      <td>Mass:</td>\n",
      "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>3</th>\n",
      "      <td>Moons:</td>\n",
      "      <td>2 (Phobos &amp; Deimos)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>4</th>\n",
      "      <td>Orbit Distance:</td>\n",
      "      <td>227,943,824 km (1.38 AU)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>5</th>\n",
      "      <td>Orbit Period:</td>\n",
      "      <td>687 days (1.9 years)</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>6</th>\n",
      "      <td>Surface Temperature:</td>\n",
      "      <td>-87 to -5 °C</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>7</th>\n",
      "      <td>First Record:</td>\n",
      "      <td>2nd millennium BC</td>\n",
      "    </tr>\n",
      "    <tr>\n",
      "      <th>8</th>\n",
      "      <td>Recorded By:</td>\n",
      "      <td>Egyptian astronomers</td>\n",
      "    </tr>\n",
      "  </tbody>\n",
      "</table>\n"
     ]
    }
   ],
   "source": [
    "mars_html_table = mars_facts_df.to_html()\n",
    "mars_html_table.replace('\\n', '')\n",
    "print(mars_html_table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Mars Hemispheres\n",
    "usgs_url = 'https://astrogeology.usgs.gov'\n",
    "url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "browser.visit(url)\n",
    "html = browser.html\n",
    "soup = BeautifulSoup(html,'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "# hemispheres item elements\n",
    "mars_hems = soup.find('div',class_='collapsible results')\n",
    "mars_item = mars_hems.find_all('div',class_='item')\n",
    "hemisphere_image_urls = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------------------------------------------------\n",
      "Cerberus Hemisphere Enhanced\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg\n",
      "--------------------------------------------------\n",
      "Schiaparelli Hemisphere Enhanced\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg\n",
      "--------------------------------------------------\n",
      "Syrtis Major Hemisphere Enhanced\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg\n",
      "--------------------------------------------------\n",
      "Valles Marineris Hemisphere Enhanced\n",
      "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg\n"
     ]
    }
   ],
   "source": [
    "# Loop through each hemisphere item\n",
    "for item in mars_item:\n",
    "\n",
    "    try:\n",
    "        # Extract title\n",
    "        hem=item.find('div',class_='description')\n",
    "        title=hem.h3.text\n",
    "        # Extract image url\n",
    "        hem_url = hem.a['href']\n",
    "        browser.visit(usgs_url+hem_url)\n",
    "        html = browser.html\n",
    "        soup = BeautifulSoup(html,'html.parser')\n",
    "        image_src = soup.find('li').a['href']\n",
    "        if (title and image_src):\n",
    "            # Print results\n",
    "            print('-'*50)\n",
    "            print(title)\n",
    "            print(image_src)\n",
    "        # Create dictionary for title and url\n",
    "        hem_dict = {\n",
    "            'title':title,\n",
    "            'image_url':image_src\n",
    "        }\n",
    "        hemisphere_image_urls.append(hem_dict)\n",
    "    except Exception as e:\n",
    "        print(e)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:PythonData]",
   "language": "python",
   "name": "conda-env-PythonData-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
