def insert(arr,tmp):
    if len(arr) == 0 or arr[-1] >= tmp:  # just change the sign of < to > it become as desc order
        arr.append(tmp)
        return
    val = arr.pop()
    insert(arr,tmp)
    arr.append(val)
    return

def sort(arr):
    if len(arr) == 1:
        return
    temp = arr.pop()
    sort(arr)
    insert(arr,temp)

arr = [3,4,2,1]
sort(arr)
print(arr)