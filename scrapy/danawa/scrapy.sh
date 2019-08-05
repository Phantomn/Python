#!/bin/bash

cd /home/ubuntu/Python/scrapy/danawa/
PATH=$PATH:/usr/local/bin
export PATH
scrapy crawl danawa
cp /home/ubuntu/Python/scrapy/danawa/danawa.json /home/ubuntu/danawa.json
