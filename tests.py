import unittest
from datetime import datetime
from pyft import FT

class TestFTAPI(unittest.TestCase):

    def  setUp(self):
        self.ft = FT()

        #this tests with key file/environ, make tests for these individually

    def test_content(self):
        
        content_json = self.ft.get_content("6f2ca3d6-86f5-11e4-982e-00144feabdc0")
        self.assertTrue("bodyXML" in content_json)

    def test_content_notifications(self):
        
        #test since yesterday 
        #yesterday = datetime.now()
        content_json = self.ft.get_content_notifications("2015-01-01")
        self.assertTrue("requestUrl" in content_json)
        self.assertTrue("notifications" in content_json)
        
if __name__ == "__main__":
    unittest.main()

