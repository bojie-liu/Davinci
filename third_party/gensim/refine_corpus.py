#!/usr/bin/python env
# -*- coding: utf-8 -*-

"""
Description:
"""

__author__ = "joshliu"

import logging
import sys

def refine(input, output):

	pos_words = []
	with open('/Users/joshualiu/dev/data/sentiment/pos_fin.txt') as fd:
		pos_words = fd.read().split('\n')

	neg_words = []
	with open('/Users/joshualiu/dev/data/sentiment/neg_fin.txt') as fd:
		neg_words = fd.read().split('\n')

	keep = pos_words + neg_words
	buffer = ''
	i = 0
	with open(input) as fd:
		for line in fd.readlines():
			news = line.split(' ')
			refined_news = [word for word in news if word in keep]
			test = ' '.join(refined_news)
			test += '\n'
			buffer += test
			i += 1
			print(i)

	with open(output, mode='w') as fd:
		fd.write(buffer)

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)

	if len(sys.argv) != 3:
		logging.error("train_dict.py $input_corpus $output_corpus")
		sys.exit(0)

	refine(sys.argv[1], sys.argv[2])