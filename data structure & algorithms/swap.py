import Linked_list

def swap_nodes(input_list, val1, val2):
    print(f'Start swapping {val1} with {val2}...')

    node1_prev = None
    node2_prev = None
    node1 = input_list.head_node
    node2 = input_list.head_node

    if val1 == val2:
        print("No point of swapping, two values are the same!")
        return 
    
    while node1 is not None:
        if node1.get_value() == val1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()
    
    while node2 is not None:
        if node2.get_value() == val2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()

    if (node1 is None or node2 is None):
        print("Swap not possible, one or more element not in lsit!")
        return
    
    if node1_prev is None:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)

    if node2_prev is None:
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)

    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)

# This version solves the adjacent node issue
def swap_nodes(input_list, val1, val2):
    print(f'Start swapping {val1} with {val2}...')
    
    if val1 == val2:
        print("No point of swapping, two values are the same!")
        return

    node1_prev = None
    node2_prev = None
    node1 = input_list.head_node
    node2 = input_list.head_node

    while node1 and node1.get_value() != val1:
        node1_prev = node1
        node1 = node1.get_next_node()

    while node2 and node2.get_value() != val2:
        node2_prev = node2
        node2 = node2.get_next_node()

    if not node1 or not node2:
        print("Swap not possible, one or more elements not in the list!")
        return

    # If node1_prev is None, it means node1 is the head node.
    if not node1_prev:
        input_list.head_node = node2
    else:
        node1_prev.set_next_node(node2)

    # If node2_prev is None, it means node2 is the head node.
    if not node2_prev:
        input_list.head_node = node1
    else:
        node2_prev.set_next_node(node1)

    # Handle the scenario when node1 and node2 are adjacent
    if node1_prev == node2:
        temp = node1.get_next_node()
        node1.set_next_node(node2)
        node2.set_next_node(temp)
    elif node2_prev == node1:
        temp = node2.get_next_node()
        node2.set_next_node(node1)
        node1.set_next_node(temp)
    else:
        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)

input_list = Linked_list.LinkedList()
for i in range(10):
    input_list.insert_beginning(i)
print(input_list.stringfy_list())

swap_nodes(input_list, 9, 9)
print(input_list.stringfy_list())