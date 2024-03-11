def string_sorting(string, length):
    string_lowercase = string.lower()
    str_list = list(string_lowercase)

    if length > 1:
        for i in range(length):
            index = i

            for j in range((i + 1), length):
                if str_list[j] < str_list[index]:
                    index = j

            str_list[i], str_list[index] = str_list[index], str_list[i]

        return ''.join(str_list)

    else:
        return string_lowercase


def is_anagram(first_string, second_string):
    first_string_length = len(first_string)
    second_string_length = len(second_string)

    ordered_first_string = string_sorting(first_string, first_string_length)
    ordered_second_string = string_sorting(second_string, second_string_length)

    if (first_string_length > 0) and (second_string_length > 0):
        if ordered_first_string == ordered_second_string:
            isEqual = True

        else:
            isEqual = False

    else:
        isEqual = False

    response = (ordered_first_string, ordered_second_string, isEqual)

    return response
