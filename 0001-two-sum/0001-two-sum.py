class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map= dict() #key:value 

        for i,num in enumerate(nums): #{index:number}
            diff = target - num
            if diff in map:
                return [map[diff], i]
            else:
                map[num] = i    

         

 



            
     


        