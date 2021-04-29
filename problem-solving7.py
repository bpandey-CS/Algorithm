# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.

def average_word_length(sentence: str):
    # remove the punctuation fromt he sentences
    unlikable_chars = ['!','.','?', "'", ",", ";", "."]
    for uc in unlikable_chars:
        sentence.replace(uc,'')
    len_of_words = [len(word) for word in sentence.split()]
    return sum(len_of_words)/len(len_of_words)

if __name__ == "__main__":
    sentence = "This is a test sentence."
    print(average_word_length(sentence))
