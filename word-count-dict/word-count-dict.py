def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    flattenedList= []
    for subList in sentences:
        flattenedList.extend(subList)
    wordCountDict = { value : flattenedList.count(value)  for value in set(flattenedList)}
    return wordCountDict