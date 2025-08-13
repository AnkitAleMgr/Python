
def twoSum(nums: list, target: int) -> list:
    hasMap = {} # value, index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in hasMap:
            pass
            return [hasMap[diff], i]
        hasMap[n] = i

            

            

print(twoSum([3,2,4], 6))
            

    



    

