# to do app used in the command line

# prints instructions to the cli
print('''instructions: 
type ADD to add new to do.
type REMOVE to remove to do from list.
type LIST to see list.''')


to_dos = []


def add_to_do(text):
    print('added ', text)


def remove_to_do(index):
    print('removed', index)


def show_to_dos():
    print(to_dos)


def interface():
    command = input()
    print(command)


interface()
