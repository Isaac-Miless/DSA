class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get frequencies
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        
        # sort by frequency
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        # get top k
        return [sorted_counts[i][0] for i in range(k)]
