def find_k_largest(arr, k):
    if k > len(arr) or k <= 0:
        raise ValueError("k має бути в межах розміру масиву")
    
    indexed_arr = [(arr[i], i) for i in range(len(arr))]  
    
    for i in range(len(indexed_arr)):
        for j in range(i + 1, len(indexed_arr)):
            if indexed_arr[i][0] < indexed_arr[j][0]:
                indexed_arr[i], indexed_arr[j] = indexed_arr[j], indexed_arr[i]
    
    k_largest_value = indexed_arr[k - 1] 
    return k_largest_value

arr = [15, 7, 22, 9, 36, 2, 42, 18]
k = 3
    
try:
    result = find_k_largest(arr, k)
    print(f"Знайдений {k}-й найбільший елемент: {result[0]}")
    print(f"Позиція {k}-го найбільшого елемента в масиві: {result[1]}")
except ValueError as e:
    print(e)

