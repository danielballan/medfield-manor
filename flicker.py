"""
https://www.dsprelated.com/showarticle/908.php

In [6]: flicker.vis(flicker.gardener_pattern(5), 5)                             
X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X X 
X   X   X   X   X   X   X   X   X   X   X   X   X   X   X   X   X 
X       X       X       X       X       X       X       X       X 
X               X               X               X               X 
X                               X                               X 

In [7]: flicker.vis(flicker.mccartney_pattern(5), 5)                            
X   X   X   X   X   X   X   X   X   X   X   X   X   X   X   X   X 
  X       X       X       X       X       X       X       X       
      X               X               X               X           
              X                               X                   
                              X                                   

In [8]: list(itertools.islice(flicker.flicker(5), 16))
"""
import itertools, math, random

def gardener_pattern(N):
    indexes = list(reversed(range(N)))
    for i in itertools.count():
        update = []
        for j in indexes:
            if i % 2**j == 0:
                update.append(j)
        yield update
                
                
def mccartney_pattern(N):
    indexes = list(reversed(range(N)))
    for i in itertools.count():
        update = []
        for j in indexes:
            if i % 2**(1 + j) == 2**j-1:
                update.append(j)
        yield update
                
                
def vis(pattern, N):
    cols = itertools.islice(pattern, 17 * 2 -1)
    rows = ["" for _ in range(N)]
    for col in cols:
        for i, row in enumerate(rows):
            if i in col:
                rows[i] += "X "
            else:
                rows[i] += "  "
    for row in rows:
        print(row)


def flicker(N):
    terms = [random.random() for _ in range(N)]
    for update in mccartney_pattern(N):
        for index in update:
            terms[index] = random.random()
        yield sum(terms)
            
list(itertools.islice(flicker(5), 16))
