import unittest
import json
from urllib.request import urlopen

class TestBookDetailsClientFlask(unittest.TestCase):
    def test_render_json_book_details(self):
        homepage_json = json.load(urlopen("http://127.0.0.1:5000/topBookQuotes?author=Susanna%20Clarke"))
        checkrow = ["Susanna Clarke", "Jonathan Strange & Mr Norrell", "\u201cTime and I have quarrelled. All hours are midnight now. I had a clock and a watch, but I destroyed them both. I could not bear the way they mocked me.\u201d"]
        self.assertIn(checkrow, homepage_json)

    def test_render_json_book_details_empty(self):
        homepage_json = json.load(urlopen("http://127.0.0.1:5000/topBookQuotes"))
        self.assertEqual([], homepage_json)

    def test_render_json_book_details_not_listed_author(self):
        homepage_json = json.load(urlopen("http://127.0.0.1:5000/topBookQuotes?author=William%20Shakespeare"))
        self.assertEqual([], homepage_json)

    def test_render_json_authors_list(self):
        homepage_json = json.load(urlopen("http://127.0.0.1:5000/authors"))
        checkrow = 'Terry Pratchett'
        self.assertIn(checkrow, homepage_json)

if __name__ == '__main__':
    unittest.main()
