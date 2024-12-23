import aocutils
import networkx as nx

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