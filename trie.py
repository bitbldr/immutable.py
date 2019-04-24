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
    self.children = children if children != None else dict()

  def clone(self, parent=None):
    return Node(
      self.label,
      self.key,
      self.value,
      (parent if parent != None else self.parent),
      self.children,
    )

class ImmutableTrie:
  head = None

  def __init__(self, head=None):
    if head == None:
      self.head = Node(label='')
    else:
      self.head = head

  def set(self, key, value):
    if key == None or len(key) == 0:
      raise ValueError('Trie.set: key must be a non-empty, non-null string')

    # create a clone of head for the new Trie
    new_head = self.head.clone()
    current_node = new_head

    for i in range(len(key)):
      # current_node is already a clone, find and clone child with updated parent
      if not key[i] in current_node.children:
        current_node.children[key[i]] = Node(key[i], key, None, current_node)
      else:
        current_node.children[key[i]] = current_node.children[key[i]].clone(current_node)
      
      # set current_node to new child, and repeat
      current_node = current_node.children[key[i]]

    # store the value at the new end node
    current_node.value = value

    # return a new trie with the new updated head
    return ImmutableTrie(new_head)

  def has(self, key):
    if key == '' or key == None:
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
  Returns value of the node at the given key
  """
  def get(self, key):
    if not self.has(key):
      raise ValueError('{} not found in trie'.format(key))

    # Recurse down the trie to get value
    current_node = self.head
    for letter in key:
      current_node = current_node.children[letter]

    return current_node.value

  """
  Returns the node at the given key
  """
  def getNode(self, key):
    if not self.has(key):
      raise ValueError('{} not found in trie'.format(key))

    # Recurse down the trie to get node
    current_node = self.head
    for letter in key:
      current_node = current_node.children[letter]

    return current_node

  """
  Returns a list of all keys in tree
  """
  def keys(self):
    keys = list()

    # Get all keys under prefix. Initialize the queue to all items under top_node
    queue = [val for key, val in self.head.children.items()]

    # Perform a breadth first search under the prefix
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

  def first(self):
    pass

  def last(self):
    pass

  def isEmpty(self):
    pass

  def remove(self):
    pass

  def size(self):
    pass

  def subMap(self, key):
    # Determine end-of-prefix node
    current = self.head
    if key == None or key == '':
      raise ValueError('Trie.subMap: key must be a non-empty, non-null string')
    
    for label in key:
      if label in current.children:
        current = current.children[label]
      else:
        # Prefix not in tree, return empty list of keys
        return None
    
    return current

  """
  Returns a string representation of the trie
  """
  def toString(self, node=None):
    if node == None:
      return self.toString(self.head)
    else:
      str = '[ Node: ' + node.key + ' ]\n'
      for _, child in node.children.items():
        str = str + self.toString(child)
      return str