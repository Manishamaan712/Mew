def two_indices(nums, target):
    for i in range(len(nums)):
        for j in range(i+2, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]
            

if __name__ == "__main__":
    nums =[1, 2, 4, 6, 8, 12, 16, 20]
    target = 10
    print(two_indices(nums, target))