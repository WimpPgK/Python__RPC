import rpyc

def executeFunction(data):


    # wywolanie na serwerze funkcji save_code, jako arg przeslny kod programu
    try:
        connection.root.save_code(content)
    except Exception as Err:
        print('Save_code error', str(Err))


    # wywolanie na serwerze funkcji execute_code wykonujacej przeslany kod
    try:
        result = connection.root.execute_code(data)
        print('Fibb [' + str(value) + '] = ' + str(result))
    except Exception as Err:
        print('Execute_code error', str(Err))



if __name__ == '__main__':

    try:
        connection = rpyc.connect('localhost', 19961)     # adres ip i port
    except:
        print("Connection error")
        exit()

    with open('code.txt', 'r') as file:
        content = file.readlines()

    while True:
        value = input("Wpisz wyraz ciagu ktory chcesz obliczyc:    ")
        if value == 'q':
            break
        else:
            result = executeFunction(value)

