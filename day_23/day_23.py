import aocutils
import matplotlib.pyplot as plt
import networkx as nx

def draw_network(graph):
	# draw network for fun
	_, ax = plt.subplots(figsize=(20, 15))
	nx.draw_networkx(graph, ax=ax, node_color="#ff0000", node_size=100, font_size=7, with_labels=True)
	plt.show()

# was lazy so used networkx :P
@aocutils.timeFunction
def main():
	ref = aocutils.readFile(23, isTest=False, toList=False)
	graph = nx.Graph()

	for line in ref:
		a, b = line.split("-")
		graph.add_edge(a, b)

	total1, total2 = 0, 0
	largest_clique = []
	for component in nx.enumerate_all_cliques(graph):
		if len(component) > len(largest_clique):
			largest_clique = component
		if [i for i in component if i.startswith("t")] and len(component) == 3:
			total1 += 1

	total2 = ",".join(sorted(largest_clique))
	aocutils.printParts(total1, total2)

if __name__ == "__main__":
	main()