fin = open('priorityqueue.in')
fout = open('priorityqueue.out', 'w')

def heap(arr, i):
    parent = i
    left_ch = 2 * i + 1
    right_ch = 2 * i + 2
    if left_ch < len(arr) and arr[i][0] > arr[left_ch][0]:
        parent = left_ch
    if right_ch < len(arr) and arr[parent][0] > arr[right_ch][0]:
        parent = right_ch
    if parent != i:
        arr[i], arr[parent] = arr[parent], arr[i]
        heap(arr, parent)

def extract_min(arr):
    if len(arr) == 0:
        return '*'
    mini = arr[0][0]
    arr[0][0] = arr[len(arr) - 1][0]
    arr[0][1] = arr[len(arr) - 1][1]
    arr[len(arr) - 1][0] = 0
    arr[len(arr) - 1][1] = 0
    arr = arr[:len(arr) - 1]
    heap(arr, 0)
    return mini, arr

def push(arr, key, num_of_push):
    arr += [ [-1, -1] ]
    decrease_key(arr, len(arr) - 1, key, num_of_push)

def find_key_to_decrease(arr, i, key):
    for k in range (len(arr)):
        if arr[k][1] == i:
            el_to_decrease = k
            break
    decrease_key(arr, el_to_decrease, key, i)

def decrease_key(arr, i, key, num_of_push):
    arr[i][0] = key
    arr[i][1] = num_of_push
    while (i > 0 and arr[(i - 1) // 2][0] > arr[i][0]):
        arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
        i = (i - 1) // 2

fin = open('priorityqueue.in')
fout = open('priorityqueue.out', 'w')
arr = []
line = fin.readline()
i = 0
