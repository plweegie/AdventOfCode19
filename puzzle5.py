# Original puzzle:
# https://adventofcode.com/2019/day/5


class OpComputer(object):

    OPCODE_ADD = 1
    OPCODE_MULTIPLY = 2
    OPCODE_INPUT = 3
    OPCODE_OUTPUT = 4
    OPCODE_JUMP_IF_TRUE = 5
    OPCODE_JUMP_IF_FALSE = 6
    OPCODE_LESS_THAN = 7
    OPCODE_EQUALS = 8
    OPCODE_HALT = 99
    
    MODE_POSITION = 11
    MODE_IMMEDIATE = 12

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
            inp = self.tape[self.pointer]
    
            code = inp % 100

            if code == self.OPCODE_HALT:
                yield (code, [])
            
            modes = inp // 100

            mode1 = modes % 10
            mode2 = (modes // 10) % 10
            mode3 = (modes // 1000) % 10

            mode_list = [mode1, mode2, mode3]
            mode_names = list(map(lambda x: self.get_mode_type(x), mode_list))

            yield (code, mode_names)
        

    def get_mode_type(self, mode):
        if mode == 0:
            return self.MODE_POSITION
        else:
            return self.MODE_IMMEDIATE


    def overwrite_tape(self, index, value, step=4):
        self.tape[index] = value
        self.pointer += step
    

    def get_operation_inputs(self, pos_input_1, pos_input_2,  modes):
        input_1 = self.tape[self.tape[pos_input_1]] if modes[0] == self.MODE_POSITION \
            else self.tape[pos_input_1]
        input_2 = self.tape[self.tape[pos_input_2]] if modes[1] == self.MODE_POSITION \
            else self.tape[pos_input_2]

        return (input_1, input_2)


    def operation_add(self, pos_input_1, pos_input_2, pos_output, modes):
        inputs = self.get_operation_inputs(pos_input_1, pos_input_2, modes)
        self.overwrite_tape(self.tape[pos_output], inputs[0] + inputs[1])

    
    def operation_multiply(self, pos_input_1, pos_input_2, pos_output, modes):
        inputs = self.get_operation_inputs(pos_input_1, pos_input_2, modes)
        self.overwrite_tape(self.tape[pos_output], inputs[0] * inputs[1])


    def operation_input(self, pos_output):
        x = input()
        self.overwrite_tape(self.tape[pos_output], int(x), step=2)


    def operation_output(self, pos, modes):
        output = self.tape[self.tape[pos]] if modes[0] == self.MODE_POSITION else self.tape[pos]
        print(output)
        self.pointer += 2


    def operation_jump_if_true(self, pos_input_1, pos_input_2, modes):
        inputs = self.get_operation_inputs(pos_input_1, pos_input_2, modes)
        if inputs[0] == 0:
            self.pointer += 3
        else:
            self.pointer = inputs[1]

        
    def operation_jump_if_false(self, pos_input_1, pos_input_2, modes):
        inputs = self.get_operation_inputs(pos_input_1, pos_input_2, modes)
        if inputs[0] == 0:
            self.pointer = inputs[1]
        else:
            self.pointer += 3


    def operation_less_than(self, pos_input_1, pos_input_2, pos_output, modes):
        inputs = self.get_operation_inputs(pos_input_1, pos_input_2, modes)
        output = 1 if inputs[0] < inputs[1] else 0
        
        self.overwrite_tape(self.tape[pos_output], output)


    def operation_equals(self, pos_input_1, pos_input_2, pos_output, modes):
        inputs = self.get_operation_inputs(pos_input_1, pos_input_2, modes)
        output = 1 if inputs[0] == inputs[1] else 0

        self.overwrite_tape(self.tape[pos_output], output)
            

    def run(self):
        pointer = self.pointer
        while True:
            
            opcode = next(self.opcode())
            if opcode[0] == OpComputer.OPCODE_ADD:
                self.operation_add(pointer+1, pointer+2, pointer+3, opcode[1])
            elif opcode[0] == OpComputer.OPCODE_MULTIPLY:
                self.operation_multiply(pointer+1, pointer+2, pointer+3, opcode[1])
            elif opcode[0] == OpComputer.OPCODE_INPUT:
                self.operation_input(pointer+1)
            elif opcode[0] == OpComputer.OPCODE_OUTPUT:
                self.operation_output(pointer+1, opcode[1])
            elif opcode[0] == OpComputer.OPCODE_JUMP_IF_TRUE:
                self.operation_jump_if_true(pointer+1, pointer+2, opcode[1])
            elif opcode[0] == OpComputer.OPCODE_JUMP_IF_FALSE:
                self.operation_jump_if_false(pointer+1, pointer+2, opcode[1])
            elif opcode[0] == OpComputer.OPCODE_LESS_THAN:
                self.operation_less_than(pointer+1, pointer+2, pointer+3, opcode[1])
            elif opcode[0] == OpComputer.OPCODE_EQUALS:
                self.operation_equals(pointer+1, pointer+2, pointer+3, opcode[1])

            else:
                print(self.tape)
                return

            pointer = self.pointer


    def reset(self):
        self.tape = self.create_tape()
        self.pointer = 0


def main():
    op_computer = OpComputer("puzzle5.txt")
    op_computer.run()


if __name__ == "__main__":
    main() 