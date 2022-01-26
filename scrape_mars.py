from bs4 import BeautifulSoup as bs
import requests
import pymongo
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import pandas as pd

def scrape():


    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless = False)
    url = 'https://redplanetscience.com'
    browser.visit(url)




    html = browser.html
    soup = bs(html, 'html.parser')
    headline_title = soup.find('div', class_='content_title').text
    headline_teaser = soup.find('div', class_='article_teaser_body').text
    headline_title



    url = 'https://spaceimages-mars.com/'
    browser.visit(url)



    html = browser.html
    soup = bs(html, 'html.parser')

    featured_image = soup.find('img', class_='headerimage')['src']
    featured_image_url = 'https://spaceimages-mars.com/' + featured_image
    featured_image_url



    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    mars_facts = tables[0]
    mars_facts.columns = mars_facts.columns.get_level_values(0)
    mars_facts




    url = 'https://marshemispheres.com/cerberus.html'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    cerberus_title = soup.find('h2', class_='title').text
    cerberus_pic = 'images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg'
    cerberus_pic_url = 'https://marshemispheres.com/' + cerberus_pic





    url = 'https://marshemispheres.com/schiaparelli.html'
    browser.visit(url)


    # In[10]:


    html = browser.html
    soup = bs(html, 'html.parser')
    schiaparelli_title = soup.find('h2', class_='title').text
    schiaparelli_pic = 'images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg'
    schiaparelli_pic_url = 'https://marshemispheres.com/' + schiaparelli_pic


    # In[11]:


    url = 'https://marshemispheres.com/syrtis.html'
    browser.visit(url)




    html = browser.html
    soup = bs(html, 'html.parser')
    syrtis_title = soup.find('h2', class_='title').text
    syrtis_pic = 'images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg'
    syrtis_pic_url = 'https://marshemispheres.com/' + syrtis_pic


    # In[13]:


    url = 'https://marshemispheres.com/valles.html'
    browser.visit(url)


    # In[14]:


    html = browser.html
    soup = bs(html, 'html.parser')
    valles_title = soup.find('h2', class_='title').text
    valles_pic = 'images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg'
    valles_pic_url = 'https://marshemispheres.com/' + valles_pic


    # In[15]:


    hemisphere_image_urls = [
        {"title": valles_title, "img_url": valles_pic_url},
        {"title": cerberus_title, "img_url": cerberus_pic_url}, 
        {"title": schiaparelli_title, "img_url": schiaparelli_pic_url},
        {"title": syrtis_title, "img-url": syrtis_pic_url},
    ]
  


    # In[ ]:

    mars = {"news_title": headline_title,
        "text": headline_teaser,
        "featured image": featured_image, 
        "featured_image_url": featured_image_url,
        # "Mars Facts": mars_facts,
        "valles_title": valles_title, "valles_pic_url": valles_pic_url,
        "cerberus_title": cerberus_title, "cerberus_pic_url": cerberus_pic_url,
        "schiaparelli_title": schiaparelli_title, "schiaparelli_pic_url": schiaparelli_pic_url,
        "syrtis_title": syrtis_title, "syrtis_pic_url": syrtis_pic_url
    }


    print(mars)
    browser.quit()
    return mars






