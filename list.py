from trie import Trie
# from sequence import IndexedSequence`
import inspect

# class List(IndexedSequence):
class List:
  data = None

  def __init__(self, value):
    if List.isList(value):
      self = value
      return
    self.data = Trie()
    # super().__init__()

  @staticmethod
  def isList(value):
    return inspect.isclass(List)
  
  @staticmethod
  def of(value):
    return List(value)
  
  def set(self, index, value):
    
  
  def delete(self):
    pass
  
  def insert(self):
    pass
  
  def clear(self):
    pass
  
  def push(self):
    pass
  
  def pop(self):
    pass
  
  def unshift(self):
    pass
  
  def shift(self):
    pass
  
  def update(self):
    pass
  
  def setSize(self):
    pass
  
  
  def toString(self):
    pass
  