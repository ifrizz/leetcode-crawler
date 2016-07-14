
# coding: utf-8

# # Generate Markdown file
#
# Format
#
#
#     # TITLE
#
#     [TOC]
#
#     ## [001. QUESTION NAME](QUESTION URL)
#
#     > QUESTION DESCRIPTION LINE 1
#     > QUESTION DESCRIPTION LINE 2
#
#
#     ```
#     @NAME: WRITE YOUR CODE HERE. (RANDOM)
#     ```
#
#

# In[1]:

FILE_NAME = "呆毛算法小分队 Week 6"
#QUESTION_LIST = [152, 017, 125, 179, 110, 118, 069, 079, 137, 029, 242, 012]
QUESTION_LIST = ["152", "017", "125", "179", "110", "118", "069", "079", "137", "029", "242", "012"]
TEAM_MEMBER = ["Weichen", "Cecilia", "WenXin", "Xinyi", "Chris", "Laijie"]

import lcCrawler
import pickle, random
import time

class writeMD():
    def __init__(self):
        self.problemLink = pickle.load(open("utils/problemLink.pk", "r"))
        self.name = TEAM_MEMBER
        random.shuffle(self.name)
        self.getNameCount = 0
        self.getContentList()

    def getProblem(self, num):
        url, isPremium = self.problemLink[num]
        c = lcCrawler.lcCrawler(url)
        return (url, c.getName(), c.getQuestionLines(), isPremium)

    def getName(self):
        index = self.getNameCount % len(self.name)
        self.getNameCount += 1
        return self.name[index]

    def getContentList(self):
        self.contentList = [0] * len(QUESTION_LIST)
        for i, q in enumerate(QUESTION_LIST):
            try:
                self.contentList[i] = self.getProblem(int(q))
                #url, name, lines, isPremium = self.getProblem(int(q))
            except:
                self.contentList[i] = ("ERROR", q + "-ERROR", "[]", + False)

    def write(self):

        f = open(FILE_NAME + ".md", 'w')
        f.write("# " + FILE_NAME + "\n\n")

        #write TOC
        f.write("* ["+FILE_NAME+"]("+"-".join(FILE_NAME.split())+")\n")
        for i, q in enumerate(QUESTION_LIST):
            url, name, lines, isPremium = self.contentList[i]
            hashLink = [q] + name.lower().split()
            hashLink = "-".join(hashLink)
            f.write("\t* ["+q+". "+name+"](#"+hashLink+")\n")

        f.write("\n\n")
        for i, q in enumerate(QUESTION_LIST):
            url, name, lines, isPremium = self.contentList[i]
            if isPremium:
                f.write("!!! THIS IS A PREMIUM QUESTION !!! \n\n")
                continue
            f.write("## "+ "[" + q + ". " + name + "](" + "https://leetcode.com" + url + ")\n\n")
            for line in lines:
                f.write(">" + line.strip() + "\n")
            f.write("\n@" + self.getName())
            f.write("\n\n\n\n```\n\n\n" + "```\n\n")
        f.close()


# In[2]:

def main():
    w = writeMD()
    w.write()


# In[ ]:

if __name__ == "__main__":
    main()


# In[ ]:
