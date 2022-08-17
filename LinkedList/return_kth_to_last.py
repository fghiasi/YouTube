# From Cracking the Coding Interview Chapter 2 Linked List Question 2.2

# Implement an algorithm to find the kth to last element of singly linked list.

# Do we know the size of the Linked List? 
# size - kth to last and we iterate from head to size - kth to last

class Node:
    def __init__(self, next=None, val=None):
        self.next = next
        self.val = val

# create a Linked List from list of entegers and returns a pointer to the head.
class LinkedList:
    
    def __init__(self):
        self.head = Node()

        
    def convert_list_to_linked_list(self, list_of_integers):
        # if len(list_of_integers) == 0
        if not list_of_integers:
            return self.head
        
        
        pointer_to_head = self.head
        for num in list_of_integers:
            temp_node = Node()
            temp_node.val = num
            
            self.head.next = temp_node
            self.head = self.head.next
            
        return pointer_to_head.next
    
    # prints the Linked list values.
    def print_linked_list(self, head):    
        while head is not None:
            print(head.val)
            head = head.next

class Solution:
    # loop once and find the size
    # return the node that is positioned at size - kth_to_last
    # Running time O(n)
    # Space O(1)
#     def return_ll_kth_to_last(head, kth_to_last):
#         # if kth_to_last == 0:
#         #     return head
        
#         head_copy = head
#         size = 0
#         while head_copy is not None:
#             size += 1
#             head_copy = head_copy.next
        
        
#         if  (size - kth_to_last) <= 0:
#             print("Error: kth to last value is larger than linked list size. ")
#             raise
            
#         # return head
#         counter = 1
#         while counter != (size - kth_to_last):
#             counter += 1
#             head = head.next
#         return head

    # using runner method a bit efficient 
    def return_ll_kth_to_last(head, kth_to_last):
        p1 = head
        p2 = head
        
        counter = 0 
        head_copy = head
        while counter != kth_to_last:
            if p2 is None:
                print("Error: kth to last value is larger than linked list size. ")
                raise
            
            p2 = p2.next
            counter += 1
        
        while p2.next is not None:
            p2 = p2.next
            p1 = p1.next
        
        return p1
    
def main():
    temp_list = [1]
    linked_list_obj = LinkedList()
    temp_linked_list_head = linked_list_obj.convert_list_to_linked_list(temp_list)
    
    # linked_list_obj.print_linked_list(temp_linked_list_head)
    
    kth_to_last_node = Solution.return_ll_kth_to_last(temp_linked_list_head, 1)
    print("kth_to_last_node is = ", kth_to_last_node.val)

if __name__ == "__main__":
    main()