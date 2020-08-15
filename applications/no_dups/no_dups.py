def no_dups(s):
    # Your code here

    s_c = ""
    s = s.split()
    for char in s:
        if char not in s_c:
            s_c += char + " "
    s = s_c.strip()

    return s


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
