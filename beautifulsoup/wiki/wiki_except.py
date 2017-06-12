from urllib import urlopen, HTTPError
from bs4 import BeautifulSoup
import re
import random
import datetime
random.seed(datetime.datetime.now())

def getLinks(articleUrl):
  try:
    html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
  except HTTPError as e:
    return None
  else:
      bsObj = BeautifulSoup(html, "html.parser")
      return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
                                                                                    #first search ()
                                                                                    #start ^/wiki/
                                                                                    #?!: - ":"is not include
                                                                                    # . - "." one char
                                                                                    #*$ - string end
links = getLinks("/wiki/Kevin_Bacon")

while len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
        if newArticle == None:
                print "Article could not be found"
        else:
                print newArticle
        links = getLinks(newArticle)
