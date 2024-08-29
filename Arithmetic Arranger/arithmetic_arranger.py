def arithmetic_arranger(problems, show_answers=False):
    arranged_problems = ''

    while True:
        # More than 5 problem handler
        if len(problems) > 5:
            response = "Error: Too many problems."
            break

        # Get operators and excluded operator handler
        operators = list(map(lambda operator: operator.split()[1], problems))
        if '*' in operators or '/' in operators:
            response = "Error: Operator must be '+' or '-'."
            break

        # Get operands
        operands = [] 
        for problem in problems:
            p = problem.split()
            operands.extend([p[0], p[2]])

        # Operand digit validation handler
        if not all(map(lambda operand: operand.isdigit(), operands)):
            response = "Error: Numbers must only contain digits."
            break

        # More than 4 digit handler
        if not all(map(lambda x: len(x) < 5, operands)):
            response = "Error: Numbers cannot be more than four digits."
            break

        # Get 1st operands, lines. andswers and alignments
        first_operands = ''
        lines = ''
        answers = list(map(lambda problem: eval(problem), problems))
        solutions = ''
        for index in range(0, len(operands), 2):
            spaces = max(len(operands[index]), len(operands[index+1])) + 2
            first_operands += operands[index].rjust(spaces)
            lines += '-' * spaces
            solutions += str(answers[index // 2]).rjust(spaces)
            if index != len(operands) - 2:
                first_operands += ' ' * 4
                lines += ' ' * 4
                solutions += ' ' * 4

        # Get 2nd operand and alignments
        second_operands = ''
        for index in range(1, len(operands), 2):
            spaces = max(len(operands[index - 1]), len(operands[index])) + 1
            second_operands += operators[index // 2]
            second_operands += operands[index].rjust(spaces)
            if index != len(operands) - 1:
                second_operands += ' ' * 4

        # Show answer handler
        if show_answers:
            response = '\n'.join((first_operands, second_operands, lines, solutions))
            break
        else:
            response = '\n'.join((first_operands, second_operands, lines))
            break
    return response

# def main():
#     print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))

# main()