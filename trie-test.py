import unittest
from trie import ImmutableTrie

class TestImmutableTrie(unittest.TestCase):

  def test_keys_and_values(self):
    trie1 = ImmutableTrie()
    trie2 = trie1.set('key1', 'value1')
    trie3 = trie2.set('key2', 'value2')
    trie4 = trie3.set('abc', '123')

    self.assertEqual(set(trie1.keys()), set([]))
    self.assertEqual(set(trie1.values()), set([]))

    self.assertEqual(set(trie2.keys()), set(['key1']))
    self.assertEqual(set(trie2.values()), set(['value1']))

    self.assertEqual(set(trie3.keys()), set(['key1', 'key2']))
    self.assertEqual(set(trie3.values()), set(['value1', 'value2']))

    self.assertEqual(set(trie4.keys()), set(['key1', 'key2', 'abc']))
    self.assertEqual(set(trie4.values()), set(['value1', 'value2', '123']))

  def test_has(self):
    trie1 = ImmutableTrie()
    trie2 = trie1.set('key1', 'value1')
    trie3 = trie2.set('key2', 'value2')
    trie4 = trie3.set('abc', '123')

    self.assertTrue(trie4.has('key1'))
    self.assertTrue(trie4.has('abc'))
    self.assertFalse(trie4.has('k'))
    self.assertFalse(trie4.has('ab'))
    self.assertFalse(trie4.has('key123'))
    
if __name__ == '__main__':
  unittest.main()