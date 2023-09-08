class Node():
  def __init__(self,value, link_node = None):
    self.value = value
    self.link_node = link_node

  def get_value(self):
    return self.value
  
  def get_link_node(self):
    return self.link_node
  
  def set_link_node(self,link_node):
    self.link_node = link_node

  def set_value(self,value):
    self.value = value

yak = Node("I ")
bak = Node("am ")
mak = Node("mak ")

yak.set_link_node(bak)
bak.set_link_node(mak)

print("yaks value is {}".format(yak.get_value()))
print("baks value is {}".format(bak.get_value()))
print("mak value is {}".format(mak.get_value()))

print(yak.get_value() + bak.get_value() + mak.get_value())

print(yak.get_value() + yak.get_link_node().get_value() + yak.get_link_node().get_link_node().get_value())