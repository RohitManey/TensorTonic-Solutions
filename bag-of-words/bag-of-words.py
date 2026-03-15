import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    bagOfWords = {value : tokens.count(value) for value in vocab}
    bagOfWordsArray = np.array(list(bagOfWords.values()),dtype=int)
    return bagOfWordsArray
    
        
        
        
    