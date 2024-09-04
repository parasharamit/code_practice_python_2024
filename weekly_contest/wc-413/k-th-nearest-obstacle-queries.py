from typing import *

def resultsArray(queries: List[List[int]], k: int) -> List[int]:
    
    results = []
    dist_arr = []

    for coord in queries:
        dist_origin = abs(coord[0]) + abs(coord[1]) 

        dist_arr.append(dist_origin)
        dist_arr = sorted(dist_arr)

        if len(dist_arr) >= k:
            results.append(dist_arr[k-1])
        else:
            results.append(-1)

    return results 


def resultsArray2(queries: List[List[int]], k: int) -> List[int]:
    
    results = []
    # kth_dist = -1
    dist_arr = []

    for i in range(len(queries)):
        dist_origin = abs(queries[i][0]) + abs(queries[i][1]) 
        dist_arr.append(dist_origin)

        if i < k-1:
            results.append(-1)
        
        else:
            
            if kth_dist >= dist_origin:
                kth_dist = dist_origin
            
            results.append(kth_dist)

    return results 


if __name__ == "__main__":
    queries = [[]]
    queries = [[1,2],[3,4],[2,3],[-3,0]]
    k = 2

    queries = [[5,5],[4,4],[3,3]]
    k = 1
    print(resultsArray(queries, k))
    print(resultsArray2(queries, k))

