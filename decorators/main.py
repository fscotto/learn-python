def my_decorator(f):
    def wrap():
        print('It has a decorator')
        f()

    return wrap


@my_decorator
def my_func():
    print("The function my_func")


def main():
    my_func()


if __name__ == '__main__':
    main()
