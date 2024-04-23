def to_list_nodes(nodes_string):
    nodes_list = []
    if (nodes_string[0] == '[') and (nodes_string[-1] == ']'):
        nodes_string = nodes_string[1:-1]
        separator = None
        print(nodes_string.find(', '))
        print(nodes_string.find(','))
        if nodes_string.find(', ') > -1:
            separator = ', '
        else:
            if nodes_string.find(','):
                separator = ','
        print(separator)
        nodes_list = nodes_string.split(separator)
        print(nodes_string)
    return nodes_list


l = '[1,2,3,4,5,6]'
print(to_list_nodes(l))
