# NIGERIAN NEWS SCRAPER (Python 3)

This project demonstrate how easy it is to build a simple news web scraper using python and newspaper3k library.  

### Motivation Behind This
I was working on a project that needed to keep users up-to date with specific news update. As a python developer, scraping was the only option. But as a lazy person, the work involved was daunting. After some 30min of research, i came across [newspaper3k](https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html#performing-nlp-on-an-article) and my problem was solved. I've decided to share this hoping to motivate some hard working programmers. The newspaper3k library also has some NLP features which can be used to further filter out some articles. 

## Dependencies

```bash
pip3 install newspaper3k

#required for nlp
curl https://raw.githubusercontent.com/codelucas/newspaper/master/download_corpora.py | python3
```
for full installation guide, please visit the newspaper3k [documentation](https://newspaper.readthedocs.io/en/latest/#get-it-now)

## Extra Note

In some part of the world, having a slow computer system and a slow internet connection is very very common. I had to make the code sleep a bit to free up resources for other system processes. Feel free to make if fly as you wish.

```python
#sleep for 2 seconds after fetching 50 articles
 if counter > 50:
    time.sleep(2)
    counter = 0
```



## License
[MIT](https://choosealicense.com/licenses/mit/)
