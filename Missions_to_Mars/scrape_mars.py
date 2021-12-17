#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import requests

#set up browser
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    return browser

#Set up scrape function
def scrape():
    browser = init_browser()
    mmdata = {}
     
    ##NASA Mars News
    #This was the one that was kinda funky so not everything matches the template
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    nt = soup.find('div', class_='content_title')
    news_title = nt.text.strip()
    mmdata['news_title'] = news_title
    np = soup.find('div', class_='article_teaser_body')
    news_p = np.text.strip()
    mmdata['news_p'] = news_p


    ##JPL Mars Space Image
    url2 = 'https://spaceimages-mars.com/'
    browser.visit(url2)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    marsimage = soup.find('img', class_='headerimage fade-in')
    image_url = soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url = url2 + image_url
    mmdata['featured_image_url'] = featured_image_url

    ##Mars Facts
    url3 = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url3)
    mars_earth_df = tables[0]
    me_df = mars_earth_df.rename(columns={0:"Description",1:"Mars",2:"Earth"})
    m_e_df = me_df.set_index("Description")
    m_e_table = m_e_df.to_html()
    metable = m_e_table.replace('\n','')
    mmdata['metable'] = metable

    ##Mars Hemispheres
    titles = []
    urls = []
    url4 = 'https://marshemispheres.com/'
    browser.visit(url4)
    html=browser.html
    soup=BeautifulSoup(html,'html.parser')
    hemis = soup.find_all('div', class_='description')

    #Loop through to get the titles
    counter = 0
    for hem in hemis:
        title = hem.a.find('h3')
        title = title.text
        titles.append(title)
        counter = counter + 1
        if (counter == 4):
            break

    #get the urls for the pages with the images to then find images
    counter = 0
    for hem in hemis:
        src = hem.find('a')['href']
        page_url = url4 + src
        urls.append(page_url)
        counter = counter + 1
        if (counter == 4):
            break

    #Loop to get the images in jpg
    image_urls = []
    for url in urls:
        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        src = soup.find('img',class_="wide-image")['src']
        wide_url = url4 + src
        image_urls.append(wide_url)

    #List of dictionaries
    hemisphere_image_urls = []

    hem1 = {'title':titles[0], 'img_url': image_urls[0]}
    hem2 = {'title':titles[1], 'img_url': image_urls[1]}
    hem3 = {'title':titles[2], 'img_url': image_urls[2]}
    hem4 = {'title':titles[3], 'img_url': image_urls[3]}

    hemisphere_image_urls = [hem1, hem2, hem3, hem4]
    mmdata['hemisphere_image_urls'] = hemisphere_image_urls

    return mmdata

