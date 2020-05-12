# Create a program to detect if two words rime, by detecting if the last two words are the same.


def it_rime(word_1, word_2):
    if word_1[-2::] == word_2[-2::]:
        print("The words rimes.")
    else:
        print("The words doesn't rime.")


