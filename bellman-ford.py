import argparse
import numpy

## This code implement Bellman-Ford Algorithm

## We use a class called bellmanFord reponsible to apply and verify the relaxation
##technique and negative-weight cycle,respectively.


class bellmanFord:
    def __init__(self,start):
        self.graph = { 'A': { 'B': 6 , 'C': 7 }, 
                       'B': { 'C': 8 , 'D': 5 , 'E':-4 }  , 
                       'C': { 'D': -3 , 'E': 9 }  , 
                       'D': { 'B': -2 }, 
                       'E': { 'A': 2  }  
                     }
        self.value = {}
        self.value[start]= 0
        for i in ['B','C','D','E']:
               self.value[i] = 'inf'
    

    def relax(self,graph,start,value):
        for interaction in xrange(1,len(graph)-1):
            for node in ['A','B','C','D','E']:
              self.path = graph[node].keys()
              for k in self.path:
                  if value[node] == 'inf':
                    break
                  elif value[k] == 'inf':
                    value[k] = graph[node].get(k) + value[node]
                  elif graph[node].get(k) + value[node] < value[k]:
                    value[k] = graph[node].get(k) + value[node]


    def negativeCycle(self,graph,value):                  
        for node in ['A','B','C','D','E']: 
          self.path = graph[node].keys()
          for k in self.path:
            if graph[node].get(k) + value[node] < value[k]:
               print 'The Graph has a negative-weight cycle'
            


if __name__ == '__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument('-n', '--node', type=str, required=True,
                        help='Beginning of the node search')
  args = parser.parse_args()

  a = bellmanFord(args.node)
  a.relax(a.graph,args.node,a.value)
  a.negativeCycle(a.graph,a.value)

  print a.value