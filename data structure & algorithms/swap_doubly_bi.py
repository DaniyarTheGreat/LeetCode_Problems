import DoublyLinkedList

def swap_nodes_doubly(input, val1, val2):
    if val1 == val2:
        print("No point of swapping, two values are the same!")
        return
    
    node1 = input.head
    node2 = input.tail
    node1_prev, nod2_next = None, None
    found_val1, found_val2 = False, False

    while node1 and node2 and (not found_val1 or not found_val2):
        if node1.get_value() == val1:
            found_val1 = True
        elif node1.get_value() == val2:
            found_val2 = True
        else:
            node1_prev = node1
            node1 = node1.get_next_node()
        if node2.get_value() == val1:
            found_val1 = True
        elif node2.get_value() == val2:
            found_val2 = True
        else:
            node2_next = node2
            node2 = node2.get_prev_node()

    if not found_val1 or not found_val2:
        print("Swap not possible, one or more elements not present!")
        return

    # If node1 and node2 are adjacent, we need to handle it differently
    if node1.get_next_node() == node2:
        # Adjusting the previous of node2
        if node1_prev:
            node1_prev.set_next_node(node2)
        else:  # node1 was the head
            input.head = node2

        # Adjusting the next of node1
        node1.set_next_node(node2_next)
        if node1.get_next_node():
            node1.get_next_node().set_prev_node(node1)

        # Adjusting node1 and node2
        node2.set_next_node(node1)
        node2.set_prev_node(node1_prev)
        node1.set_prev_node(node2)

    elif node2_next == node1:
        # Adjusting the previous of node1
        if node2.get_prev_node():
            node2.get_prev_node().set_next_node(node1)
        else:  # node2 was the head
            input.head = node1

        # Adjusting the next of node2
        node2.set_next_node(node1.get_next_node())
        if node2_next:
            node2_next.set_prev_node(node2)

        # Adjusting node2 and node1
        node1.set_next_node(node2)
        node1.set_prev_node(node2.get_prev_node())
        node2.set_prev_node(node1)

    else:  # General case, where node1 and node2 are not adjacent
        # Adjusting the previous of node1 and node2
        if node1_prev:
            node1_prev.set_next_node(node2)
        else:  # node1 was the head
            input.head = node2

        if node2.get_prev_node():
            node2.get_prev_node().set_next_node(node1)
        else:  # node2 was the head
            input.head = node1

        # Adjusting the next of node1 and node2
        tmp = node1.get_next_node()
        node1.set_next_node(node2_next)
        node2.set_next_node(tmp)

        if node1.get_next_node():
            node1.get_next_node().set_prev_node(node1)
        if node2_next:
            node2_next.set_prev_node(node2)

        # Adjusting the previous pointers of node1 and node2
        node1.set_prev_node(node2.get_prev_node())
        node2.set_prev_node(node1_prev)

    # Adjusting the tail if necessary
    if input.tail == node1:
        input.tail = node2
    elif input.tail == node2:
        input.tail = node1
            


subway = DoublyLinkedList.DoublyLinkedList()
subway.add_to_head(1)
subway.add_to_head(2)
subway.add_to_head(3)
subway.add_to_tail(0)
subway.add_to_tail(-1)
subway.add_to_tail(-2)
print(subway.stringfy_list())
print(swap_nodes_doubly(subway, -1, 1))
print(subway.stringfy_list())


    # while not found_val1 and not found_val2:
    #     if node1.get_value() != val1:
    #         node1_prev = node1
    #         node1 = node1.get_next_node()
    #     else:
    #         found_val1 = True
    #     if node2.get_value() != val2:
    #         node2_next = node2
    #         node2 = node2.get_prev_node()
    #     else:
    #         found_val2 = True