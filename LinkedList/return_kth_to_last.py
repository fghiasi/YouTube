# 1- write dups from unsorted linked list
# 2- what if temp buffer is Not allowd

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print_linked_list(self, head):
        print("Prinitng Linked List Values: ")
        while head is not None:
            print("Node val is = ", head.val)
            head = head.next



# 3- iterative 
class solution:
    # 1- Space = O(n)
    # 2- time = O(n)
    def remove_dups_with_buffer(self, ll_head):
        if ll_head is None:
            return ll_head
        
        ll_head_holder = ll_head
        seen = dict()
        seen[ll_head.val] = True
        
        while ll_head.next is not None:
            if ll_head.next.val not in seen:
                seen[ll_head.next.val] = True
                ll_head = ll_head.next
            else:
                ll_head.next = ll_head.next.next

        return ll_head_holder
    
    # 1- Space = O(1)
    # 2- time = O(n^2)
    def remove_dups_without_buffer(self, ll_head):
        if ll_head is None:
            return ll_head
        
        ll_head_holder = ll_head

        while ll_head.next is not None:
            head_temp = ll_head
            node_value = ll_head.val
            
            while ll_head.next is not None:
                if node_value == ll_head.next.val:
                    ll_head.next = ll_head.next.next
                else:
                    ll_head = ll_head.next
                    
            if head_temp.next is not None:
                ll_head = head_temp.next
                
        return ll_head_holder
    
def main():
    
    temp_vals = [1,1,2,3,5,8,1,2,3,1,10,100000,-1,-2,-1]
    temp_ll = Node()
    temp_ll_head = temp_ll
    for val in temp_vals:
        temp_node =  Node()
        temp_node.val = val
        
        temp_ll.next = temp_node
        temp_ll = temp_ll.next
    
    temp_ll_head = temp_ll_head.next
    print("Before")
    Node().print_linked_list(temp_ll_head)
    # removed_dups = solution().remove_dups_with_buffer(temp_ll_head)
    removed_dups = solution().remove_dups_without_buffer(temp_ll_head)
    print("After")
    Node().print_linked_list(removed_dups)

if __name__ == "__main__":
    main()
    