# Your code here
def print_text(path):

    histo_txt = ""
    histogram = {}
    unwanted_char = ['"', ':', ';', ',', '.', ' ,' '-', '+', '=',
                     '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', ]
    for word in open(path,  "r"):
        word = word.replace("#", "")
        word = word.replace('"', "")
        word = word.replace(":", "")
        word = word.replace(";", "")
        word = word.replace(",", "")
        word = word.replace(".", "")
        word = word.replace("|", "")
        word = word.replace("-", "")
        word = word.replace("[", "")
        word = word.replace("]", "")
        word = word.replace("{", "")
        word = word.replace("}", "")
        word = word.replace("+", "")
        word = word.replace("=", "")
        word = word.replace("*", "")
        word = word.replace("^", "")
        word = word.replace("&", "")
        word = word.replace("/", "")
        word = word.replace('\\', '')
        word = word.replace('', '')
        word = word.lower()
        histo_txt += word

    histo_txt_split_text = histo_txt.split()

    for word in histo_txt_split_text:
        if word not in histogram:
            histogram[word] = 1
        else:
            histogram[word] += 1

    histogram = sorted(histogram.items(), key=lambda x: x[1], reverse=True)

    for key, value in histogram:
        print(f'{key}, {value * "#"}')


print_text("/Users/lesley/code/Python/Projects/cs-module-project-hash-tables/applications/histo/robin.txt")
