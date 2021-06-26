def main():
    # Dictionary data structure (aka Hashtable, Map, ecc.)
    person = {
        'Name': 'Ford Prefect',
        'Gender': 'Male',
        'Occupation': 'Researcher',
        'Home Planet': 'Betelguese Seven'
    }

    print(f"Initial values:\n{person=}\n")

    # Lookup values by key
    print(f"Fetch name value from dict {person['Name']=}\n")

    # Add new pair key/value
    person['Age'] = 33
    print(f"After add new key Age:\n{person=}\n")

    # Count vowel frequency in a word
    word = "Supercalifragilisticexpialidocious"
    frequency = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for c in word.lower():
        if c in frequency:
            frequency[c] += 1

    print(f"{frequency=}\n")

    for k, v in sorted(frequency.items()):
        print(f"{k} was found {v} time(s)")

    # Set data structure
    print("\nSet data structure")
    vowels = set('aeiou')
    found = vowels.intersection(word)
    for vowel in found:
        print(vowel)


if __name__ == '__main__':
    main()
