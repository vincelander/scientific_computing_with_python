"""
    Lambda interpretation,
        Just liike a function but simple operations/functions.
        normal function:
            def func_name:(param_x):
                return x * 2
            
        lambda:
            lambda_var_name = lambda x: x* 2

        OUTPUT: if x = 2
            4
        
        Can be used to simplify loop and loop + if
        e.g.
        normal function:
            new_list = []
            for item in sample_list:
                new_list.append(item*2)
                
        lambda:
            lambda_var_name = list(map(lambda X: X*2, sample_list))

        OUPUT: if ssample_list = [1,2,3,4]
            [2, 4, 6, 8]
        
    Can also print the sum of applied operation per item in list, just use the sum() funcion and lamda as parameter inside.
    Can also be used to return filtered list when condition is met per item in list
        normal function:
            new_list = []
            for item in sample_list:
                if item % 2 == 0:
                    new_list.append(item)

        lambda:
            lambda_var_name = list(filter(lambda X: X % 2 == 0, sample_list))

        OUTPUT: if sample_list = [1,2,3,4]
            [2, 4]

"""