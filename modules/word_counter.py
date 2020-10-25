import requests 
from bs4 import BeautifulSoup 
import operator 
from collections import Counter 
  
def start(url): 
    # empty list to store the contents of  
    # the website fetched from our web-crawler 
    wordlist = [] 
    source_code = requests.get(url).text 
  
    # BeautifulSoup object to ping the requested url for data 
    soup = BeautifulSoup(source_code, 'html.parser') 
  
    # Get all text found in the body
    for each_text in soup.findAll('body'): 
        content = each_text.text 
  
        # use split() to break the sentence into  
        # words and convert them into lowercase  
        words = content.lower().split() 
        # print(len(words))
        for each_word in words: 
            wordlist.append(each_word) 

        return wordlist
  
# Function removes any unwanted symbols 
def clean_wordlist(wordlist): 
    clean_list =[] 

    # Check for unwanted symbols and remove
    for word in wordlist: 
        symbols = '!@#$%^&*()_-+={[}]|\;:"<>?/., '
          
        for i in range (0, len(symbols)): 
            word = word.replace(symbols[i], '') 
              
        if len(word) > 0: 
            clean_list.append(word) 
        
    # Check for common words and remove
    stopwords = ['and', 'to', 'the', 'you', 'a', 'an', 'of', 'we', 'in', 'our', 'are', 'as', 'with', 'for', 'is', 'her', 'she', 'his', 'your', 'he']
    for word in clean_list:
        if word in stopwords:  
            clean_list.remove(word)
        
    return(clean_list)
    # create_dictionary(clean_list) 
  
# Creates a dictionary conatining each word's  
# count and top_20 ocuuring words 
def create_dictionary(clean_list): 
    word_count = {} 
      
    for word in clean_list: 
        if word in word_count: 
            word_count[word] += 1
        else: 
            word_count[word] = 1
            
    c = Counter(word_count) 
      
    # returns the most occurring elements 
    top = c.most_common(5) 

    return top

# Counts all words in the body of a URL and gets the top 5 uncommon words
def wordCoutingMagic(serpURLs, SERPData): 
    totalWordList = ['Word Count']
    topKeywordsList = ['Top 5 Words']

    for url in serpURLs:
        totalWords = start(url)
        clean_list = clean_wordlist(totalWords)
        topKeywords = create_dictionary(clean_list)
        totalWordList.append(len(totalWords))
        topKeywordsList.append(topKeywords)

    i = 0
    for row in SERPData:
        row.append(totalWordList[i])
        row.append(topKeywordsList[i])
        i+=1

    # Clear the arrays for the next loop
    totalWordList.clear()
    topKeywordsList.clear()
    
    return SERPData