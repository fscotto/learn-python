def main():
    phrase = "Don't panic"
    plist = list(phrase)
    print(phrase)
    print(plist)

    # I insert here my code
    new_phrase = ''.join(plist[1:3])
    new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]])

    print(plist)
    print(new_phrase)


if __name__ == '__main__':
    main()
