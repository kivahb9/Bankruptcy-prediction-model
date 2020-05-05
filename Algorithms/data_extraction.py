import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from nltk.stem import PorterStemmer
import nltk
from nltk.corpus import stopwords
import os
def preprocessing(text):
    if len(text)>500:
#        text = text.decode("utf8")
        # tokenize into words
        tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        
        # remove stopwords
        stop = stopwords.words('english')
        tokens = [token for token in tokens if token not in stop]
    
        # remove words less than three letters
        tokens = [word for word in tokens if len(word) >= 3]
    
        # lower capitalization
        tokens = [word.lower() for word in tokens]
    
        # lemmatize
        porter = PorterStemmer()
        tokens = [porter.stem(word) for word in tokens]
        preprocessed_text= ' '.join(tokens)
        return preprocessed_text
def datapreprocess(company_dict):
    result1={}
    c=0
    for url,filing in company_dict.items():
        c+=1
        result1[url]=preprocessing(filing)
        print (c)
    return result1
def dataextraction(dict_companies):
    c=0
    dict_final={}
    for cik,url in dict_companies.items():
        if '.htm' in url:
            str2=''
            resultstring=''
            c+=1
            page = requests.get(url)
        #    time.sleep(5)
            soup = BeautifulSoup(page.text, 'html.parser')
#            [cell.extract() for cell in soup.find_all('t')]
            str1=soup.get_text(strip=True)
            str1=str1.lower()
    #        print (c)
            str1=re.sub('[^A-Za-z]+', ' ', str1)
    #str1=''.join(table_list)
            l1=[m.start() for m in re.finditer("management s discussion and analysis", str1)]
            l2=[m.start() for m in re.finditer('quantitative and qualitative', str1)]
#            l3=[m.start() for m in re.finditer('controls and procedures', str1)]
            print (l1)
            print ("--")
            print (l2)
            if len(l1)>2:
                if len(str(l1[1])) > len(str(l1[0])):
                    str2=str1[l1[1]:]
                    print ("a")
                elif len (str(l1[2])) > len(str(l1[1])):
                    str2=str1[l1[2]:]
                    print ("b")
            elif len(l1)==2:
                if len(str(l1[1])) > len(str(l1[0])):
                    str2=str1[l1[1]:]
                    print ("c")
            elif len(l1)<2:
                if len(l1)==1:
                    str2=str1[l1[0]:]
                    print ("d")
                elif len(l1)==0:
                    str2=''
                    print ("e")
            if str2.find('quantitative and qualitative') == -1:
                resultstring=str2[:str2.find('controls and procedures')]
                print ("a1")
            else:
                resultstring=str2[:str2.find('quantitative and qualitative disclosures about market risk')]
                print ("a2")
            resultstring=resultstring.replace('\xa0', ' ').replace('table of contents', ' ')
            dict_final[url]=resultstring
            print (c)
    return dict_final
def result(df,dict_final):
    list_of_filing=[]
    for i in range(len(df)):
        x1=df.loc[i,'url']
        try:
            list_of_filing.append(dict_final[x1])
        except:
            list_of_filing.append('')
            
    df['filing'] = list_of_filing
    return df

def preparation(filename):
    
    df_companies=pd.read_csv(filename)
    
    col=['cik','filing_type','date','null','url','status']
    df_companies.columns=col
#    (df_companies)
#    df_bad_companies=pd.read_csv('bankruptedFileList.csv')
    list_url_companies = df_companies['url']
#    list_url_bad_companies = df_bad_companies['url']
    
    list_cik = df_companies['cik']
#    list_cik1 = df_bad_companies['cik']
    
    dict_companies=dict(zip(list_cik,list_url_companies))
#    dict_bad_companies=dict(zip(list_cik1,list_url_bad_companies))
    
#    dict_bad1=dataextraction(dict_bad_companies)
    dict_1=dataextraction(dict_companies)
#    df_bad_final=result(df_bad_companies,dict_bad1)
#    df_final=result(df_companies,dict_1)
#    preprocessed_dict_bad=datapreprocess(dict_bad1)
    preprocessed_dict=datapreprocess(dict_1)
    
    df_preprocessed=result(df_companies,preprocessed_dict)
#    df_bad_preprocessed=result(df_bad_companies,preprocessed_dict_bad)
    target=[]
    for i in range(len(df_companies)):
        target.append(0)
        
#    target_bad=[]
#    for i in range(len(df_bad_companies)):
#        target_bad.append(1)
    df_preprocessed['target']=target
#    df_bad_preprocessed['target']=target_bad
    return df_companies

