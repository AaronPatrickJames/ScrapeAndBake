import unittest
import Scrape


class TestScrape(unittest.TestCase):

    def test_getRequest(self):
        result = Scrape.getRequest("https://www.google.com");
        
        
