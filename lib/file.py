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
            mk_path(file_path)

            self.file = open(file_path, 'w')

    def __del__(self):
        self.file.close
        pass

    def mk_path(self, file_path):
        print file_path
        path = os.path.split(file_path)[0]
        if os.path.exist(path):
            os.makedirs(path)
            return True
        else:
            return False

    def write(self, content):
        self.file.write(content)
        pass

    def close(self):
        self.file.close()
        pass