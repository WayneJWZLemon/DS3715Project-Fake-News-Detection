import newspaper
import pandas as pd

homeUrlYahoo = "https://news.yahoo.com/"
homeUrlNYtimes = "https://www.nytimes.com/"
homeUrlWallSt = "https://www.wsj.com/"
homeUrlWaPost = "https://www.washingtonpost.com/"

yahoo = newspaper.build(homeUrlYahoo, language='en', memoize_articles=False)
nyTimes = newspaper.build(homeUrlNYtimes, language='en', memoize_articles=False)
wallSt = newspaper.build(homeUrlWallSt, language='en', memoize_articles=False)
waPost = newspaper.build(homeUrlWaPost, language='en', memoize_articles=False)

news_title = []
news_text = []
news_date =[]

news = yahoo.articles

for i in range(len(news)):
    paper = news[i]
    try:
        paper.download()
        paper.parse()
        news_title.append(paper.title)
        news_text.append(paper.text)
        news_date.append(paper.publish_date)
    except:
        news_title.append('NULL')
        news_text.append('NULL')
        news_date.append('NULL')
        continue

news = nyTimes.articles

for i in range(len(news)):
    paper = news[i]
    try:
        paper.download()
        paper.parse()
        news_title.append(paper.title)
        news_text.append(paper.text)
        news_date.append(paper.publish_date)
    except:
        news_title.append('NULL')
        news_text.append('NULL')
        news_date.append('NULL')
        continue

news = wallSt.articles

for i in range(len(news)):
    paper = news[i]
    try:
        paper.download()
        paper.parse()
        news_title.append(paper.title)
        news_text.append(paper.text)
        news_date.append(paper.publish_date)
    except:
        news_title.append('NULL')
        news_text.append('NULL')
        news_date.append('NULL')
        continue

news = waPost.articles

for i in range(len(news)):
    paper = news[i]
    try:
        paper.download()
        paper.parse()
        news_title.append(paper.title)
        news_text.append(paper.text)
        news_date.append(paper.publish_date)
    except:
        news_title.append('NULL')
        news_text.append('NULL')
        news_date.append('NULL')
        continue

data = pd.DataFrame({'title': news_title, 'text':news_text, 'data':news_date})
data.to_csv('extracted.csv', index=False, sep=',')
