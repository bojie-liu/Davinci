#!/usr/bin/python env
# -*- coding: utf-8 -*-

"""
Description:
"""

__author__ = "joshliu"

import logging
import sys

import gensim.corpora


class MMCorpus(object):

	def __init__(self, corpus_path="/Users/joshualiu/dev/data/word2vec-for-wiki-master/wiki.cn.text.jian.removed",
			dict_path="/Users/joshualiu/dev/tmp/wiki_O1.dict"):
		self._corpus_path = corpus_path
		self._dict = gensim.corpora.Dictionary.load(dict_path)

	def __iter__(self):
		for line in open(self._corpus_path):
			yield self._dict.doc2bow(line.split(" "))

	def doc_bow(self):
		for line in open(self._corpus_path):
			return self._dict.doc2bow(line.split(" "))


def train_corpus(input_corpus, input_dict, output_corpus):
	corpus = MMCorpus(input_corpus, input_dict)
	logging.info(corpus)
	gensim.corpora.MmCorpus.serialize(output_corpus, corpus)


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)

	if len(sys.argv) != 4:
		logging.error("train_corpus $input_corpus $input_dict $output_corpus")
		sys.exit()

	train_corpus(sys.argv[1], sys.argv[2], sys.argv[3])