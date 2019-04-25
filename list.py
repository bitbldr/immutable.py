from trie import ImmutableTrie
import inspect

# class List(IndexedSequence):
class List:
  data = None

  def __init__(self, value):
    if List.is_list(value):
      self = value
      return
    self.data = ImmutableTrie()

  @staticmethod
  def is_list(value):
    return inspect.isclass(List)
  
  @staticmethod
  def of(value):
    return List(value)
  
  def set(self):
    pass
  
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
  
  def slice(self):
    pass
  
  def first(self):
    pass

  def last(self):
    pass

  def __str__(self):
    pass
  