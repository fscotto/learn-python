class MyIterator:
    def __iter__(self):
        self.__myattr = 2
        return self

    def __next__(self):
        if self.__myattr < 300:
            n = self.__myattr
            self.__myattr *= 2
            return n
        else:
            raise StopIteration


def main():
    for x in MyIterator():
        print(x)


if __name__ == '__main__':
    main()
