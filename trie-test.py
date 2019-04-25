import unittest
from trie import ImmutableTrie

def get_stub_data():
  trie1 = ImmutableTrie()
  trie2 = trie1.set('sheep', 'bahhh')
  trie3 = trie2.set('cat', 'meow')
  trie4 = trie3.set('duck', 'quack')

  return (trie1, trie2, trie3, trie4)

class TestImmutableTrie(unittest.TestCase):

  def test_is_persistent(self):
    (trie1, trie2, trie3, trie4) = get_stub_data()

    self.assertIsNot(trie1, trie2)
    self.assertIsNot(trie2, trie3)
    self.assertIsNot(trie3, trie4)

  def test_set(self):
    trie2 = ImmutableTrie().set('sheep', 'bahhh')
    trie3 = trie2.set('cat', 'meow')
    trie4 = trie3.set('duck', 'quack')
    trie5 = (ImmutableTrie()
      .set('key3', 'bahhh') 
      .set('key4', 'meow')
      .set('key5', 'value3')
    )

    self.assertTrue(trie2.has('sheep'))
    self.assertTrue(trie3.has('cat'))
    self.assertTrue(trie4.has('duck'))
    self.assertFalse(trie3.has('duck'))
    self.assertFalse(trie2.has('k'))
    self.assertFalse(trie4.has('sheep23'))
    self.assertFalse(trie4.has('ab'))
    self.assertTrue(trie5.has('key3'))
    self.assertTrue(trie5.has('key4'))
    self.assertTrue(trie5.has('key5'))
  
  def test_has(self):
    (_, _, _, trie4) = get_stub_data()

    self.assertTrue(trie4.has('sheep'))
    self.assertTrue(trie4.has('duck'))
    self.assertFalse(trie4.has('s'))
    self.assertFalse(trie4.has('ck'))
    self.assertFalse(trie4.has('sheep23'))
  
  def test_get(self):
    (trie1, trie2, trie3, trie4) = get_stub_data()

    self.assertEqual(trie4.get('sheep'), 'bahhh')
    self.assertEqual(trie4.get('duck'), 'quack')
    self.assertIs(trie1.get('cat'), None)
    self.assertIs(trie2.get('duck'), None)
    self.assertIs(trie3.get('duck'), None)
    self.assertIs(trie4.get('c'), None)
    self.assertIs(trie4.get('ab'), None)
    self.assertIs(trie4.get('sheep23'), None)
  
  def test_get_node(self):
    (_, trie2, _, _) = get_stub_data()

    # find the node in the trie
    key = 'sheep'
    node = trie2.head
    for letter in key:
      if letter in node.children:
        node = node.children[letter]
      else:
        node = None
        break
    
    self.assertIsNot(node, None)
    self.assertIs(trie2.get_node(key), node)
  
  def test_keys(self):
    (trie1, trie2, trie3, trie4) = get_stub_data()

    self.assertEqual(set(trie1.keys()), set([]))
    self.assertEqual(set(trie2.keys()), set(['sheep']))
    self.assertEqual(set(trie3.keys()), set(['sheep', 'cat']))
    self.assertEqual(set(trie4.keys()), set(['sheep', 'cat', 'duck']))

  def test_values(self):
    (trie1, trie2, trie3, trie4) = get_stub_data()

    self.assertEqual(set(trie1.values()), set([]))
    self.assertEqual(set(trie2.values()), set(['bahhh']))
    self.assertEqual(set(trie3.values()), set(['bahhh', 'meow']))
    self.assertEqual(set(trie4.values()), set(['bahhh', 'meow', 'quack']))

  def test_size(self):
    (trie1, trie2, trie3, trie4) = get_stub_data()

    trie5 = (trie4
      .set('cow', 'moo')
      .remove('dog')  # no effect
      .set('dog', 'bark')
      
      .set('mouse', 'squeak')
      .remove('mouse')
      .remove('owl')  # no effect
    )

    # updating existing key should not change the size
    trie6 = trie5.set('dog', 'bark')

    self.assertEqual(trie1.size, 0)
    self.assertEqual(trie2.size, 1)
    self.assertEqual(trie3.size, 2)
    self.assertEqual(trie4.size, 3)
    self.assertEqual(trie5.size, 5)
    self.assertEqual(trie6.size, 5)

  def test_is_empty(self):
    (trie1, trie2, trie3, trie4) = get_stub_data()

    trie5 = (trie4
      .remove('sheep')
      .remove('cat')
      .remove('duck')
    )

    self.assertTrue(trie1.is_empty())
    self.assertFalse(trie2.is_empty())
    self.assertFalse(trie3.is_empty())
    self.assertFalse(trie4.is_empty())
    self.assertTrue(trie5.is_empty())

  def test_node_at_subkey(self):
    trie1 = ImmutableTrie().set('sheepdog', 'woof')
    trie2 = trie1.set('sheep', 'bahhh')

    self.assertIs(trie1.get('sheep'), None)
    self.assertEqual(trie1.get('sheepdog'), 'woof')
    self.assertEqual(trie2.get('sheep'), 'bahhh')
    self.assertEqual(trie2.get('sheepdog'), 'woof')

if __name__ == '__main__':
  unittest.main()