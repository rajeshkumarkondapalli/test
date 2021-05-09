# test

python --version  

python -m venv webenv
source webenv/bin/activate

scrapy genspider imdb www.imdb.com
 1020  scrapy crawl imdb
 1021  scrapy crawl imdb -o imdbdata.json -t json