import re

line = int(input())
regex = r"![A-Za-z]+!:\[[A-Za-z]+]"
second_regex = r"[[A-Za-z]+]"
third_regex = r"![w[A-Za-z]+!"
my_dict = []
for i in range(line):
    massage = input()
    matches = re.findall(regex, massage)
    my_words = ""
    if len(massage) >= 3:
        if matches:
            for el in matches:
                second_matches = re.findall(second_regex, el)
                for idx in second_matches:
                    my_word = idx[1:-1]
                    for j in my_word:
                        my_dict.append(ord(j))
            for word in matches:
                third_match = re.findall(third_regex, word)
                for h in third_match:
                    my_words = h[1:-1]

            print(f"{my_words}: {' '.join(map(str, my_dict))}")
        if not matches:
            print("The message is invalid")
