# Data Collection

## Moneycontrol

### What's done?

Moneycontrol has static pages, hence data is scraped by iterating each section of the page and navigating via pagenation links.

### Tools and Technology

- Python 3.x
- Scrapy

### How to run?

```bash
scrpy crawl newsScraper -o filename.json
```

## Economic Times

Unlike moneycontrol, economic times has dynamic pages which is loaded via javascript. To tackle the issue, the following approach has been implemented.

A helper module is created in order to tackle the dynamically generated
content in economic times page. The module uses beautifulsoup and
selinium driver to execute javascript injection so that it can collect
the URLs alone as fast as possible.

The collected URLs are then passed to our scrapy project which scrapes
data and generates the json same like how it's implemented for
moneycontrol

### Tools and Technology

- Python 3.x
- Scrapy
- BeautifulSoup
- Selinium

### How to run?

For helper module

```bash
python scrapeNews.py
```

For scrapy

```bash
scrapy crawl NewsScraper -a filename="path-to-links-file" -o filename.json
```
