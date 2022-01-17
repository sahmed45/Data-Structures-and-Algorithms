def find(n1):
  res = n1
  
   while res != par[res]:
     par[res] = par[par[res]] # path compression
     res = par[res]
  
  return res

def union(n1, n2):
  p1 = find(n1) # find parent of n1
  p2 = find(n2) # find parent of n2

  if p1 == p2:
    #already unioned cuz they have the same parent
    return

  if rank[p1] > rank[p2]: # meaning p1 component is larger than p2
    rank[p1] += rank[p2] # adding the size of p2 component to p1 size
    par[p2] = p1
  else:
    # else, merge the opposite way
    rank[p2] += rank[p1]
    par[p1] = p2
