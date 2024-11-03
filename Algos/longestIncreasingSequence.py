def longest_increasing_subsequence_at_index(nums, index):
    if not nums or index < 0 or index >= len(nums):
        return 0

    dp = [1] * len(nums)

    for i in range(1, index + 1):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp[:index+1])

# Example usage
nums = [5, 2, 8, 6, 3, 6, 9, 5]
index = 5
print(longest_increasing_subsequence_at_index(nums, index))
