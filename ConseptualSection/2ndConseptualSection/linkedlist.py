

class Node:
    def __init__(self,v):
        self.val=v
        self.next=None 
        

    

class Linked_List:
    def __init__(self):
        self.head=None 

    def insert_at_pos(self,pos,val):
        newNode=Node(val)
        if pos==0:
            newNode.next=self.head
            self.head=newNode
        else:
            tmp=self.head
            for i in range(pos-1):
                tmp=tmp.next
                if tmp == None:
                    print("Out of bound")
                    return
            
            newNode.next=tmp.next
            tmp.next=newNode


    def insert_at_tail(self,val):
        newNode = Node(val)
        if self.head == None:
            self.head=newNode
        else:
            tmp=self.head
            while tmp.next != None:
                tmp=tmp.next 
            tmp.next=newNode

    def delete_at_pos(self,pos):
        if pos==0:
            delNode=self.head
            self.head=self.head.next 
            del delNode
        else:
            tmp=self.head
            for i in range(pos-1):
                tmp=tmp.next
                if tmp == None:
                    print("Out of bound")
                    return
            delNode = tmp.next 
            if tmp.next == None:
                print("Out of bound")
                return
            tmp.next=tmp.next.next
            del delNode

    def print_list(self):
        tmp=self.head
        while tmp != None:
            print(tmp.val)
            tmp=tmp.next
    
    def reverse(self):
        if self.head.next == None:
            return self.head 
        save=self.head 
        self.head=self.head.next 
        newHead = self.reverse()
        save.next.next=save
        save.next=None 
        return newHead

def main():
    lst = Linked_List()
    lst.insert_at_tail(10)
    lst.insert_at_tail(20)
    lst.insert_at_tail(30)
    lst.delete_at_pos(100)
    lst.head = lst.reverse()
    lst.print_list()

main()