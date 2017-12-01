import unittest # Importing the unittest module
from user_test import User # Importing the user class

class User(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
         unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):

        '''
        set up method to run before each test casesself.
        '''

self.new_user = User("davy","mark","markkariuki17@gmail.com") # create user object

def test_init(self):

    '''
    test_init test case to test if the object is initialized properly
    '''
    self.assertEqual(self.new_user.first_name,"davy")
    self.assertEqual(self.new_user.last_name,"mark")
    self.assertEqual(self.new_user.email,"markkariuki17@gmail.com")


if __name__ == '__main__':
    unittest.main()
