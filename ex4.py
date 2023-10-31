def encryptThis(message):
    words = message.split()
    encrypted_words = []

    for word in words:
        if len(word) == 0:
            continue
        elif len(word) == 1:
            encrypted_words.append(str(ord(word[0])))
        else:
            encrypted_word = str(ord(word[0])) + word[-1] + word[2:-1] + word[1]
            encrypted_words.append(encrypted_word)

    return ' '.join(encrypted_words)