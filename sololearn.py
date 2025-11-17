def vowel_counter():
    string = input("introduce a sentence\n")
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    print(count)

vowel_counter()
print('ee')
