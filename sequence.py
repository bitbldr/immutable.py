from abc import ABC, abstractmethod

"""
Sequence Abstract Class
""" 
class Sequence(ABC):
 
  def __init__(self):
    super().__init__()

"""
KeyedSequence Abstract Class
""" 
class KeyedSequence(Sequence):

  def __init__(self, value):
    self.value = value
    super().__init__()
  
  @abstractmethod
  def get(self):
    pass
  
  @abstractmethod
  def set(self):
    pass
  
  @abstractmethod
  def has(self):
    pass
  
  @abstractmethod
  def first(self):
    pass
  
  @abstractmethod
  def last(self):
    pass
  
  @staticmethod
  def of(value):
    raise NotImplementedError()

"""
IndexedSequence Abstract Class
""" 
class IndexedSequence(Sequence):

  def __init__(self, value):
    self.value = value
    super().__init__()
  
  @staticmethod
  def isList(value):
    raise NotImplementedError()
  
  @staticmethod
  def of(value):
    raise NotImplementedError()
  
  @abstractmethod
  def get(self):
    pass
  
  @abstractmethod
  def set(self):
    pass
  
  @abstractmethod
  def has(self):
    pass
  
  @abstractmethod
  def first(self):
    pass
  
  @abstractmethod
  def last(self):
    pass
    

"""
SetSequence Abstract Class
""" 
class SetSequence(Sequence):

  def __init__(self, value):
    self.value = value
    super().__init__()
  
  @staticmethod
  def of(value):
    raise NotImplementedError()