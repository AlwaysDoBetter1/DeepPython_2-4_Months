'''
getrefcount example
'''

import sys

nums1 = [1, 2, 3]
nums2 = [nums1]
nums3 = nums2 * 10

print(sys.getrefcount(nums1))

# output:
# 13

