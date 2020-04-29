# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l, r = 0, mountain_arr.length() - 1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid
        peek = mountain_arr.get(l)
        if peek < target:
            return -1
        elif peek == target:
            return l
        index = self.binary_search(mountain_arr, 0, l, target, asc=True)
        if index != -1:
            return index
        return self.binary_search(mountain_arr, l, mountain_arr.length() - 1, target, asc=False)

    def binary_search(self, mountain_arr: 'MountainArray', l: int, r: int, target: int, asc=True) -> int:
        while l <= r:
            mid = (l + r) // 2
            tmp = mountain_arr.get(mid)
            if tmp == target:
                return mid
            elif tmp < target:
                if asc:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if asc:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
