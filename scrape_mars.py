# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

def scrape():
    browser = Browser('chrome', headless=False)
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    title = soup.div.find(class_="content_title").text.strip()
    paragraph = soup.div.find(class_="image_and_description_container").text.strip()
    print(title)
    print(paragraph)

    #retrieve url link to large size featured image

    browser = Browser('chrome', headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find_all('article', class_='carousel_item')

    for result in results:
    # Retrieve url to where full size featured image is located
        img = result.find('a')['data-link']
        

        
    data_link ='https://www.jpl.nasa.gov' + str(img)


    #go to new url and find the url for full size featured image
    #browser = Browser('chrome', headless=False)
    browser.visit(data_link)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    results3 = soup.find_all('figure', class_='lede')
    for result in results3:
    # Retrieve url to where full size featured image is located
        featured_image_url = result.find('img')['src']
    featured_image_url = "https://www.jpl.nasa.gov" +str(featured_image_url)
    print(featured_image_url)


    #Visit Twitter Page and pull latest tweet about Mars Weather
    url ="https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    # HTML object
    html = browser.html
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')

    #Retrieve Latest tweet that has weather data
    mars_weather = [p for p in soup.body.find_all('p') if 'Sol' in p.text][0].text
    print(mars_weather)


    #use pandas to scrape data about Mars
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    tables =tables[0]
    tables.columns = ['Mars Property','Data']
    print(tables)

    #convert dataframe to HTML
    mars_table =tables.to_html()
    #Create hemisphere url dict
    hemisphere_image_urls = []

    #Retrieve Mars Hemispheres Images:
        #Cerberus Hemisphere IMG

    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    cerberus= soup.find_all('div', class_='downloads')

    for result in cerberus:
    # Retrieve url to where full size featured image is located
        cerberus_hemi_img = result.find('a')['href']
        hemi_1 = {'title': 'Cerberus Hemisphere', 'img_url': str(cerberus_hemi_img) }
        #append cerberus to hemi dict
        hemisphere_image_urls.append(hemi_1)


    #schiaparelli hemisphere
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    browser.visit(url)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    schiaparelli = soup.find_all('div', class_='downloads')
    for result in schiaparelli:
    # Retrieve url to where full size featured image is located
        schiaparelli_hemi_img = result.find('a')['href']
        hemi_2 = {'title': 'Schiaparelli Hemisphere', 'img_url': str(schiaparelli_hemi_img) }
        #append to hemi dict
        hemisphere_image_urls.append(hemi_2)

    #Syrtis_major Hemi
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    syrtis_major = soup.find_all('div', class_='downloads')
    for result in syrtis_major:
    # Retrieve url to where full size featured image is located
        syrtis_hemi_img = result.find('a')['href']
        hemi_3 = {'title': 'Syrtis Major Hemisphere', 'img_url': str(syrtis_hemi_img) }
        #append to hemi dict
        hemisphere_image_urls.append(hemi_3)


    #Valles Marineris Hemisphere
    browser = Browser('chrome', headless=False)
    url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url)
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    valles = soup.find_all('div', class_='downloads')
    for result in valles:
    # Retrieve url to where full size featured image is located
        valles_hemi_img = result.find('a')['href']
        
        hemi_4 = {'title': 'Valles Marineris Hemisphere', 'img_url': str(valles_hemi_img) }
        #append to hemi dict
        hemisphere_image_urls.append(hemi_4)
    print(hemisphere_image_urls)
scrape()

