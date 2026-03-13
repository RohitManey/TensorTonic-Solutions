def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    filteredTokens= []
    #tokensList = tokens.split()
    for word in tokens:
        if word not in stopwords:
            filteredTokens.append(word)
            
    return filteredTokens       
    