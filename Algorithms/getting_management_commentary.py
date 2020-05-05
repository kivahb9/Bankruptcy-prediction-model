# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:06:32 2019

@author: bhavik.prajapati
"""


import bs4 as bs
import pandas as pd
import requests
import re
import nltk
from nltk.corpus import stopwords

data=pd.DataFrame()

df_link = pd.read_csv('C:\\Users\\bhavik.prajapati\\Desktop\\Creditpulse_indexing\\main_frame_031019_10_K.csv')
dataset_cik = df_link[["CIK"]]
dataset_typeoffiling = df_link[["Type of filling"]]
dataset_date = df_link[["Date"]]


for i,j in df_link.iterrows():

    a = dataset_cik.loc[i]
    b = dataset_typeoffiling.loc[i]
    c = dataset_date.loc[i]

    def dataextraction(text):
        str2=''
        resultstring=''
        str1=text.lower()

        str1=re.sub('[^a-z.,]+', ' ', str1)

        l1=[m.start() for m in re.finditer("management s discussion and analysis", str1)]
        l11=[m.start() for m in re.finditer("management discussion", str1)]
        l2=[m.start() for m in re.finditer('quantitative and qualitative', str1)]

        print (l1)
        print ("--")
        print (l2)
        if len(l1)>2:
            if len(str(l1[1])) > len(str(l1[0])):
                str2=str1[l1[1]:]

            elif len (str(l1[2])) > len(str(l1[1])):
                str2=str1[l1[2]:]
    #            print ("b")
        elif len(l1)==2:
            if len(str(l1[1])) > len(str(l1[0])):
                str2=str1[l1[1]:]
    #            print ("d")
        elif len(l1)<2:
            if len(l1)==1:
                str2=str1[l1[0]:]
    #            print ("e")
            elif len(l1)==0 or len(l11)!=0:
    #            print (l11)
    #            print ("--")
    #            print (l2)
                if len(l11)>2:
                    if len(str(l11[1])) > len(str(l11[0])):
                        str2=str1[l11[1]:]
    #                    print ("a")
                    elif len (str(l11[2])) > len(str(l11[1])):
                        str2=str1[l11[2]:]
    #                    print ("b")
                elif len(l11)==2:
                    if len(str(l11[1])) > len(str(l11[0])):
                        str2=str1[l11[1]:]
    #                    print ("d")
                elif len(l11)<2:
                    if len(l11)==1:
                        str2=str1[l11[0]:]
    #                    print ("e")
                    if len(l11)==0:
                        str2=str1
        if str2.find('quantitative and qualitative') == -1:
            resultstring=str2[:str2.find('controls and procedures')]
    #        print ("a1")
        else:
            resultstring=str2[:str2.find('quantitative and qualitative')]
    #        print ("a2")
        if len(resultstring) == 0:
            resultstring=str2
        else:
            resultstring=resultstring.replace('\xa0', ' ').replace('table of contents', ' ')
        return resultstring

    def preprocessing(text):
     """
     It takes the string and preprocess the string with the help pf nltk library
     Parameters:
         text(str): string which needs to be prerprocessed
     Return
         preprocessed string with no stopwords
     """
     text=str(text).lower()
     text=re.sub('[^a-z]+', ' ', text)
     tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]

#     remove stopwords
     stop = stopwords.words('english')
     tokens = [token for token in tokens if token not in stop]

#     remove words less than three letters
     tokens = [word for word in tokens if len(word) >= 3]

#     lower capitalization
     tokens = [word.lower() for word in tokens]

#    lemmatize
#    porter = PorterStemmer()
#    tokens = [porter.stem(word) for word in tokens]
     preprocessed_text= ' '.join(tokens)
     return preprocessed_text

    try:
         url = j['Weblink']
         q = url.replace('/ix?doc=', '')
         r = requests.get(q)
         soup = bs.BeautifulSoup(r.content)
         page = soup.get_text()
         page = dataextraction(page)
         page = preprocessing(page)
         save_path = "C:/Users/bhavik.prajapati/Desktop/Creditpulse_indexing/10K_commentary_03102019/"
         file = open(save_path + "{0}_{1}_{2}.txt".format(a.values[0],b.values[0],c.values[0]),"w")
         file.write(page)
         file.close()
         print (url)
    except Exception as e:
        print(e)
# =============================================================================
#         df = pd.DataFrame({'Weblink': [url], 'Text': [page]})
#         data = data.append(df)
#         export_csv = data.to_('C:\\Users\\bhavik.prajapati\\Desktop\\Creditpulse_indexing\\17092019_10_K_commentary.xlsx',
#                                index=None, header=True)
# =============================================================================
