# Scrapy_Crawler

---

Here we are using  **Scrapy 1.6** framework for webcrawling
Scrapy is an open source and collaborative framework for extracting the data you need from websites in a fast, simple, yet extensible way.

---

## Getting Started

- Installation `pip install scrapy` or `conda install -c conda-forge scrapy`

```python
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('div.prev-post > a'):
            yield response.follow(next_page, self.parse)
```

- Run Scrapy `scrapy runspider myspider.py`

---

## Creating a Project

- `scrapy startproject tutorial`

This will create a `tutorial` directory with the following contents:

```bash
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
```