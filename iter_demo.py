class MyIter:
    def __init__(self):
        self.vals = [1, 2, 3]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        val = self.vals[self.index]
        self.index += 1
        return val


def main():
    my_iter = MyIter()
    for n in range(5):
        print(next(my_iter))


if __name__ == "__main__":
    main()

