# cuvant = "a _ _ a _ _ t"
# alfabet
# word = "alfabet"
from random import random

list_of_random_word = ["papagal", "caiet", "calculator"]
word = random.choice(list_of_random_word)
word_list = []
for item in word:
    if item != word[0] and item != word[-1]:
        word_list.append('_')
    else:
        word_list.append(item)
    #print(word[0], word[-1])
# print(word_list)
print(" ".join(word_list))
count_nr = 1
list_already_checked = []
new_word = " ".join(word_list)
while count_nr <= 7:
    user_letter = input("Alege o litera")
    if user_letter == "":
        print("Introdu o litera")
        continue
    if user_letter in word_list:
        print("Litera deja afisata pe ecran")
    elif user_letter in list_already_checked:
        print(list_already_checked)
        print(f"Litera deja a fost incercata, literele deja incercate sunt: {' '.join(list_already_checked)}")
    else:
        elif user_letter in word:
            for iterator, value in enumerate(word):
                if user_letter == value:
                    word_list[iterator] = user_letter
            print(" ".join(word_list))

        else:
            count_nr += 1
        list_already_checked.append((user_letter))
