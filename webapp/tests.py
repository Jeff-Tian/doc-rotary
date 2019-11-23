from app import app

import os
import unittest


class AppTestCase(unittest.TestCase):

    def test_root_text(self):
        tester = app.test_client(self)
        response = tester.get('/')
        assert 'Hello world!'.encode() in response.data

    def test_blotter(self):
        tester = app.test_client(self)
        response = tester.get('/blotter/600848')
        assert response.data.startswith(b'{"name":')


if __name__ == '__main__':
    unittest.main()
