import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq_different_text(self):
        node = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Goodbye", TextType.BOLD)
        self.assertNotEqual(node, node2)
    def test_not_eq_different_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_not_eq_different_url(self):
        node = TextNode("Click Here", TextType.LINK, url="https://example.com")
        node2 = TextNode("Click Here", TextType.LINK, url="https://another.com")
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()