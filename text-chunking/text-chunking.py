def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    step = chunk_size - overlap
    newTokens = [tokens[i:i+chunk_size] for i in range(0,len(tokens)-overlap,step)]
    return newTokens
    
        