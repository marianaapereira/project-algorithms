def is_palindrome_recursive(word, low_index, high_index):
    word_length = len(word)

    if word_length == 0:
        return False

    if low_index >= high_index:
        if low_index == int(word_length / 2):
            return True

        else:
            return False

    else:
        if word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)

        else:
            return False
