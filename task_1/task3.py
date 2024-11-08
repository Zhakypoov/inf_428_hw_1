from typing import List


class task3:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        M = {}
        for num in nums1:
            M[num] = 1

        res = []
        for num in nums2:

            if num in M:
                res.append(num)
                del M[num]

        return res