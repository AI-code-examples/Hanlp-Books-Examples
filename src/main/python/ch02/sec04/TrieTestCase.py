import unittest

from Python.ch02.sec04.Trie import Trie


class TrieTestCase(unittest.TestCase):
    def test_add(self):
        trie = Trie()

        # 增
        trie["自然"] = 'nature'
        trie["自然人"] = 'human'
        trie["自然语言"] = 'language'
        trie["自语"] = 'talk to oneself'
        trie["入门"] = 'introduction'
        self.assertIn('自然', trie)

    def test_delete(self):
        trie = Trie()

        # 删
        trie["自然"] = None
        self.assertNotIn('自然', trie)

    def test_modify(self):
        trie = Trie()

        # 改
        trie["自然语言"] = 'human language'
        self.assertEqual(trie["自然语言"],'human language')

    def test_search(self):
        trie = Trie()

        # 查
        trie["入门"] = 'introduction'
        self.assertEqual(trie["入门"],'introduction')


if __name__ == '__main__':
    unittest.main()
