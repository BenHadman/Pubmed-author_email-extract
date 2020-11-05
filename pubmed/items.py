# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AuthorItem(scrapy.Item):
    FullTextLink =scrapy.Field()     #ȫ������
    TitleName = scrapy.Field()       #���±���
    AuthorsName = scrapy.Field()     #��������
    Citation = scrapy.Field()        #����
    AuthorInformation = scrapy.Field() #������Ϣ
    Abstract = scrapy.Field()        #ժҪ
    pmid = scrapy.Field()            #PMID
    AI = scrapy.Field()
    email = scrapy.Field()
