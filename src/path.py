#!/usr/bin/env python3
# coding: utf8
import os, sys, pathlib, csv, json, datetime, locale, inspect
from string import Template
from collections import namedtuple

class Path:
#    def __init__(self, base=None):
#        self.__path = pathlib.Path(inspect.stack()[1].filename if base is None else base)
#    @property
#    def Path(self): return self.__path
#    @Path.setter
#    def Path(self, v): self.__path = v
    @property
    def This(self): return str(pathlib.Path(inspect.stack()[1].filename).resolve())
    @property
    def Here(self): return str(pathlib.Path(inspect.stack()[1].filename).parent.resolve())
    @property
    def Current(self): return str(pathlib.Path(os.getcwd()).resolve())
    @Current.setter
    def Current(self, v): os.chdir(v) # カレントディレクトリを指定パスに変更する
    @property
    def Name(self): return str(pathlib.Path(inspect.stack()[1].filename).resolve().name)
    @property
    def Stem(self): return str(pathlib.Path(inspect.stack()[1].filename).resolve().stem)
    @property
    def Ext(self): return str(pathlib.Path(inspect.stack()[1].filename).resolve().suffix)
    @property
    def Parts(self): return list(pathlib.Path(inspect.stack()[1].filename).resolve().parts)
    @property
    def Depth(self): return len(self.Parts)
        
    # 呼出元ディレクトリからの相対パス
    def here(self, path): return str(pathlib.Path(pathlib.Path(inspect.stack()[1].filename).parent, v).resolve())
    def depth(self, path): return len(list(pathlib.Path(path).resolve().parts))
    def here_parent(self, num=1): return self.parent(pathlib.Path(inspect.stack()[1].filename).resolve())
    def parent(self, path, num=1):
        if num < 1: raise ValueError(f'遡る階層数は1以上の自然数にしてください。num={num}')
        p = pathlib.Path(path).resolve()
        if len(p.parts) <= num: raise ValueError(f'遡る階層数が多すぎます。引数numの値は{len(p.parts)-1}までです。{str(p)}')
#        pl = list(p.parents)
#        return str(p if num <= 0 else pl[num - 1])
        return str(p if num < 1 else p.parents[num - 1])
    def name(self, path): return str(pathlib.Path(path).resolve().name)
    def stem(self, path): return str(pathlib.Path(path).resolve().stem)
    def ext(self, path): return str(pathlib.Path(path).resolve().suffix)
Path = Path()

