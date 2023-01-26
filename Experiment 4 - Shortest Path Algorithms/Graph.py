#!/usr/bin/python3
from Node import Node
from Link import Link
from APQ_Heap import APQHeap

class Graph:
    #the keys are the nodes and values are the link
    def __init__(self):
        #create an initial empty graph
        self._structure = dict()
    def __str__(self):
        strnodes="\nNodes"
        for v in self._structure:
            strnodes +="\t"+str(v)
        links=self.links()
        strlink="\nLinks:"
        for w in links:
            strlink +=str(w)
        return ("Total Nodes: " +str(self.num_nodes())+"\n"+"Total Links: "+
                               str(self.num_links())+ strnodes+strlink)
    #ADT methods to query the graph

    def num_nodes(self):
        return len(self._structure)

    def num_links(self):
        num = 0
        for v in self._structure:
            num +=len(self._structure[v])
        return num // 2

    def nodes(self):
        return [key for key in self._structure]

    def get_node_by_label(self, element):
        for v in self._structure:
            if v.element()== element:
                #print(v)
                return v
        return None
    def links(self):
        linklist = []
        for v in self._structure:
            for w in self._structure[v]:
                #to avoid duplicates,only return if v in the first nodes
                if self._structure[v][w].start() ==v:
                    linklist.append(self._structure[v][w])
        return linklist
        
    def get_links(self,v):
        #list of all links
        if v in self._structure:
            linklist = []
            for w in self._structure[v]:
                linklist.append(self._structure[v][w])
            return linklist
        return None

    def get_link(self,v,w):
        #link between v and w
        if(self._structure != None and v in self._structure
           and w in self._structure[v]):
            return self._structure[v][w]
        return None

    def degree(self, v):
        #return degree of node v
        return len(self._structure[v])

    def get_weight(self,v,w):
        #Cost between v and w
        if(self._structure !=None and v in self._structure
            and w in self._structure[v]):
            return len(self._structure[v][w])

    def add_node(self,element):
        v=Node(element)
        self._structure[v]=dict()
        return v

    
    def add_node_if_new(self, element):
        for v in self._structure:
            if v.element()== element:
                #print("already there")
                return v
        return self.add_node(element)

    def add_link(self, v, w,element):
        if not v in self._structure or not w in self._structure:
            return None
        e=Link(v,w,element)
        self._structure[v][w]=e
        self._structure[w][v]=e
        return e

    def highestdegreenode(self):
        #return the vertex with highet degree
        hd=-1
        hdv=None
        for v in self._structure:
            if self.degree(v)>hd:
                hd=self.degree(v)
                hdv = v
        return hdv
    
    def linkState(self, src):
        closed = dict()
        locs = dict()
        pred = {src:None}
        apq = APQHeap()#empty apq
        locs[src]=apq.add(0,src)
        while not apq.is_empty():
            key, u = apq.remove_min()
            del locs[u]
            closed[u]=(key,pred[u])
            for e in self.get_links(u):
                v = e.opposite(u)
                if v not in closed:
                    newcost = e.element() + key
                    if v not in locs:
                        pred[v] = u
                        locs[v] = apq.add(newcost,v)
                    elif newcost< apq.get_key(locs[v]):
                        pred[v] = u
                        apq.update_key(locs[v],newcost)
        return closed

    def graphreader(filename):
         
        """ Read and return the route map in filename. """
        graph = Graph()
        file = open(filename, 'r')
        entry = file.readline() #either 'Node' or 'Edge'
        num = 0
        print("**********Welcome to Link State Topology*************")
        while entry == 'Node\n':
            num += 1
            nodeid = int(file.readline().split()[1])
            node = graph.add_node(nodeid)
            entry = file.readline() #either 'Node' or 'Edge'
        print("\tFound", num, 'Nodes and added into the graph')
        num = 0
        while entry == 'Edge\n':
            num += 1
            source = int(file.readline().split()[1])
            sv = graph.get_node_by_label(source)
            target = int(file.readline().split()[1])
            tv = graph.get_node_by_label(target)
            length = float(file.readline().split()[1])
            edge = graph.add_link(sv, tv, length)
            file.readline() #read the one-way data
            entry = file.readline() #either 'Node' or 'Edge'
        print("\tFound", num, 'Links and added into the graph')
        print(graph)
        return graph
