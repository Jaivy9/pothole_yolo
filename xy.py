def target_sum(nums, target):
    i=0
    j=len(nums)-1
    output_lst = []
    while i<j:
        if nums[i]+nums[j]>target:
            j-=1
        elif nums[i]+nums[j]==target:
            output_lst.append([i,j])
            i+=1
        elif nums[i]+nums[j]<target:
            i+=1
    return output_lst



nums = [2,7,11,15]
target = 100
print(target_sum(sorted(nums),target))

def mini_sum(grid,i,j):
    if i==len()

grid = [[1,3,1],[1,5,1],[4,2,1]]
