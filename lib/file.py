#! /usr/bin/python
# -*- coding: utf-8 -*-
import os

class File(object):
    """docstring for File"""
    def __init__(self, file_path):
        self.file_path = file_path
        if os.path.isfile(file_path):
            self.file = open(file_path, 'a')
        else:
            if self.mk_path(file_path):
                self.file = open(file_path, 'w')
            else:
                raise 'not output file error'

    def __del__(self):
        if self.file:
            self.file.close
            pass
        else:
            pass

    def mk_path(self, file_path):
        path = os.path.split(file_path)[0]
        if os.path.exists(path):
            return True
        else:
            os.makedirs(path)
            return False

    def write(self, content):
        self.file.write(content)
        pass

    def close(self):
        self.file.close()
        pass