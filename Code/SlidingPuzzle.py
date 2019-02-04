# CS-411 AI assignment 1 
# Name : Sarit Adhikari
# Net-Id : sadhik6
# This script consists of all the custom code written for the programming assignment . The code makes calls to function from aima-python codebase.

from search import * # import the search module from aima codebase

class SlidingPuzzle(Problem):
	def __init__(self, initial, goal=None):
		Problem.__init__(self, initial, goal)
	
	#This function returns the possible actions that can be applied to current state  	
	def actions(self, state):
		possible_actions = []
		for i in range(0, len(state)):
			next_index = (i+1) % len(state)
			if (state[i]=='*' or state[next_index]=='*'):
				possible_actions.append(('s',i,next_index)) # action stored as tuple (swap ,element1, element2 ) e.g. ('s',1,2) means swap elements 1 and 2
		
		for i in range(0, len(state)):
			next_index = (i+2) % len(state)
			if (state[i]=='*' or state[next_index]=='*'):
				possible_actions.append(('js',i,next_index)) # action stored as tuple (jumpswap ,element1, element2 ) e.g. ('js',1,3) means swap elements 1 and 3 jumping over element in between
	
		return possible_actions
	
	#This function returns the state after applying action to current state
	def result(self, state, action):
		child_state = list(state[:])
		
		child_state[action[1]],child_state[action[2]] = child_state[action[2]],child_state[action[1]] #swapping the value as indicated in action
		return tuple(child_state)
	
	#This function tests if the goal state has been reached . It checks if same-colored tiles are next to each other
	def goal_test(self, state):		
		for i in range(0, len(state)):
			l = (i-1) % (len(state))  
			r = (i+1) % (len(state))
			if state[l] == state[i] or state[i]==state[r]:
				return False
		return True
	
	#This function returns the path cost based on action . If it is slide 1 is added , if it is jump slide 2 is added
	def path_cost(self, cost_so_far, state1, action, state2):
		return cost_so_far + (2 if action[0]=='js' else 1) # add cost 2 if the action is jump swap and cost 1 otherwise (swap) 
	
	#This function returns the heuristic value for a node 	
	def h(self, node):
		state_dup = list(node.state[:]) #creating duplicate to avoid changing original tuple, converting it to list so that value within list can be changed
		h_val = 0
		for i in range(0, len(state_dup)):
			if(state_dup[i]=='*' or state_dup[i]=='-'):
				continue
		
			l = (i-1) % (len(state_dup))   
			r = (i+1) % (len(state_dup))
			if state_dup[l] == state_dup[i] or state_dup[i]==state_dup[r]:
				h_val = h_val+1
				state_dup[i] = '-' #changing tile to - so for a pair of tile h_val is incremented just once	
		
		return h_val #number of pairs of same-colored tiles together





def main():
	for seed in range(2,5):
		
		print("current seed "+ str(seed))
		
		#Inital state is generated randomly with a fixed seed
		initial_state = generateRandomInitialState(n=3,seed=seed)
		print("initial state")
		print(initial_state)
		sliding_puzzle = SlidingPuzzle(initial_state)
		
		#Create files for writing the results
		fout_astar = open('astar_'+str(seed-1)+'.dat','w')
		fout_breadth = open("breadth_"+str(seed-1)+".dat","w")
		
		for tile in initial_state:
			print(tile.upper())
			fout_astar.write(tile.upper()+" ")
			fout_breadth.write(tile.upper()+" ")
		fout_astar.write("\n")
		fout_breadth.write("\n")
		
		#Astar Search
		print("astar search")
		astar_result = astar_search(sliding_puzzle)
		astar_solution = astar_result.solution()
		astar_path = astar_result.path()
		
		
		print("final result")
		print(astar_result)
		print("cost: "+ str(astar_result.path_cost))
		
		print("solution")
		print(astar_solution)
		
		print("path")
		print(astar_path)
		print("\n")
		
		for step in astar_solution:
			fout_astar.write(str(step[1]) +" "+str(step[2])+" "+str(1 if step[0]=="s" else 2)+"\n")
			
		
		
		#Breadth First Search
		print("uninformed search : breadth first search")
		
		
		breadth_first_result = breadth_first_search(sliding_puzzle)
		breadth_first_solution = breadth_first_result.solution()
		breadth_first_path = breadth_first_result.path()
		
		print("final result")
		print(breadth_first_result) 
		print("cost: "+ str(breadth_first_result.path_cost))
		
		print("solution")
		print(breadth_first_solution)
		
		print("path")
		print(breadth_first_path)
		print("\n")
		
		for step in breadth_first_solution:
			fout_breadth.write(str(step[1]) +" "+str(step[2])+" "+str(1 if step[0]=="s" else 2)+"\n")
		
		fout_astar.close()
		fout_breadth.close()

#This function generates the random state for the puzzle based on seed and n 
def generateRandomInitialState(n,seed):
	random.seed(seed) #seed is set to generate pseudo random number for shuffling the list so that the random experiment can be replicated
	state = [] # this variable will store the state of the puzzle, position in the list denotes the position in the sliding ring
	
	counter = 0
	while(counter< 2*n):
		if (counter < n):
			state.append('g')
		else:
			state.append('r')
		counter = counter+1
	state.append('*')  # since there are always two empty 
	state.append('*')
	random.shuffle(state)
	return tuple(state)	
	
if __name__=="__main__" : main()