#!/usr/bin/python env
# -*- coding: utf-8 -*-

"""
"""

__author__ = "joshliu"

import os
import csv
from utils import log

def read(path):
	if os.path.isfile(path) == False or os.path.exists(path) == False:
		log.e("Input exception!")

	content = ''
	(filename, ext) = os.path.splitext(path)
	if ext == '.txt':
		content = _read_large_txt(path)
	elif ext == '.csv':
		content = _read_csv(path)
	else:
		log.e(ext + ' not suppored')

	return content

def _read_large_txt(path):
	chunk_size = 1024
	content = ''
	with open(path, "r") as f:
		for chunk in iter(lambda: f.read(chunk_size), ''):
			content += chunk
	return content 

def _read_csv(path):
	content = []
	with open(path, 'r') as f:
		dict_f = csv.DictReader(f, None, None, None, csv.excel)
		for row in dict_f:
			content.append(row)
	return content

if __name__ == "__main__":
	pass
