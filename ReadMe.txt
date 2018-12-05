Since this project uses scrapy,
please install scrapy beforehand. >_<
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

How to use.............

change dir to root folder (Temp) of the project.
use scrapy's command to run spider.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
scrapy crawl peter -o [dumpfile.filetype] #uses json line (.jl) currently
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
if you want to crawl using cache, use scrapy's JOBDIR parameter.
(please refer to the original documentation for this)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
limitations(?)

currently, this spider can only crawl specific categories provided by user

please add the url of the categories (http://www.mizzimaburmese.com/(news:special-news:bla bla))
in start url list of the 
Temp/temp/spiders/peter.py

----------------------------------------------------------------------------------------------------------------------------------------------------------------------