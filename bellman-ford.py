import argparse
import string
## This code implement Bellman-Ford Algorithm

## We use a class called bellmanFord reponsible to apply and verify the 
## relaxation technique and negative-weight cycle,respectively.


class bellmanFord:
    def __init__(self,start,graph):
        self.graph = graph
        self.value = {}
        self.value[start]= 0
        self.start = start
        self.stringGraph = list(string.ascii_uppercase[:len(self.graph)])
        for i in self.stringGraph[1:]:
               self.value[i] = 'inf'
        self.relax()
        self.negativeCycle()


    def relax(self):
        for interaction in xrange(1,len(self.graph)-1):
            for node in self.stringGraph:
                self.path = self.graph[node].keys()
                for k in self.path:
                    if self.value[node] == 'inf':
                        break
                    elif self.value[k] == 'inf':
                        self.value[k] = self.graph[node].get(k) + \
                                        self.value[node]
                    elif ( self.graph[node].get(k) + \
                        self.value[node] < self.value[k] ):
                        self.value[k] = self.graph[node].get(k) + \
                                        self.value[node]
        print self.value

    def negativeCycle(self):                  
        for node in self.stringGraph: 
            self.path = self.graph[node].keys()
            for k in self.path:
                if self.graph[node].get(k) + self.value[node] < self.value[k]:
                    print 'The Graph has a negative-weight cycle'
            


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--node', type=str, required=True, \
                        help='Beginning of the node search')
    args = parser.parse_args()

    bellmanFord(args.node,{ 'A': { 'B': 6 , 'C': 7 }, 
                            'B': { 'C': 8 , 'D': 5 , 'E':-4 }  , 
                            'C': { 'D': -3 , 'E': 9 }  , 
                            'D': { 'B': -2 }, 
                            'E': { 'A': 2  }  
                          }
               )

