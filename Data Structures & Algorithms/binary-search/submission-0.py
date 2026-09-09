class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # nums = [-1,0,3,5,9,12] sorted, target = 9
        #         i=0       j=5, 0+5//2 = 2, nums[2]=3<9, i->2
        #         i=2       j=5, 2+5//2 = 3, nums[3]=5<9, i->3
        #         i=3       j=5, 3+5//2 = 4, nums[4]=9<9, i->4, return 4

        # nums = [-1,0,3,5,9,12] sorted, target = 2
        #         i=0       j=5, 0+5//2 = 2, nums[2]=3>2, j->2
        #         i=0       j=2, 0+2//2 = 1, nums[1]=0<2, j->1
        #         i=0       j=1, 0+1//2 = 0, nums[0]=-1<2, j->0, return -1

        i, j=0, len(nums)-1

        while i <= j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        
        return -1