import unittest


class SkeletonTestSuite(unittest.TestCase):

    def setUp(self):
        print('Setup test')

    def tearDown(self):
        print('Teardown test')

    def test_mock(self):
        print('Testing asdada test')
