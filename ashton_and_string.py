from itertools import izip
from _bisect import bisect_left


def get_suffix_array(s):
    n=len(s)
    suffixes=[]
    for i in xrange(n):
        suffixes.append(buffer(s,i,n-i))
    return sorted(suffixes)

def get_rank_array(s_a):
    rank_arr=[]
    for i,suffix in enumerate(s_a):
        if i==0:
            rank_arr.append(len(s_a[i])-1)
        if i>0:
            prev_suffix=s_a[i-1]
            lcp=get_LCP(prev_suffix,suffix)
            rank_arr.append(rank_arr[-1]+len(suffix[lcp:]))
    return rank_arr

def get_LCP(s1,s2):
    lcp=0
    for x,y in izip(s1,s2):
        if x==y:
            lcp+=1
        else:
            break
    return lcp

def get_substring(k):
    insertion=bisect_left(rank,k)
    if insertion==len(rank):
        return None
    suffix_index=rank[insertion]
    suffix=arr_suffix[insertion]
    if suffix_index==k:
        return suffix
    else:
        return suffix[:k-suffix_index]

n = int(raw_input())
results = []
for _ in xrange(n):
    string=raw_input()
    k=int(raw_input())

    arr_suffix=get_suffix_array(string)
    rank=get_rank_array(arr_suffix)
    n_substrings=rank[-1]+1
    distinct_length=0
    result=None


    for i in xrange(n_substrings):
        s=str(get_substring(i))
        distinct_length+=len(s)

        if distinct_length>=k:
            result=s
            break

    if result!=None:
        res_len=len(result)
        start_substring=distinct_length-res_len+1
        for i in xrange(res_len):
            if k == i+start_substring:
                results.append(result[i])
                break
for r in results:
    print r

