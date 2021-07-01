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


def get_double_gen():
    e = 2
    while e < 300:
        yield e
        e *= 2


def get_double_gen2():
    e = 2
    while True:
        yield e
        e *= 2
        if e >= 300:
            return


def main():
    print("Iterators with class MyIterator")
    for x in MyIterator():
        print(x)

    print("\nIterators with function get_double_gen")
    for x in get_double_gen():
        print(x)


if __name__ == '__main__':
    main()
