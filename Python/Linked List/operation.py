class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insertion(self, check, data):
    # insert in beginning:
    if check == 'b':
      newNode = Node(data, self.head)
      self.head = newNode
      return
    
    # insert at last if list is empty
    if self.head == None:
      self.head = Node(data, None)
      return
    
    itr = self.head
    while itr.next:
      itr = itr.next
    itr.next = Node(data, None)
    return
  
  def insertWithIndex(self, data, index):
    if index == 0:
      newNode = Node(data, self.head)
      self.head = newNode
      return
    
    if index < 0 or index >= self.length():
      raise Exception("Invalid Index.")
    
    itr = self.head
    count = 0
    while itr:
      if count == index - 1:
        newNode = Node(data, itr.next)
        itr.next = newNode
        break
      itr = itr.next
      count += 1

  def length(self):
    itr = self.head
    count = 0
    while itr:
      itr = itr.next
      count += 1
    return count

  def deletion(self, index):
    if index < 0 or index >= self.length():
      raise Exception("Invalid index")
    
    if index == 0:
      self.head = self.head.next
      return
    
    itr = self.head
    count = 0
    while itr:
      if count == index - 1:
        itr.next = itr.next.next
        break
      count += 1
      itr = itr.next

  def display(self):
    if self.head == None:
      print("Empty List")
      return
    outputString = ''
    itr = self.head
    while itr:
      outputString += str(itr.data)
      outputString += '--->'
      itr = itr.next
    print(outputString)
    print("Length of list is: ", self.length())

if __name__ == '__main__':
  linkedList = LinkedList()
  data = 'a'
  print("Enter q to end: ")
  while data != 'q':
    data = input("Please enter the data to be populated: ")
    check = 'e'
    linkedList.insertion(check, data)
  
  linkedList.insertWithIndex('In Between', 2)
  linkedList.deletion(linkedList.length()-1)
  linkedList.display()