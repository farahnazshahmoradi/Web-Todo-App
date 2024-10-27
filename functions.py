def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
    to-do items
    """
    with open(filepath, 'r') as local_file:
        todos_local = local_file.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ write the to-do items in the text file."""
    with open(filepath, 'w') as local_file:
        local_file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())
