import collections
import pandas as pd
from wordcloud import WordCloud, STOPWORDS

def isWordPresent(sentence, word):
     
    # To break the sentence in words
    s = sentence.split(" ")
 
    for i in s:
 
        # Comparing the current word
        # with the word to be searched
        if (i == word):
            return True
    return False

data = pd.ExcelFile("C:\\Users\\Swopil\\Desktop\\ViewFinders\\youtube_extract\\youtube_extract_Finance_Factory.xlsx")
analytics = pd.read_excel(data,'Sheet1')
all_headlines=""
headlines = []
common_tags = ['#doers','the doers','the doers nepal','#doersnepal','doers nepal','doers','nepal','thedoers']
for i in analytics['tags']:
    i = i.replace("'","")
    i = i.replace("[","")
    i = i.replace(" [","")
    
    i = i.replace("] ","")
    i = i.replace("]","")
    i = i.replace(" ","")
    
    i = i.replace("', '","',")
    i = i.replace(","," ")

    
    headlines.append(i)


for i in headlines:
    all_headlines = all_headlines + " " + i




stopwords = STOPWORDS
filtered_words = [word for word in all_headlines.split(" ") if word not in stopwords]
counted_words = collections.Counter(filtered_words)
repeat_words = []
repeat_counts = []
for letter, count in counted_words.most_common(14):

    repeat_words.append(letter)

    repeat_counts.append(count)
    
#print(repeat_words)
#print(repeat_counts)
stopwords = repeat_words 
tag = []
counter = []
for i in analytics['tags']:
    i = i.replace("'","")
    i = i.replace("[","")
    i = i.replace(" [","")
    
    i = i.replace("] ","")
    i = i.replace("]","")
    
    i = i.replace("', '","',")
    i = i.replace(", ","")
    #print(i)


    filtered_words = [word for word in i.split(" ") if word not in stopwords]
    counted_words = collections.Counter(filtered_words) 
    letters = 
    for letter,count in counted_words.most_common(3):
        
    tag.append(letter)
    counter.append(count)
print(tag)

