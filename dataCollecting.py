import newspaper

cnn_paper = newspaper.build('http://cnn.com')

urlList = []
for article in cnn_paper.articles:
    print(article.url)
    urlList.append(article.url)

for category in cnn_paper.category_urls():
    print(category)

for url in urlList:
    a = newspaper.Article(url, language='en')
    a.download()
    a.parse()
    print(a.title)
    print(a.text[:150])
