class DLNODE:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DList:
    def __init__(self):
        self.head = None
        #tail
        
    def insert_node_after(self, val, pos=False): #need condition for no pos, to add to back of list
        new_node = DLNODE(val)
        current_head = self.head
        if current_head ==None:
            self.head = new_node
            return self
        elif pos == False:
            runner = current_head
            while runner.next != None:
                runner = runner.next
            runner.next = new_node
            new_node.prev = runner  
            
        else:
            runner = current_head  #to make circular, you can have final node,next point to current head
            if runner.val == pos:
                new_node.prev =  runner
                new_node.next= runner.next
                runner.next = new_node
                runner.next.prev = new_node
                
                
            else:
                runner = runner.next
        return self
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.val)
            runner = runner.next
        return self

_list = DList()

_list.insert_node_after(9).insert_node_after(2,9).insert_node_after(3,9).insert_node_after(8).print_values()


    
