def get_int(start_message='Input int number:', error_message='Wrong value. Input int number:', end_message='Thank you.'):
    #input(f'{start_message}\n')
    #input(f'{error_message}\n')
    #input(f'{end_message}\n')
    print(start_message)
    x = 0
    while x == 0:
        try:
            x = int(input())
            print(end_message)
            return x
        except:
            print(error_message)


x = get_int()
print(x)