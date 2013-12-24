class Tree(object):
	''' Doubly-linked tree (not proven to be free of memory issues). '''
	def __init__(self, value):
		self.value = value
		self.max = False
		self.visited = False
		self.parents = []
		self.children = []
		
	@property
	def arguments(self):
		return (self.value, self.max, self.visited,) + tuple(self.children)

	def add_child(self, child):
		#if self.find_child(child) == None:
		self.children.append(child)
		child.parents.append(self)

		#child.add_parent(self)
			
	def add_parent(self, parent):
		#if self.find_parent(parent) == None:
		self.parents.append(parent)
		
	def find_child(self, value):
		for child in self.children:
			if child.value == value:
				return child
		return None

	def find_parent(self, value):
		for parent in self.parents:
			if parent.value == value:
				return parent
		return None

	def find_max_child(self):
		for child in self.children:
			if child.max:
				return child
		return None

	def get_max_path(self):
		path = []
		node = self
		while node != None:
			path.append(node)
			node = node.find_max_child()
		return path
	
	def __eq__(self, trie):
		try:
			return self.arguments == trie.arguments
		except AttributeError:
			return False

	def __repr__(self):
		i = 0
		node = self
		if len(self.parents) > 0:
			node = self.parents[0]
			while not node == None:
				i += 1
				node = node.parents[0:1][0] if len(node.parents)>0 else None

		argumentStr = ', '.join(map(repr, self.arguments))
		return "\n%s%s(%s)" % (' '*i,self.__class__.__name__, argumentStr)


def build_node_tree(number_tree):
	''' Build a tree of nodes based off of the above number values '''
	node_tree = []
	for i in range(len(number_tree)):
		node_tree.append([])
		row = number_tree[i]
		for j in range(len(row)):
			node_tree[i].append(Tree(number_tree[i][j]))
	return node_tree

def build_parent_child(node_tree):
	''' Build the parent-child relationships for the node tree '''
	for i in range(len(node_tree)-1):
		row = node_tree[i]
		next_row = node_tree[i+1]
		for j in range(len(row)):
			node = row[j]
			node.add_child(next_row[j])
			if j+1 < len(next_row):
				node.add_child(next_row[j+1])
				
def get_paths(node, path):
	global paths
	''' Print all paths from root to leaf '''
	if node == None:
		return []
	
	tmp_path = list(path)
	tmp_path.append(node.value);
	if len(node.children) == 0:
		paths.append(tmp_path)
	else:
		for child in node.children:
			get_paths(child, tmp_path)

number_tree = ((75,), # Ew
(95,64),
(17,47,82),
(18,35,87,10),
(20,4,82,47,65),
(19,1,23,75,3,34),
(88,2,77,73,7,63,67),
(99,65,4,28,6,16,70,92),
(41,41,26,56,83,40,80,70,33),
(41,48,72,33,47,32,37,16,94,29),
(53,71,44,65,25,43,91,52,97,51,14),
(70,11,33,28,77,73,17,78,39,68,17,57),
(91,71,52,38,17,14,91,43,58,50,27,29,48),
(63,66,4,68,89,53,67,30,73,16,69,87,40,31),
(4,62,98,27,23,9,70,98,73,93,38,53,60,4,23))

small_number_tree = ((3,),
(7,4),
(2,4,6),
(8,5,9,3))

node_tree = build_node_tree(number_tree)

build_parent_child(node_tree)

paths = []
get_paths(node_tree[0][0],[])

max = 0
for path in paths:
	s = sum(path)
	if s > max:
		max = s
print max

## A much faster way... invert the tree and, as you go up, replace a given node with the
## max of the sum with is and each of it's children. Awesome

# #fill triangle with an array for each row of numbers
# triangle = []
# for line in input_file:
#     split_line =  line.split()
#     a = []
#     for nr in split_line:
#         a.append(int(nr))
#     triangle.append(a)
# 
# #results array, one bigger than biggset of triangle ( for loop uses the last extra zero to count first row of inverted triangle)
# result_array = [0]*(len(triangle[-1])+1) 
# 
# for p_row in triangle[::-1]: # Loop inverted triangle
#     for i, n in enumerate(p_row):
#         # get max of Results_array[i] + Triangle[i] and Results_array[i+1] + Triangle[i]
#         b = result_array[i+1] + n
#         a = result_array[i] + n
#         # update results array
#         result_array[i] = max(a,b)
#     print result_array
# print result_array[0]


