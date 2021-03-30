# DS3715Project-Fake-News-Detection
Using real/fake news datasets to train a machine learning model that is going to detect whether the input news data is fake or not.
# Detecting Fake News
## By Wayne Zheng & Benson Li
### Introduction
The proposal for our project is to create an algorithm that can detect fake news in order to traverse an increasingly diverse media landscape where information can be spread at the blink of an eye to massive audiences. Our motivation for choosing this project is because of the proliferation of blatantly false news being spread around the internet regardless of whether that source had a bias towards Democrats or Republicans. A recent example of this took place on Twitter when verified accounts reported that the shooter at a Colorado supermarket was a white man, when in reality the shooter was a man of Syrian descent. Another example of widespread fake news took place after the 2020 presidential election, in which many prominent figures echoed claims of the election being stolen due to rigged voting machines or because of votes of dead people being counted. Our proposed project would work to fight against the proliferation of claims like this that can cause concrete harm to today’s society. For more help with creating our model, we will look at an academic article written by researchers Gerardo Ernesto Rolong Agudelo, Octavio José Salcedo Parra, and Julio Barón Velandia about creating a machine learning model in Python to detect fake news. Their paper outlined using various tools and methods that will also be used to help create our fake news detection algorithm such as the TfidfVectorizer and the Naive Bayes model. For more guidance on how to build a web-based machine learning algorithm, we will also be looking at a textbook written by Anubhav Singh, a web developer, and Sayak Paul, who is affiliated with PyImageSearch.

### Proposed Work
For our project, we would work with various machine learning models and other data science concepts, some of which have already been covered in class and in the lab.
To begin this project, we are aiming to use a mixture of datasets from sources including Kaggle and GitHub. To avoid overfitting and in order to get better generalized results, we are planning to use Python modules such as the Scrapy and the Newspaper3k to extract data from recent news articles online. As the technology evolves, so as the fake news generators, our data collecting approach ensures that the machine learning model we are trying to build can detect fake information at the present and from the past.
Next, we will need to preprocess all the text data we gather, one important method we are going to use is the TfidfVectorizer which can help measure the Term Frequency-Inverse Document Frequency (TF-IDF) statistic that indicates how important a word is to the document and the whole corpus that are being examined. This is an essential component to our machine learning model as it converts plain text documents to useful features with numerical measures that can be analyzed.
Then to build the machine learning model, we are going to make use of the Passive Aggressive algorithm since it is a flexible method that will remain passive when the classification outcomes are accurate, and turns aggressive when miscalculations happen by updating the model and adjusting to the change in the data. Since there are new articles being posted daily, we want to make sure our model can correctly make the prediction, thus Passive Aggressive algorithm is extremely suitable in this case. Furthermore, we are planning to use other classification methods such as decision tree classifier and random forest classifier to evaluate the data, by having more algorithms we can compare the result and make improvements to come up with the most desirable solution. To examine the performance of our model, we are going to use statistical measurements such as the confusion matrix, the recall, and the precision.

### Timeline
* First Week (3-29-2021 to 4-4-2021)
1. Set up the cooperative coding environment using git and GitHub
2. 2 Collect enough data from the web using Scrapy and Newspaper3k
3. Combine different datasets together
4. Finish data preprocessing
5. Write up the first progress report
* Second Week (4-5-2021 to 4-11-2021)
1. Train the data with different classification algorithms
2. Validate the results and make changes to the model as necessary
3. Test the model with the test set and potentially apply the model to a completely different dataset for further testing
4. Write up the second progress report
* Third Week (4-12-2021 to 4-18-2021)
1. Start building the front end for other users
2. Start deploying the project
3. Prepare the materials for in-class presentation/lighting talk
* Four Week (4-19-2021 to 4-25-2021)
1. Wrap up the project
2. Write up the final report

![DS Project Flow Chart](https://user-images.githubusercontent.com/60633000/113054079-ff47dc00-9176-11eb-83e1-05d4a2bc0e05.png)

References
- Agudelo G.E.R., Parra O.J.S., Velandia J.B. (2018) Raising a Model for Fake News Detection		Using Machine Learning in Python. In: Al-Sharhan S. et al. (eds) Challenges and			Opportunities in the Digital Era. I3E 2018. Lecture Notes in Computer Science, vol		11195. Springer, Cham.https://doi-org.libproxy.temple.edu/10.1007/978-3-030-02131 -3_52
- Zoleikha Jahanbakhsh-Nagadeh, Mohammad-Reza Feizi-Derakhshi, Arash Sharifi, A			semi-supervised model for Persian rumor verification based on content information,		Multimedia Tools and Applications, 10.1007/s11042-020-10077-3, (2020).
- Hands-On Python Deep Learning for Web by Anubhav Singh and Sayak					Paul https://github.com/PacktPublishing/Hands-On-Python-Deep-Learning-for-Web
