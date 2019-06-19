
file = open("input2.txt","r")
matrix = []
# lst = file.readlines()
for line in file:
    matrix.append(line.split())

def find_all_cycles(graph, vertex,order=[],longest=0,all=[]):
    '''Parent is the node we just came from'''
    if order:
        parent = order[-1]
    else:
        parent = -1
    
    longest_cycle = longest
    order.append(vertex)
    #current noe in the graph
    current_node=graph[vertex]
    for i in range(0,len(current_node)):
        '''
        makes sure the current neoghbor is not the parent we just came from 
        make sure current node has a connection or current_node == '1'
        '''
        if parent != i and current_node[i] == '1':
            # if i is in the path then there is a cycle
            if i in order:
                # find frst isntance if i in the path and that will be the start cyle 
                index= order.index(i)
                # i had to put it in a set so i can avoid appneding duplicate cycles
                cycle= set(order[index:])
                if cycle not in all :
                    all.append(cycle)
                    if len(cycle) > longest_cycle:
                        longest_cycle = len(cycle)
            else:   
                # recursivley calls the methods and returns cyles
                all = find_all_cycles(graph, i,order,longest_cycle,all)
    order.pop()
    return all

def bfs(graph,queue,visited=[]):
    if(not queue):
        return -1
    current_level = queue
    visited.extend(queue)
    #we clear the qeueu because that were were store all the nodes in the next level
    queue = []
    for vertex in current_level:
        current_node= graph[vertex]
        for i in range(len(current_node)):
            #current node has a connection with i
            # i has not been visted
            # i is not in the qeueu/ prevents duplicstes
            #
            #
            #

            if current_node[i] == '1' and i not in visited:# and i not in current_node:
                queue.append(i)
    return 1 + bfs(graph,queue,visited)

all_cycles = find_all_cycles(matrix,0)
longest_cycle = len(max(all_cycles,key=len,default=[])) #finds the cycle with largest length


print(f'Number of cycles: {len(all_cycles)}')

print(f'Longest Cycle: {longest_cycle} nodes')

print(f'Number of layers in the graph: {bfs(matrix,[0])}')