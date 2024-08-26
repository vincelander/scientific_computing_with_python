def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        raise ValueError('Error: Too many problems.')
    
    problem_list = list(
        map(
            lambda split:
            split.split(),
            problems
        )
    )

    new_problem_list = []
    lines = ''
    count = 0
    for problem in problem_list:
        first_operand = problem[0]
        second_operand = problem[2]
        operator = problem[1]
        max_value = max(int(first_operand), int(second_operand))
        min_value = min(int(first_operand), int(second_operand))
        spaces = len((str(max_value))) - len(str(min_value))
        str_max_value = str(max_value)

        if operator == '*' and operator == '/':
            raise ValueError("Error: Operator must be '+' or '-'.")
        
        if not first_operand.isdigit() or not second_operand.isdigit():
            raise ValueError('Error: Numbers must only contain digits.')
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            raise ValueError('Error: Numbers cannot be more than four digits.')

        if first_operand == str_max_value:
            problem[0] = first_operand.rjust(3 + spaces)
            problem[2] = second_operand.rjust(2 + spaces)
        else:
            problem[0] = first_operand.rjust(4 + spaces)
            problem[2] = second_operand.rjust(3 + spaces)

        new_problem_list.extend(problem)

        first_operand_list = new_problem_list[::3]
        second_operand_list = new_problem_list[2::3]
        operator_list = new_problem_list[1::3]

        first_operand_print = ''
        second_operand_print = ''
        operator_print = ''
        for f in first_operand_list:
            first_operand_print = first_operand_print + f'{f}\t'
            
        for s in second_operand_list:
            second_operand_print = second_operand_print + operator + f'{s}\t'

        if count == 0:
            lines = '_' * (len((str(max_value))) + 3)
            count += 1
        else:
            lines = lines + '\t' + '_' * (len((str(max_value))) + 2)
    print(first_operand_print)
    print(second_operand_print)
    print(lines)
    return first_operand_print, second_operand_print, lines

    # return first_operand_list, second_operand_list, operator_list
# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# TESTS
arithmetic_arranger(["3801 - 2", "123 + 49"])