import rpyc

def executeFunction(data):
    try:
        result = connection.root.execute_code(data)
        print('Fibb [' + str(value) + '] = ' + str(result))
    except Exception as Err:
        print('Error in send argument', str(Err))



if __name__ == '__main__':


    try:
        connection = rpyc.connect('localhost', 19961)     # adres ip i port
    except:
        print("Connection error")
        exit()


    with open('code.txt', 'r') as file:
        content = file.readlines()

    connection.root.save_code(content)

    while True:
        value = input("Wpisz wyraz ciagu ktory chcesz obliczyc:    ")
        if value == 'q':
            break
        else:
            result = executeFunction(value)

