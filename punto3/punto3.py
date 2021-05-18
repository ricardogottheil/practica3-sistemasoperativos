from memory_profiler import profile
import numpy as np
 
@profile
def main():
    m = np.random.uniform(1, 100, size=(1000, 1000))

    del m
 
    print('Done!')

if __name__ == '__main__':
    main()