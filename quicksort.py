def quicksort(array, lo, hi):
    #print("start quicksort")
    #print(array)
    if lo >= hi or lo < 0:
        return
    p = partition(array,lo,hi)
    quicksort(array,lo,p-1)
    quicksort(array,p+1,hi)
    #print("end quicksort")

def partition(array,lo,hi):
    pivot = array[hi]
    print("pivot:",pivot)
    i = lo-1
    print(array)
    for j in range(lo,hi):
        if array[j] <= pivot:
            i=i+1
            tmp = array[j]
            array[j]=array[i]
            array[i]=tmp
    i=i+1
    tmp=array[hi]
    array[hi]=array[i]
    array[i]=tmp
    print("array[i]",array[i])
    print(array)
    return i


if __name__ == "__main__":
    print("start")
    array = [1,3,7,4,9,8,4,2,6]
    print(array)
    array_sorted = quicksort(array,0,len(array)-1)
    print(array)
    print("end")
