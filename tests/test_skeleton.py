import unittest


class SkeletonTestSuite(unittest.TestCase):

    def setup(self):
        print('Setup test')

    def teardown(self):
        print('Teardown test')

    def test_mock(self):
        print('Testing test')
