import sys


def insertionSort(list):
    """
    input: Integers seperated by spaces
    output: sorted list
    created by : Amit Kumar
    """
    for i in range(len(list)-1):
        n = i
        while n > -1 and list[n] > list[n+1]:
            list[n] , list[n+1] = list[n+1] , list[n]
            n -= 1
    return list

def main():
    data = [int(i) for i in sys.stdin.readline().rstrip().split(' ')]
    sys.stdout.write(str(insertionSort(data)));


if __name__ == '__main__':
    main()
