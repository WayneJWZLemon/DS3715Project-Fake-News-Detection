import newspaper
import pandas as pd

homeUrlCnn = "https://www.cnn.com/"
homeUrlFox = "https://www.foxnews.com/"
homeUrlNbc = "https://www.nbcnews.com/"
homeUrlBuzz = "https://www.buzzfeednews.com/"

cnn = newspaper.build(homeUrlCnn, language='en', memoize_articles=False)
fox = newspaper.build(homeUrlFox, language='en', memoize_articles=False)
nbc = newspaper.build(homeUrlNbc, language='en', memoize_articles=False)
buzz = newspaper.build(homeUrlBuzz, language='en', memoize_articles=False)

news_title = []
news_text = []
news_date =[]

news = cnn.articles

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

news = fox.articles

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

news = nbc.articles

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

news = buzz.articles

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

print("length of the title list: ", str(len(news_title)))
print("length of the text list: ", str(len(news_text)))
print("length of the date list: ", str(len(news_date)))

data = pd.DataFrame({'title': news_title, 'text':news_text, 'date':news_date})
data.to_csv('extracted.csv', index=False)
