# AI Assignment 1
# Sarit Adhikari
# net-id : sadhik6
# This scipt generates graph as required by part I question 5 . The scipt makes use of functions created in the file SlidingPuzzle.py

from SlidingPuzzle import *
import matplotlib.pyplot as plt


def main():
	MIN_N = 3
	MAX_N = 7
	
	MIN_SEED = 0
	MAX_SEED = 49
		
	
	avg_path_cost_list =[]
	avg_node_expanded_list=[]
	n_list = []
	for n in range(MIN_N,MAX_N+1):
		print ("n=" + str(n))
		path_cost_total = 0
		node_expanded_total = 0
		for seed in range(MIN_SEED,MAX_SEED+1):
			initial_state = generateRandomInitialState(n,seed=seed)
			sliding_puzzle = SlidingPuzzle(initial_state)
			astar_result = astar_search(sliding_puzzle)
			astar_solution = astar_result.solution()
			path_cost_total = path_cost_total + astar_result.path_cost
			print(len(astar_solution))
			node_expanded_total = node_expanded_total + len(astar_solution) 
			
		n_list.append(n)
		avg_path_cost_list.append(path_cost_total/50)
		avg_node_expanded_list.append(node_expanded_total/50)
				
	plt.subplot(211)
	plt.ylabel('average cost')
	plt.xlabel('n')
	plt.plot(n_list,avg_path_cost_list)
	print(avg_path_cost_list)
	
	plt.subplot(212)
	plt.ylabel('average no. of nodes')
	plt.xlabel('n')
	plt.plot(n_list,avg_node_expanded_list)
	print(avg_node_expanded_list)
	
	plt.show()


if __name__=="__main__":main()