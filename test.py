from app import app
import unittest
import json

class APITest(unittest.TestCase):

    #check if GET News is a valid API
    def test_News_validRoute(self):
        tester = app.test_client(self)
        response = tester.get("/News/Jiraya-Sensei")
        self.assertEqual(response.status_code, 200)

    #check if GET News API has JSON response
    def test_News_validContenType(self):
        tester = app.test_client(self)
        response = tester.get("/News/Jiraya-Sensei")
        self.assertEqual(response.content_type, "application/json")

    #check if GET News API does not give empty response
    def test_News_validData(self):
        tester = app.test_client(self)
        response = tester.get("/News/Jiraya-Sensei")
        self.assertTrue(response.data)

     #check if GET Categories is a valid API
    def test_Categories_validRoute(self):
        tester = app.test_client(self)
        response = tester.get("/Categories/Jiraya-Sensei")
        self.assertEqual(response.status_code, 200)

    #check if GET Categories API has JSON response
    def test_Categories_validContenType(self):
        tester = app.test_client(self)
        response = tester.get("/Categories/Jiraya-Sensei")
        self.assertEqual(response.content_type, "application/json")

    #check if GET Categories API does not give empty response
    def test_Categories_validData(self):
        tester = app.test_client(self)
        response = tester.get("/Categories/Jiraya-Sensei")
        self.assertTrue(response.data)

     #check if PUT Categories is a valid API
    def test_Categories_Update_validRoute(self):
         tester = app.test_client(self)
         headers = {'content-type': 'application/json'}
         data = { 
            "business": True,
            "entertainment": False,
            "general": False,
            "health": True,
            "science": True,
            "sports": False,
            "technology": True
        }
         response = tester.put("/Categories/Jiraya-Sensei", data= json.dumps(data), headers= headers)
         self.assertEqual(response.status_code, 200)

     #check if PUT Categories API has JSON response
    def test_Categories_Update_validContenType(self):
         tester = app.test_client(self)
         headers = {'content-type': 'application/json'}
         data = { 
            "business": True,
            "entertainment": False,
            "general": False,
            "health": True,
            "science": True,
            "sports": False,
            "technology": True
        }
         response = tester.put("/Categories/Jiraya-Sensei", data= json.dumps(data), headers= headers)
         self.assertEqual(response.content_type, "application/json")

     #check if PUT Categories API does not give empty response
    def test_Categories_Update_validData(self):
         tester = app.test_client(self)
         headers = {'content-type': 'application/json'}
         data = { 
            "business": True,
            "entertainment": False,
            "general": False,
            "health": True,
            "science": True,
            "sports": False,
            "technology": True
        }
         response = tester.put("/Categories/Jiraya-Sensei", data= json.dumps(data), headers= headers)
         self.assertTrue(response.data)


     #check if GET News per category is a valid API
    def test_categorisedNews_validRoute(self):
        tester = app.test_client(self)
        response = tester.get("/News/category/General")
        self.assertEqual(response.status_code, 200)

    #check if GET News per category API has JSON response
    def test_categorisedNews_validContenType(self):
        tester = app.test_client(self)
        response = tester.get("/News/category/General")
        self.assertEqual(response.content_type, "application/json")

    #check if GET News per category API does not give empty response
    def test_categorisedNews_validData(self):
        tester = app.test_client(self)
        response = tester.get("/News/category/General")
        self.assertTrue(response.data)

    #check if GET News per category API gives error for invalid categories
    def test_categorisedNews_InvalidCategory(self):
        tester = app.test_client(self)
        response = tester.get("/News/category/xyz")
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['code'], 401)

    #check if GET News per category API gives news for valid categories
    def test_categorisedNews_validCategory(self):
        tester = app.test_client(self)
        response = tester.get("/News/category/General")
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['status'], 'ok')


if __name__ == "__main__":
    unittest.main()
