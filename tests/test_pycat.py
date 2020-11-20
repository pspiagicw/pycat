import unittest
import os
import time

from pycat.main import get_arguments
from pycat.main import cat_files
from pycat.main import process_arguments
from pycat.main import format_contents
from pycat import main



class TestPyCat(unittest.TestCase):

    def setUp(self):
        test_text = 'This is a test message'
        with open('test_file','w') as file:
            file.write(test_text)

    def tearDown(self):
        os.remove('test_file')


    def test_args(self)->None:
        arguments = '--version tags'.split()
        namespace = get_arguments(arguments)
        time.sleep(1)
        self.assertTrue(namespace.version)

    def test_args2(self)->None:
        arguments = 'test_file'
        time.sleep(1)
        namespace = get_arguments(arguments)
        self.assertEqual(namespace.files,list(arguments))
    def test_args3(self)->None:
        arguments = '--number test_file'.split()
        time.sleep(1)
        namespace = get_arguments(arguments)
        self.assertTrue(namespace.number)
        self.assertEqual(namespace.files,['test_file'])

    def test_reading(self)->None:
        arguments = ['test_file']
        time.sleep(1)
        args = get_arguments(arguments)
        files = process_arguments(args)
        contents = cat_files(files)
        self.assertEqual(contents,'This is a test message')

    def test_formatting(self)->None:
        arguments = ['test_file']
        time.sleep(1)
        args = get_arguments(arguments)
        files = process_arguments(args)
        contents = cat_files(files)
        lines = contents.split('\n')
        for i in range(len(lines)):
            lines[i] = str(i) + ' . ' + lines[i]
        lines = '\n'.join(lines)
        main.number = True
        self.assertEqual(lines,format_contents(contents))






if __name__ == '__main__':
    unittest.main()
