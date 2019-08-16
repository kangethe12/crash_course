import unittest #importing the function
from modules import formated_name #import the function to be tested

class Namestestcase(unittest.TestCase):

  #Writing the 1st function test
  def test_first_last_name(self):
  #does names like 'john kangs' work
    test_name=formated_name('john','kangs')
    self.assertEqual(test_name,'John Kangs')

if __name__=='__main__':
  unittest.main()