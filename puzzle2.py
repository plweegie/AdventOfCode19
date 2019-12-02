class OpComputer(object):

    OPCODE_ADD = 1
    OPCODE_MULTIPLY = 2

    def __init__(self, file_path):
        self.file_path = file_path
        self.tape = self.create_tape()
        self.pointer = 0


    def create_tape(self):
        with open(self.file_path, "r") as file:
            text = file.read()
            return [ int(x) for x in text.split(',') ]


    def update_inputs(self, noun, verb):
        self.tape[1] = noun
        self.tape[2] = verb

    
    def opcode(self):
        while True:
            yield self.tape[self.pointer]
        

    def overwrite_tape(self, index, value):
        self.tape[index] = value
        self.pointer += 4
    

    def operation_add(self, pos_input_1, pos_input_2, pos_output):
        input_1 = self.tape[self.tape[pos_input_1]]
        input_2 = self.tape[self.tape[pos_input_2]]
        self.overwrite_tape(self.tape[pos_output], input_1 + input_2)

    
    def operation_multiply(self, pos_input_1, pos_input_2, pos_output):
        input_1 = self.tape[self.tape[pos_input_1]]
        input_2 = self.tape[self.tape[pos_input_2]]
        self.overwrite_tape(self.tape[pos_output], input_1 * input_2)


    def run(self):
        pointer = self.pointer
        while True:
            opcode = next(self.opcode())
            if (opcode == OpComputer.OPCODE_ADD):
                self.operation_add(pointer+1, pointer+2, pointer+3)
            elif (opcode == OpComputer.OPCODE_MULTIPLY):
                self.operation_multiply(pointer+1, pointer+2, pointer+3)
            else:
                print(self.tape)
                return

            pointer = self.pointer


    def reset(self):
        self.tape = self.create_tape()
        self.pointer = 0


def main():
    output = 19690720
    op_computer = OpComputer("puzzle2.txt")
    
    for i in range(100):
        for j in range(100):
            op_computer.update_inputs(i, j)
            op_computer.run()

            if (op_computer.tape[0] == output):
                print((100 * i) + j)
                return
            else:
                op_computer.reset()


if __name__ == "__main__":
    main() 
        
