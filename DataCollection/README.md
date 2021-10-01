# Data Collection

## Scraping Stock News

- Moneycontrol has static pages, hence data is scraped by iterating each section of the page and navigating via pagenation links.

- Economic times has dynamic pages which is loaded via javascript. To tackle the issue, the following approach has been implemented.

  A helper module is created in order to tackle the dynamically generated
  content in economic times page. The module uses beautifulsoup and
  selinium driver to execute javascript injection so that it can collect
  the URLs alone as fast as possible.

  The collected URLs are then passed to our scrapy project which scrapes
  data and generates the json same like how it's implemented for
  moneycontrol

### How to run?

```bash
$ cd DataCollection/stock_news/stock_news/spiders
$ scrapy crawl economic_times -o economic_times_stock_news.json
$ scrapy crawl money_control -o money_control_stock_news.json
```

### Tools and Technology

- Python 3.x
- Scrapy
- BeautifulSoup
- Selinium
