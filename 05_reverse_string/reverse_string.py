def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    new_list = list(phrase)
    new_list.reverse()
    new_phrase = "".join(new_list)
    return new_phrase

