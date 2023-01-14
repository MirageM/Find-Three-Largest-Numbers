#Find Three Largest Numbers
#Time Complexity: O(n) || Space Complexity: O(1)
def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        findThreeLargest(threeLargest, num)
    return threeLargest
def findThreeLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)
def shiftAndUpdate(threeLargest, num, idx):
    for i in range (idx + 1):
        if i == idx:
            threeLargest[i] = num
        else:
            threeLargest[i] = threeLargest[i + 1]