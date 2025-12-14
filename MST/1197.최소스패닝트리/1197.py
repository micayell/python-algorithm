import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


class DisjointSet:
    def __init__(self, v):
        self.p = [i for i in range(v+1)]

    def find_set(self,x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]
    
    def union(self,x,y):
        px = self.find_set(x)
        py = self.find_set(y)

        if px==py:
            return False
        if px < py:
            self.p[py]=px
        else:
            self.p[px]=py
        return True

def mst_kruskal(v, edges):
    mst_weight=0
    ds = DisjointSet(v)

    edges.sort(key=lambda x: x[2])

    cnt=0
    for edge in edges:
        s,e,w = edge
        if ds.union(s,e):
            mst_weight += w
            cnt+=1

            if cnt == v-1:
                break
    return mst_weight

v,e=map(int,input().split())

edges=[tuple(map(int,input().split())) for _ in range(e)]

res=mst_kruskal(v,edges)
print(res)
