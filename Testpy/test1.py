n = int(input("Enter a number:"))
nums = []
for i in range(n):
    x = int(input("Enter an element:"))
    nums.append(x)

def Cal(nums):
    num_max = nums[0]
    for i in range(len(nums)):
        if nums[i] > num_max:
            num_max = nums[i]
    print("Maximum Value:",num_max)
    print("Maximum Index position: ",nums.index(num_max))

result = Cal(nums)