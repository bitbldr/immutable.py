import inspect

def is_method(obj, name):
    return hasattr(obj, name) and inspect.ismethod(getattr(obj, name))

class Node:
  label = None
  key = None
  value = None
  parent = None
  children = None
  
  def __init__(self, label=None, key=None, value=None, parent=None, children=None):
    self.label = label
    self.key = key
    self.value = value
    self.parent = parent
    self.children = children.copy() if children != None else dict()

  """
  Returns a shallow clone of the node
  """
  def clone(self, parent=None):
    return Node(
      self.label,
      self.key,
      self.value,
      (parent if parent != None else self.parent),
      self.children,
    )

  def __str__(self):
    return f'Node {hex(hash(self))} [ key: {self.key}, label: {self.label}, value: {str(self.value)} ]'

class ImmutableTrie:
  head = None
  size = 0

  def __init__(self, head=None, size=0):
    if head is None:
      self.head = Node(label='')
    else:
      self.head = head

    self.size = size

  """
  Returns a new Trie with the item set at the specified key
  """
  def set(self, key, value):
    if key is None or len(key) == 0:
      raise ValueError('Trie.set: key must be a non-empty, non-null string')

    # create a clone of head for the new Trie
    new_head = self.head.clone()
    current_node = new_head

    exists = True
    for i in range(len(key)):
      # current_node is already a clone, find and clone child with updated parent
      if not key[i] in current_node.children:
        exists = False
        current_node.children[key[i]] = Node(key[i], key, None, current_node)
      else:
        current_node.children[key[i]] = current_node.children[key[i]].clone(parent=current_node)
      
      # set current_node to new child, and repeat
      current_node = current_node.children[key[i]]

    # store the value at the end node of the cloned branch
    current_node.value = value

    # return a new trie with the new updated head
    newSize = self.size if exists else self.size + 1
    return ImmutableTrie(new_head, newSize)

  """
  Returns a new Trie with the item removed at the specified key.
  If the key doesn't exist, it returns the same trie
  """
  def remove(self, key):
    if key is None or key == '':
      raise ValueError('Trie.has: key must be a non-empty, non-null string')

    # create a clone of head for the new Trie
    new_head = self.head.clone()
    current_node = new_head

    # Recurse down the trie to the item
    current_node = self.head
    for label in key:
      if label in current_node.children:
        current_node.children[label] = current_node.children[label].clone(parent=current_node)
        current_node = current_node.children[label]
      else:
        current_node = None
        break

    if current_node is None:
      # key not found, return the same trie
      return self

    # key was found, remove it from the cloned branch
    label = current_node.label
    current_node.parent.children[label] = None

    # return a new trie with the new updated head
    return ImmutableTrie(new_head, self.size - 1)
    

  """
  Returns true if the key exists in the trie
  """
  def has(self, key):
    if key is None or key == '':
      raise ValueError('Trie.has: key must be a non-empty, non-null string')

    # Start at the top
    current_node = self.head
    exists = True
    for letter in key:
      if letter in current_node.children:
        current_node = current_node.children[letter]
      else:
        exists = False
        break

    # check if key a subkey that isn't actually a full key
    if exists:
      if current_node.value == None:
        exists = False

    return exists

  """
  Returns the value at the given key
  """
  def get(self, key):
    # Recurse down the trie to get value
    current_node = self.head
    for letter in key:
      if letter in current_node.children:
        current_node = current_node.children[letter]
      else:
        return None

    return current_node.value

  """
  Returns the node at the given key
  """
  def get_node(self, key):
    # Recurse down the trie to get node
    current_node = self.head
    for letter in key:
      if letter in current_node.children:
        current_node = current_node.children[letter]
      else:
        return None

    return current_node

  """
  Returns a list of all keys in tree
  """
  def keys(self):
    keys = list()

    # Get all keys under prefix. Initialize the queue to all items under top_node
    queue = [val for key, val in self.head.children.items()]

    # Perform a breadth first search
    # BFS will return a list of keys ordered by increasing length
    while queue:
      current_node = queue.pop()
      if current_node.value != None:
        keys.append(current_node.key)
      queue = [val for key, val in current_node.children.items()] + queue

    return keys

  def values(self):
    values = list()

    # Initialize the queue to all items under head node
    queue = [val for key, val in self.head.children.items()]

    # Perform a breadth first search using the queue
    # BFS will return a list of values ordered by increasing length of keys
    while queue:
      current_node = queue.pop()
      if current_node.value != None:
        values.append(current_node.value)
      queue = [val for key, val in current_node.children.items()] + queue

    return values

  """
  Returns true if the trie is empty
  """
  def is_empty(self):
    return self.size == 0

  """
  Returns a string representation of the trie
  """
  def __str__(self, node=None):
    if node is None:
      return str(self.head)
    else:
      s = '[ Node: ' + node.key + ' ]\n'
      for _, child in node.children.items():
        s = s + str(child)
      return s