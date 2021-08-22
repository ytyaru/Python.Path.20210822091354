#!/usr/bin/env python3
# coding: utf8
import os,sys,pathlib,inspect
sys.path.append(str(pathlib.Path(__file__, '../../src').resolve()))
from path import Path
import unittest
class TestPath(unittest.TestCase):
    def setUp(self):
        self.excepted = '期待値'
    def test_This(self): self.assertEqual(Path.This, __file__)
    def test_Here(self): self.assertEqual(Path.Here, os.path.dirname(__file__))
    def test_Current_get(self): self.assertEqual(Path.Current, os.getcwd())
    def test_Current_set(self):
        expected = os.path.expanduser("~")
        Path.Current = expected 
        self.assertEqual(Path.Current, expected)
    def test_Name(self): self.assertEqual(Path.Name, os.path.basename(__file__))
    def test_Stem(self): self.assertEqual(Path.Stem, os.path.splitext(os.path.basename(__file__))[-2])
    def test_Ext(self): self.assertEqual(Path.Ext, os.path.splitext(os.path.basename(__file__))[-1])
    def test_Parts(self): self.assertEqual(Path.Parts, list(pathlib.Path(__file__).resolve().parts))
    def test_Depth(self): self.assertEqual(Path.Depth, len(list(pathlib.Path(__file__).resolve().parts)))
    def test_here_brother_0(self): self.assertEqual(Path.here('a.txt'), str(pathlib.Path(__file__, '../a.txt').resolve()))
    def test_here_brother_1(self): self.assertEqual(Path.here('./a.txt'), str(pathlib.Path(__file__, '../a.txt').resolve()))
    def test_here_parent(self): self.assertEqual(Path.here('../a.txt'), str(pathlib.Path(__file__, '../../a.txt').resolve()))
    def test_here_child(self): self.assertEqual(Path.here('some/a.txt'), str(pathlib.Path(__file__, '../some/a.txt').resolve()))
    def test_here_abs(self): self.assertEqual(Path.here('/some/a.txt'), str(pathlib.Path(__file__, '../some/a.txt').resolve()))
    def test_here_last_slash(self): self.assertEqual(Path.here('/some/a.txt/'), str(pathlib.Path(__file__, '../some/a.txt').resolve()))
    def test_here_empty(self): self.assertEqual(Path.here(''), os.path.dirname(__file__))
    def test_here_none(self): self.assertEqual(Path.here(None), os.path.dirname(__file__))

    def test_current_brother_0(self): self.assertEqual(Path.current('a.txt'), str(pathlib.Path(os.getcwd(), 'a.txt').resolve()))
    def test_current_brother_1(self): self.assertEqual(Path.current('./a.txt'), str(pathlib.Path(os.getcwd(), 'a.txt').resolve()))
    def test_current_parent(self): self.assertEqual(Path.current('../a.txt'), str(pathlib.Path(os.getcwd(), '../a.txt').resolve()))
    def test_current_child(self): self.assertEqual(Path.current('some/a.txt'), str(pathlib.Path(os.getcwd(), 'some/a.txt').resolve()))
    def test_current_abs(self): self.assertEqual(Path.current('/some/a.txt'), str(pathlib.Path(os.getcwd(), 'some/a.txt').resolve()))
    def test_current_last_slash(self): self.assertEqual(Path.current('/some/a.txt/'), str(pathlib.Path(os.getcwd(), 'some/a.txt').resolve()))
    def test_current_empty(self): self.assertEqual(Path.current(''), os.getcwd())
    def test_current_none(self): self.assertEqual(Path.current(None), os.getcwd())

    def test_depth(self): self.assertEqual(Path.depth('/'), 1)
    def test_depth(self): self.assertEqual(Path.depth('/tmp'), 2)
    def test_depth(self): self.assertEqual(Path.depth('/tmp/a.txt'), 3)
    def test_depth(self): self.assertEqual(Path.depth('/tmp/work/../a.txt'), 3)
    def test_depth(self): self.assertEqual(Path.depth('a.txt'), len(pathlib.Path(__file__, '../a.txt').parts))
    def test_depth(self): self.assertEqual(Path.depth('./a.txt'), len(pathlib.Path(__file__, '../a.txt').parts))
    def test_depth(self): self.assertEqual(Path.depth('../a.txt'), len(pathlib.Path(__file__, '../../a.txt').parts))
    def test_depth(self): self.assertEqual(Path.depth(''), len(pathlib.Path(__file__).resolve().parts))
    def test_depth(self): self.assertEqual(Path.depth(None), len(pathlib.Path(__file__).resolve().parts))
#    def test_depth(self): self.assertEqual(Path.depth(''), len(pathlib.Path(os.path.expanduser("~")).resolve().parts))
        
if __name__ == "__main__":
    unittest.main()
