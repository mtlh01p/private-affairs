## THIS FUNCTION IS GIVEN TO STUDENT
"""
a function to convert a rule number (int) to its binary representation (str)

Parameters: 
rule_number (int): a range of numbers 0-255

Returns: 
string of binary representation
"""
def rule_to_binary(rule_number):
    return f"{rule_number:08b}"

"""
a function to get the neighborhood of a cell.

Parameters: 
state (str) - current state in binary format
index (int) : the index to yield its neighbour

Returns: 
string of 3 binary representation
"""
def get_neighborhood(state, index):
    pass

"""
a function to compute the next state of the automaton based on the current state and the rule.

Parameter: 
state (str) : current state in binary format
rule_binary (int) : the index to yield its neighbour

Returns: 
new binary representation (next generation)
"""
def next_state(current_state, rule_binary):
    pass

"""
Simulates a one-dimensional cellular automaton.

Parameters:
initial_state (list of str): The initial state of the automaton, represented as a list of characters (e.g., '0' and '1').
rule_number (int): The rule number (0-255) defining the automaton's behavior, which is converted to binary.
generations (int): The number of generations to simulate.

Returns:
None: The function prints each generation's state to the console.
"""
def simulate_automaton(initial_state, rule_number, generations):
    pass

## main function to take user input and run the simulation
def main():
    rule_number = int(input("Enter the rule number (0-255): "))
    initial_state = list(input("Enter the initial state (e.g., 0001000): "))
    generations = int(input("Enter the number of generations: "))
    simulate_automaton(initial_state, rule_number, generations)
    print(rule_to_binary(rule_number))

main()