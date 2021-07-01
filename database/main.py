class FakeCursor:
    pass


class FakeConnection:
    def __init__(self, configuration: dict) -> None:
        self.__configuration = configuration

    def cursor(self):
        return FakeCursor()


class UseDatabase:
    def __init__(self, config: dict) -> None:
        self.__configuration = config

    def __enter__(self) -> 'cursor':
        print("Initializing DB connection...")
        self.__connection = FakeConnection(self.__configuration)
        self.__cursor = self.__connection.cursor()
        return self.__cursor

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Python call this method when close resources
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        print("...Close resources")
        print(f"{exc_type=}, {exc_val=}, {exc_tb=}")


def main():
    with UseDatabase({}) as my_cursor:
        print("Execute 'with' body")
        print(f"{my_cursor=}")


if __name__ == '__main__':
    main()
