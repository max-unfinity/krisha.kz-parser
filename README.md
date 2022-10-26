krisha.kz Scrapy parser
-----------------------

Parses prices on real estate at https://krisha.kz for further analysing.

Some results I've got after analysing appartments for a rent in Astana and
Almaty:

Long-term:

![output/astana_vs_almaty_longterm.jpg](./output/astana_vs_almaty_longterm.jpg)

Short-term:

![output/astana_vs_almaty_shortterm.jpg](./output/astana_vs_almaty_shortterm.jpg)

To start parse you need scrapy installed:

`pip install scrapy`

 

Running script
--------------

1.  Go to https://krisha.kz and set parameters:

![](img/screen1.png)

2. Click “Показать результаты”

3. Copy link in your browser (Chrome: Ctrl+L, then Ctrl+C). It will be
`base_url` parameter.

4. Go to the end of the page, find what the number of the last page (**54** in
this example)

It will be `n_pages` parameter.

![](img/screen2.png)

5. In command line run:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
scrapy crawl prices_spider -a base_url="https://krisha.kz/arenda/kvartiry/astana/?das[live.rooms]=1&das[rent.period]=1" -a n_pages=2 -O output/test.json
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 
