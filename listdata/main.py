from collections import Counter


def main():
    # Tuple
    vowels = ('a', 'e', 'i', 'o', 'u')

    word = 'Supercalifragilisticexpialidocious'

    # Loop over string
    for letter in word:
        if letter in vowels:
            print(letter)

    # Count vowels in a word
    vowels_in_word = [letter for letter in word.lower() if letter in vowels]
    print(Counter(vowels_in_word), '\n')

    # List share reference between first and second
    first = [1, 2, 3, 4, 5]
    print(f"{first=} (initial)")
    second = first
    print(f"{second=} (initial)")

    second.append(6)
    print(f"{second=} (post append)")
    print(f"{first=} (post append)")

    # If you want create a list's copy you must to use copy method
    print("Third is a copy of second")
    third = second.copy()
    print(f"{third=} (pre append)")

    third.append(7)
    print(f"{third=} (post append)")
    print(f"{second=} (post append)")


if __name__ == '__main__':
    main()
