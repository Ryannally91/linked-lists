class SLNode:
    def __init__(self, val):
        self.val = val
        self.next= None
        
    def __repr__(self):
        return f' val:{self.val} next:{self.next.val}->'

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node =SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.val)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head == None:	# if the list is empty
            self.add_to_front(val)	# run the add_to_front method
            return self	# let's make sure the rest of this function doesn't happen if we add to the front
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node	# increment the runner to the next node in the list
        return self # return self to allow for chaining
    
    def insert_node(self, val, location):
        new_node= SLNode(val)
        runner = self.head
        counter = 0
        if location == 0:
            current_head = self.head
            new_node.next = current_head
            self.head = new_node
            return self
        else:
            while runner.next != None:
                if counter == location-1:
                    new_node.next = runner.next.next
                    runner.next = new_node
                    return self
                else:
                    runner = runner.next
                    counter+= 1
            return self
                


    def remove_front(self):
        if self.head != None:
            self.head = self.head.next
        return self
    
    def remove_back(self):
        runner = self.head
        while runner.next!= None:
            if runner.next.next == None:
                runner.next = None
            else:
                runner = runner.next
        return self
        #or (dojo solution) can also play around with saving previous node to a var to refernce
    def remove_from_back(self): 
        if self.head == None: #case of empty list
            return None
        elif self.head.next == None:#case if there is only one element or is the back
            self.head = None
            return self
        else:
            runner = self.head
            while runner.next.next!= None:
                runner = runner.next
            runner.next =None
        return self
            


    def remove_val(self, target):#need case if first item selected (paste in code from remove front funct)
        if self.head == None: #case of empty list
            return None
        elif self.head.next == None:
            self.head = None
            return self
        else:
            runner = self.head
            while runner is not None:
                if runner.val == target:
                    break
                prev_runner = runner
                runner = runner.next
                if runner == None:
                    return 'Target not present'
                prev_runner.next = runner.next
        return self
        
        #Optimize to take in multiple args
    def remove_values(self, *targets):#need case if first item selected (paste in code from remove front funct)
        for target in targets:
            if self.head == None: #case of empty list
                return None
            elif self.head.next == None:
                self.head = None
                return self
            else:
                runner = self.head
                while runner is not None:
                    if runner.val == target:
                        break
                    prev_runner = runner
                    runner = runner.next
                    if runner == None:
                        return 'Target not present'
                prev_runner.next = runner.next
        return self

    
test_1 = SList().add_to_back(9).add_to_back(8).add_to_back(7).add_to_back(6).add_to_back(5).add_to_back(4).add_to_back(3).print_values()

test_1.remove_values(3,8)
print('_______')
test_1.insert_node(100, 2).print_values()

    
_list = SList()

_list.add_to_front('sup')


_list.add_to_front(7).add_to_front(9).add_to_front('how')

# my_list = SList()	# create a new instance of a list
# my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()    # chaining, yeah!

# # r = 
# my_list.remove_front()
# # print(r)
# my_list.print_values()

# my_list.remove_back()
# my_list.print_values()

# _list.add_to_front('yo').add_to_back(99)
# _list.print_values()
# _list.remove_val('how')
# _list.print_values()

