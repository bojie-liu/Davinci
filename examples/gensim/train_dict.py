#!/usr/bin/python env
# -*- coding: utf-8 -*-

"""
Description:
"""

__author__ = "joshliu"

import sys
from collections import defaultdict
import logging
import gensim.corpora


def train_dict(corpus_path, dict_path):
	_stopword_path = ""
	with open(corpus_path) as f:
		texts = f.read().split("\n")

		stopwords = []
		with open(_stopword_path) as stop_f:
			stopwords = stop_f.read().split("\n")

		logging.info("Has %d stopwords. " % (len(stopwords)))

		frequency = defaultdict(int)
		for text in texts:
			for token in text.split():
				frequency[token] += 1

		logging.info("Preparing corpus")
		corpus = [[token for token in text if frequency[token] > 3 and token not in stopwords] for text in texts]
		logging.info("Building dictionary")
		dictionary = gensim.corpora.Dictionary(corpus)
		dictionary.save(dict_path)
		print(dictionary)

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)

	if len(sys.argv) != 3:
		logging.error("train_dict.py $input_corpus $output_dict")
		sys.exit(0)

	train_dict(sys.argv[1], sys.argv[2])
