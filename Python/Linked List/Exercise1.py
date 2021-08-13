# exercise link: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/3_linked_list_exercise.md

# Code copied directly from the problem:
class Node:
    def __init__(self, data=None, next=None):
      self.data = data
      self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def print(self):
    if self.head is None:
        print("Linked list is empty")
        return
    itr = self.head
    llstr = ''
    while itr:
        llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
        itr = itr.next
    print(llstr)

  def get_length(self):
    count = 0
    itr = self.head
    while itr:
        count+=1
        itr = itr.next

    return count

  def insert_at_begining(self, data):
    node = Node(data, self.head)
    self.head = node

  def insert_at_end(self, data):
    if self.head is None:
        self.head = Node(data, None)
        return

    itr = self.head

    while itr.next:
        itr = itr.next

    itr.next = Node(data, None)

  def insert_at(self, index, data):
    if index<0 or index>self.get_length():
        raise Exception("Invalid Index")

    if index==0:
        self.insert_at_begining(data)
        return

    count = 0
    itr = self.head
    while itr:
        if count == index - 1:
            node = Node(data, itr.next)
            itr.next = node
            break

        itr = itr.next
        count += 1

  def remove_at(self, index):
    if index<0 or index>=self.get_length():
        raise Exception("Invalid Index")

    if index==0:
        self.head = self.head.next
        return

    count = 0
    itr = self.head
    while itr:
        if count == index - 1:
            itr.next = itr.next.next
            break

        itr = itr.next
        count+=1

  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
        self.insert_at_end(data)

# My code starts from here (solution):
  def insert_after_value(self, data_after, data_to_insert):
    itr = self.head
    while itr:
      if itr.data == data_after:
        new_node = Node(data_to_insert, itr.next)
        itr.next = new_node
        return
      itr = itr.next
    raise Exception("Data not present in list!")
  
  def remove_by_value(self, data):
    # new Code
    itr = self.head
    index = 0
    while itr:
      if itr.data == data:
        # at the beginning:
        if index == 0:
          self.head = self.head.next
          return
        break
      itr = itr.next
      index += 1
    
    if index == self.get_length():
      print("Element not in list!")
      return
    
    itr = self.head
    for i in range(index):
      if i == index - 1:
        # at the end:
        if i == self.get_length() - 1:
          itr.next = None
          return
        itr.next = itr.next.next
        return
      itr = itr.next


if __name__ == '__main__':
  ll = LinkedList()
  ll.insert_values(["banana","mango","grapes","orange"])
  ll.print()
  ll.insert_after_value("mango","apple") # insert apple after mango
  ll.print()
  ll.remove_by_value("orange") # remove orange from linked list
  ll.print()
  ll.remove_by_value("figs")
  ll.print()
  ll.remove_by_value("banana")
  ll.remove_by_value("mango")
  ll.remove_by_value("apple")
  ll.remove_by_value("grapes")
  ll.print()