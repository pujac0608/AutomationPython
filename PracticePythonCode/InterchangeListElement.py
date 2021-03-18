# interchange first and last elements in a list
def swapList(List):
    size = len(List)
    temp = List[0]
    List[0] = List[size - 1]
    List[size - 1] = temp
    return List


newList = [12, 35, 9, 56, 24, 9]
print(swapList(newList))
