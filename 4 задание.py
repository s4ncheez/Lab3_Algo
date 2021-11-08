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
