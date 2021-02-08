BOT_NAME = 'wyelandsbank'
SPIDER_MODULES = ['wyelandsbank.spiders']
NEWSPIDER_MODULE = 'wyelandsbank.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'DEBUG'
USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
ITEM_PIPELINES = {
   'wyelandsbank.pipelines.DatabasePipeline': 300,
}
