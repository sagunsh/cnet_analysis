# Analyzing CNET's Headlines

Data for this analysis is scraped from https://www.cnet.com/sitemaps/articles/

## Install Requirements

* For mac and linux
    
      $ pip install -r requirements.txt
      
* For windows use Anaconda and install required packages from requirements.txt

## Scraping Data
  
    $ scrapy runspider cnet_scraper.py -o cnet_data.csv # for csv
    $ scrapy runspider cnet_scraper.py -o cnet_data.json # for json
    
## Running Jupyter Notebook

    $ jupyter notebook