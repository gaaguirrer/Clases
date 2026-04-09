class TuringMachine:
    def __init__(self, tape, initial_state, transitions, final_states):
        self.tape = list(tape)
        self.head_position = 0
        self.state = initial_state
        self.transitions = transitions
        self.final_states = final_states
    
    def run(self):
        while self.state not in self.final_states:
            current_symbol = self.tape[self.head_position]
            if (self.state, current_symbol) in self.transitions:
                transition = self.transitions[(self.state, current_symbol)]
                self.tape[self.head_position] = transition[1]
                self.head_position += transition[2]
                self.state = transition[0]
            else:
                raise Exception("No transition found for current state and symbol.")
        
        return ''.join(self.tape)
        

# Defining the transitions for the binary addition machine
transitions = {
    ('q0', '0'): ('q0', '0', 1),
    ('q0', '1'): ('q0', '1', 1),
    ('q0', ' '): ('q1', ' ', -1),
    ('q1', '0'): ('q2', '1', -1),
    ('q1', '1'): ('q1', ' ', -1),
    ('q1', ' '): ('qF', ' ', 0),
    ('q2', '0'): ('q2', '0', -1),
    ('q2', '1'): ('q2', '1', -1),
    ('q2', ' '): ('q3', ' ', 1),
}

# Creating the Turing machine
tape = "101 + 110"
initial_state = 'q0'
final_states = {'qF'}
tm = TuringMachine(tape, initial_state, transitions, final_states)

# Running the Turing machine
result = tm.run()
print("Result:", result)
