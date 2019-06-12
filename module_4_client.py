import rpyc

class module_4_client:
    def __init__(self):
        server = rpyc.connect('localhost', 18871)
        server.root.create_table()
        content = self.get_file()
        server.root.save_code(content)
        my_program_id = int(server.root.get_program_id())
        server.root.compare_code(my_program_id)
        compare_info = server.root.get_message()
        print(compare_info)    
        while True:
            value = input("Wpisz wyraz ciagu ktory chcesz obliczyc:    ('q' aby wyjsc)")
            if value == 'q':
                break
            else:
                n_fib = int(value)
                result = str(server.root.execute_code(n_fib))
                print('Fibb ['+ str(n_fib) + '] = ' + str(result))


    def get_file(self):
        content = ''
        with open('code.txt', 'r') as file:
            content = file.readlines()
        return  content


if __name__ == "__main__":
    client = module_4_client()