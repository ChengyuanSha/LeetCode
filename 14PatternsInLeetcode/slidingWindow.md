




## Common problems:

### Maximum sum subarray of size ‘K’ (easy)

```python
def maxSum(arr, n, k):
    i = 0
    j = i + k
    sum_glob = 0
    while j <= n:
        sum_cur = sum([arr[i] for i in range(i, j)])
        sum_glob = max(sum_cur, sum_glob)
        i += 1
        j += 1
    return sum_glob

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))
```




