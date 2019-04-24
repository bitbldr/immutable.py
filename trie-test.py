import unittest
from trie import ImmutableTrie

class TestImmutableTrie(unittest.TestCase):

  def test_keys(self):
    trie = ImmutableTrie()
    trie.set('key1', 'value1')
    trie.set('key2', 'value2')
    trie.set('abc', 'value3')

    print(trie.keys())
    print(trie.values())
    print(trie.getNode('key1').key, trie.getNode('key1').value)
    print(trie.getNode('key2').key, trie.getNode('key2').value)
    print(trie.getNode('abc').key, trie.getNode('abc').value)

    self.assertEqual('foo'.upper(), 'FOO')

  # def test_isupper(self):
  #     self.assertTrue('FOO'.isupper())
  #     self.assertFalse('Foo'.isupper())

  # def test_split(self):
  #     s = 'hello world'
  #     self.assertEqual(s.split(), ['hello', 'world'])
  #     # check that s.split fails when the separator is not a string
  #     with self.assertRaises(TypeError):
  #         s.split(2)

if __name__ == '__main__':
  unittest.main()