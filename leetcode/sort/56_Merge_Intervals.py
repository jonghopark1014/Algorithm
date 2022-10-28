class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merge = [intervals[0]]
        for i in range(1, len(intervals)):  
            if merge[-1][0] <= intervals[i][0] <= merge[-1][1]:  
                if intervals[i][1] >= merge[-1][1]:  
                    merge[-1][1] = intervals[i][1]
            else:  
                merge += [intervals[i]]

        return merge
