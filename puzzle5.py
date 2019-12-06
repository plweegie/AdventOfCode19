# Original puzzle:
# https://adventofcode.com/2019/day/5


class OpComputer(object):

    OPCODE_ADD = 1
    OPCODE_MULTIPLY = 2
    OPCODE_INPUT = 3
    OPCODE_OUTPUT = 4
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
    

    def get_operation_inputs(self, pos_input_1, pos_input_2, pos_output, modes):
        if modes[0] == self.MODE_POSITION:
            input_1 = self.tape[self.tape[pos_input_1]]
        else:
            input_1 = self.tape[pos_input_1]

        if modes[1] == self.MODE_POSITION:
            input_2 = self.tape[self.tape[pos_input_2]]
        else:
            input_2 = self.tape[pos_input_2]

        return (input_1, input_2)


    def operation_add(self, pos_input_1, pos_input_2, pos_output, modes):
        inputs = self.get_operation_inputs(pos_input_1, pos_input_2, pos_output, modes)
        self.overwrite_tape(self.tape[pos_output], inputs[0] + inputs[1])

    
    def operation_multiply(self, pos_input_1, pos_input_2, pos_output, modes):
        inputs = self.get_operation_inputs(pos_input_1, pos_input_2, pos_output, modes)
        self.overwrite_tape(self.tape[pos_output], inputs[0] * inputs[1])


    def operation_input(self, pos_output):
        x = input()
        self.overwrite_tape(self.tape[pos_output], int(x), step=2)


    def operation_output(self, pos, modes):
        if modes[0] == self.MODE_POSITION:
            print(self.tape[self.tape[pos]])
        else:
            print(self.tape[pos])
        self.pointer += 2


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