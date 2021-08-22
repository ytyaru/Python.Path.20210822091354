#!/usr/bin/env python3
# coding: utf8
import os,sys,pathlib
sys.path.append(str(pathlib.Path(__file__, '../../src').resolve()))
from path import Path
import unittest
class TestPath(unittest.TestCase):
    def setUp(self):
        self.excepted = '期待値'
    def test_this(self): self.assertEqual(Path.This, __file__)
    def test_here(self): self.assertEqual(Path.Here, os.path.dirname(__file__))
        
if __name__ == "__main__":
    unittest.main()
