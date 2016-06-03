
# coding: utf-8

# In[21]:

import requests
from bs4 import BeautifulSoup

import html2text


class lcCrawler:
    def __init__(self, url):
        baseUrl = "https://leetcode.com"
        self.url = baseUrl + url
        self.getSoup();

    def getSoup(self):
        response = requests.get(self.url)
        self.soup = BeautifulSoup(response.text, "lxml")

    def getQuestionLines(self):
        question_div = self.soup.find("div", class_="question-content")
        questionsLines = filter(lambda x: x != u"\n", question_div.contents)
        mdLines = []
        for line in questionsLines[:-3]:
            mdLines.append(html2text.html2text(str(line)).strip())
        return mdLines

    def getName(self):
        h3 = self.soup.find("h3").text
        return h3[h3.find(" ")+1:]
