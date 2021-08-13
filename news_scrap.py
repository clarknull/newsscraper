import datetime, pytz
import newspaper



class NewsScraper:

    def __init__(self):
        
        # list of sources
        # can be made dynamic with a simple json file
        
        self.sources = ["https://www.legit.ng/", "https://punchng.com/",
                        "http://dailypost.ng/", "http://pulse.ng/", "http://www.premiumtimesng.com/",
                        "http://www.saharareporters.com/", "http://guardian.ng/",
                        "http://www.dailytrust.com.ng/", "http://tribuneonlineng.com/",
                        "http://www.thisdaylive.com/", "http://www.247nigerianewsupdate.co/",
                        "http://thecable.ng/", "http://www.nigerianbulletin.com/",
                        "http://www.leadership.ng/", "http://www.newsrescue.com/",
                        "http://www.ynaija.com/", "http://www.nigeriaworld.com/"]

        config = newspaper.Config()
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
        config.browser_user_agent = user_agent
        
        #necessary if you have a slow internet connection
        config.request_timeout = 60
        
        self.config = config

    def scrap(self):
        counter = 0
        now = datetime.datetime.now(tz=pytz.utc)
        for news_source in self.sources:
            source = newspaper.build(news_source, memoize_articles=False, config=self.config)
            print(news_source,' has ', len(source.articles))
            for article in source.articles:
                counter += 1
                article.download()
                article.parse()
                if article.publish_date:
                    # get recent articles
                    date = article.publish_date.astimezone()
                    time_diff = now - datetime.timedelta(weeks=2)
                    if article.publish_date > time_diff:
                        # perform your logic
                        print(article.title)
                        print('\n')

            # can be useful on slow processors 
            if counter > 50:
                time.sleep(2)
                counter = 0

if __name__ == '__main__':    
    scraper = NewsScraper()
    scraper.scrap()
