#!/usr/bin/python env
# -*- coding: utf-8 -*-

"""
Description:
"""

# from __future__ import absolute_import

__author__ = "joshliu"

import sys
from collections import defaultdict
# from utils import log
import logging
import gensim.corpora


# log.get_logger('root')

def train_dict(corpus_path, dict_path):
	_stopword_path = ""
	with open(corpus_path) as f:
		texts = f.read().split("\n")

		stopwords = []
		# with open(_stopword_path) as stop_f:
		# 	stopwords = stop_f.read().split("\n")

		logging.info("Has %d stopwords. " % (len(stopwords)))

		frequency = defaultdict(int)
		# for text in texts:
		# 	for token in text.split():
		# 		frequency[token] += 1

		logging.info("Preparing corpus")
		corpus = [text.split() for text in texts]
		logging.info("Building dictionary")
		dictionary = gensim.corpora.Dictionary(corpus)
		dictionary.save(dict_path)
		print(dictionary)


def test_dict(dict_path):
	diction = gensim.corpora.Dictionary.load(dict_path)
	test = diction.items()
	pass

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)

	if len(sys.argv) != 3:
		logging.error("train_dict.py $input_corpus $output_dict")
		sys.exit(0)

	train_dict(sys.argv[1], sys.argv[2])
	# test_dict(sys.argv[2])
