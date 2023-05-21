text = input()
text_list = []
vowels = ['a', 'o', 'u', 'e', 'i']

for i in text:
    text_list.append(i)
    for ch in text_list:
        if ch in vowels:
            text_list.remove(ch)

print(''.join(text_list))
