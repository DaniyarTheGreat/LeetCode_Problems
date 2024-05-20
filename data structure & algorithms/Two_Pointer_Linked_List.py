from Linked_list import LinkedList

# returing the nth last node. E.g. 1, 2, 3, 4, 5 n = 2 -- returns 4
def nth_last_node(linked_list, n):
    current_node = None
    tail_node = linked_list.head_node
    count = 1

    while tail_node:
        tail_node = tail_node.get_next_node()
        count += 1

        if count >= n + 1:
            if current_node is None:
                current_node = linked_list.head_node
            else:
                current_node = current_node.get_next_node()
    return current_node

# returns the middle node of the list by using two pointers; fast pointer travels two times the speed of the slow, when fast reaches the end, slow will reach middle
def find_middle(linked_list):
    slow_pointer = linked_list.head_node
    fast_pointer = linked_list.head_node
    while fast_pointer:
        fast_pointer = fast_pointer.get_next_node()
        if fast_pointer:
            fast_pointer = fast_pointer.get_next_node()
            slow_pointer = slow_pointer.get_next_node()

    return slow_pointer

# def generate_test_linked_list():
#     linked_list = LinkedList()
#     for i in range(50, 0, -1):
#         linked_list.insert_beginning(i)
#     return linked_list

# # Use this to test your code:
# test_list = generate_test_linked_list()
# print(test_list.stringfy_list())
# nth_last = nth_last_node(test_list, 4)
# print(nth_last.get_value())

def generate_test_linked_list(length):
    linked_list = LinkedList()
    for i in range(length, 0, -1):
        linked_list.insert_beginning(i)
    return linked_list

# Use this to test your code:
test_list = generate_test_linked_list(7)
print(test_list.stringfy_list())
middle_node = find_middle(test_list)
print(middle_node.value)