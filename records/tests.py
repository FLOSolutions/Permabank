import unittest

from utils.testing import DjangoTestCase

class TestPageLoad(DjangoTestCase):
    def test_wish_browse(self):
        response = self.client.get('/wishes/all/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
