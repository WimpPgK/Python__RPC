import rpyc
from ResultsDataBase import ResultsDataBase

"""
    this module is a RPC client
"""

class module_4_client:

    def __init__(self, is_test_run, entered_value):
        """
            'is_test_run' param allows to test the function with different values with no need to enter them manually
            'enetered_value param is actual value entered in the tests

            the function reads given code file, gets parameter for the code from the user,
            invokes the server to save the code in the database, compare the code with other codes and save the differences in database, 
            compile, run the code and return the result

            then it prints the returned value to the user and saves in client-side database
        """
        server = rpyc.connect('localhost', 18871)
        resultsDataBase = ResultsDataBase()
        server.root.create_table()
        content = self.get_file()
        server.root.save_code(content)
        my_program_id = int(server.root.get_program_id())
        server.root.compare_code(my_program_id)
        compare_info = server.root.get_message()
        print(compare_info)   
        x = 0 
        while x < 1:
            if is_test_run == True:
                value = entered_value
                x += 1
            else:
                value = input("Wpisz wyraz ciagu ktory chcesz obliczyc: ('q' aby wyjsc): ")
            
            if value == 'q':
                break
            else: 
                result = str(server.root.execute_code(value))
                print('Fibb ['+ value + '] = ' + str(result) + '\n')
                
                result = ('Fibb ['+ value + ']', str(result))
                result_id = resultsDataBase.add_program_result(result)
                print("All results from base:")
                rows = resultsDataBase.select_all_results()
                print()

    def get_file(self):
        """
            reads 'code.txt' file and returns a list of its lines as a result
        """
        content = ''
        with open('code.txt', 'r') as file:
            content = file.readlines()
        return  content


if __name__ == "__main__":
    client = module_4_client(False, 1)