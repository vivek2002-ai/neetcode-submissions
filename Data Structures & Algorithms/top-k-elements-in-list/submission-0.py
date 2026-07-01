class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()
        for num in nums:
            freq = freq_dict.get(num,0)
            freq += 1
            freq_dict[num] = freq

        freq_list = [(value,key) for key,value in freq_dict.items()]
        freq_list = sorted(freq_list, key = lambda x: x[0])
        result = [x[1] for x in freq_list[len(freq_list)-k:]]
        return result

               