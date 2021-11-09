@profile
def range(start, stop, step=1):
    numbers = []
    while start < stop:
        numbers.append(start)
        start += step
    return numbers

@profile
def call():
    for i in range(1,1000000):
        pass

if __name__ == "__main__":
    call()
