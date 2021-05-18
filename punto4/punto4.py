from memory_profiler import profile
import random


 
@profile
def main():
    arrayNumbers = []

    for i in range(1000):
        n = random.randint(0,100)
        arrayNumbers.append(n)

    del arrayNumbers
 
    print('Done!')


if __name__ == '__main__':
    main()