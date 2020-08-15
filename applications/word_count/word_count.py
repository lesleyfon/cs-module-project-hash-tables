import re


def word_count(s):
    # Your code here
    unwanted_char = [":", ";", ",", ".", "-", "+", "=", "/",
                     "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", '"']
    s = s.lower()
    s = s.replace('\\', '')

    for u_char in unwanted_char:
        s = s.replace(u_char, "")

    dictionary = {}
    index = 0
    l = s.split()
    while index < len(l):
        key = l[index]
        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 1
        index += 1
    # print(dictionary)
    return dictionary


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count(
        'Hello, my cat. And my cat doesn\'t say "hello" back. ":;,.-+=/\\|[]{}()*^&'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
