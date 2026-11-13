class Solution(object):
    def thirdMax(self, nums):
        largest = []
        i = 0
        while i < len(nums):
            if nums[i] not in largest:
                if len(largest) == 0:
                    largest.append(nums[i])
                elif len(largest) == 1:
                    if nums[i] < largest[0]:
                        largest.insert(0, nums[i])
                    else:
                        largest.append(nums[i])
                elif len(largest) == 2:
                    if nums[i] < largest[0]:
                        largest.insert(0, nums[i])
                    elif nums[i] < largest[1]:
                        largest.insert(1, nums[i])
                    else:
                        largest.append(nums[i])
                else:
                    if nums[i] > largest[0]:
                        largest.pop(0)
                        if nums[i] < largest[0]:
                            largest.insert(0, nums[i])
                        elif nums[i] < largest[1]:
                            largest.insert(1, nums[i])
                        else:
                            largest.append(nums[i])
            i += 1

        if len(largest) == 3:
            return largest[0]
        else:
            return max(largest)