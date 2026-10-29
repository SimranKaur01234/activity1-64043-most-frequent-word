def words_starting_with(text, prefix):
    # Split the text into individual words
    words = text.split()

    # Store words that start with the prefix
    result = []

    # Check each word
    for word in words:
        if word.startswith(prefix):
            result.append(word)

    # Return matching words
    return result
