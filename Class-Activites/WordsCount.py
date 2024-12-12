def main():
    filename = "gettysburg_address.txt"
    print("This program counts the words in a file")
    
    #get worrds and unique words
    words = get_words_from_file(filename)  #get list of words
    unique_words = get_unique_words(words) #get list of unique words
    
    #disoplay number of works and unique words
    print(f"Number of words = {len(words)}")
    