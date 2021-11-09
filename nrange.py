def nrange(start, stop, step=1):
    while start < stop:
        yield start 
        start += step

@profile
def ncall():
    for i in nrange(1,1000000):
        pass

if __name__ == "__main__":
    ncall()
