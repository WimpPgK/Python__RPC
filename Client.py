import rpyc

def executeFunction01(data):
    try:
        result = connection.root.run_fibonacci(data)
        print(result)
    except Exception as Err:
        print('Error in send argument', str(Err))


if __name__ == '__main__':

    try:
        connection = rpyc.connect('192.168.0.52', 19961)     # adres ip i port
    except:
        print("Connection error")

    while True:
        value = input("Wpisz wyraz ciagu ktory chcesz obliczyc:    ")
        if value == 'q':
            break
        else:
            executeFunction01(int(value))