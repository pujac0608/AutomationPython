def CalculateSum(arr):
    Calsum = 0
    for i in arr:
        Calsum = Calsum + i

    return Calsum


arr = []
arr = [12, 4, 4, 10, 10]
n = len(arr)
ans = CalculateSum(arr)
result = sum(arr)
print('Sum of the array is ', ans)
print('Sum of the array is ', result)
