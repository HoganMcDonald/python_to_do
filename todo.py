# to do app used in the command line


to_dos = []


# prints instructions to the cli
def instructions():
    print('''instructions: 
    type ADD to add new to do.
    type REMOVE to remove to do from list.
    type LIST to see list.''')
    interface()


# add a new to do
def add_to_do(text):
    to_dos.append(text)
    print('added ', text)
    interface()


# remove a to do at a specific index
def remove_to_do(index):
    print('{} was removed from the list.'.format(to_dos[index]))
    del to_dos[index]
    interface()


# show all to dos in list
def show_to_dos(bool):
    if len(to_dos) > 1:
        for i in range(len(to_dos)):
            print(i + 1, '.  {}'.format(to_dos[i]))
    elif len(to_dos) == 1:
        print(1, '.  {}'.format(to_dos[0]))
    else:
        print('Nothing to show here. You can add to your list with ADD!')
    if not bool:
        interface()


# interface with user
def interface():
    command = input()
    if command.lower() == 'add':
        text = input('What do you need to do?   ')
        add_to_do(text)
    elif command.lower() == 'remove':
        if len(to_dos):
            show_to_dos(True)
            index = int(input('Which to do would you like to remove?   ')) - 1
            remove_to_do(index)
        else:
            print('You have an empty list.')
            interface()
    elif command.lower() == 'list':
        show_to_dos(False)
    else:
        print('I don\'t know that command! Try one of these.')
        instructions()


# initiate app
instructions()
