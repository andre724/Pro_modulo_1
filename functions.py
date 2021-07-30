'''
Module for functions
'''
def mult_check(*x):
    '''
    This function checks if the arguments passed are multiples of 5 and 7
    '''
    test_results=[]
    for i in x:
        check_5 = i%5
        check_7 = i%7
        if check_5==0 and check_7 == 0:
            result= 'fizzbuzz'
            test_results.append(result)
        elif check_7 == 0:
            result = 'buzz'
            test_results.append(result)
        elif check_5  == 0:
            result = 'fizz'
            test_results.append(result)
        else:
            result = 'miss'
            test_results.append(result)
    return test_results
