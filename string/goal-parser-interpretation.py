class Solution:
    def interpret(self, command: str) -> str:
        # return command.replace('()', 'o').replace('(al)', 'al')

        s = []

        for i in range(len(command)):
            if command[i] == 'G':
                s.append('G')
            elif command[i] == '(':
                if command[i + 1] == ')':
                    s.append('o')
                elif command[i + 1] == 'a':
                    s.append('al')
        return "".join(s)