#!/usr/bin/python env
# -*- coding: utf-8 -*-

"""
Description:
"""

__author__ = "joshliu"

import sys
import logging
import gensim.corpora
import gensim.models

import numpy as np  # for arrays, array broadcasting etc.


def build_eta(shape, diction):
	eta = np.asarray([[(1.0 - 0.0002) / (shape[0] - 2) for i in range(shape[1])] for i in range(shape[0])])
	eta[0, :] = 0.0001
	eta[1, :] = 0.0001

	pos_words = []
	with open('/Users/joshualiu/dev/data/sentiment/pos_fin.txt') as fd:
		pos_words = fd.read().split('\n')

	neg_words = []
	with open('/Users/joshualiu/dev/data/sentiment/neg_fin.txt') as fd:
		neg_words = fd.read().split('\n')

	# for bow in diction.doc2bow(pos_words):
	# 	eta[:, bow[0]] = 0.01
	# 	eta[0, bow[0]] = 0.91
	#
	# for bow in diction.doc2bow(neg_words):
	# 	eta[:, bow[0]] = 0.01
	# 	eta[1, bow[0]] = 0.91

	eta[:, 1438] = 0.0001
	eta[0, 1438] = 0.9991

	return eta


def train_lda(input_corpus, input_dict, output_lda=None):
	corpus = gensim.corpora.MmCorpus(input_corpus)
	diction = gensim.corpora.Dictionary.load(input_dict)
	# test = diction.get(1, -1)
	# eta = build_eta((10, len(diction.items())), diction)
	lda = gensim.models.ldamulticore.LdaMulticore(corpus=corpus, id2word=diction, num_topics=5, chunksize=10000,
	                                              passes=1)
	if output_lda is not None:
		lda.save(output_lda)
	lda.print_topics()


def extract_sentiment(input_corpus, pos_corpus, neg_corpus):
	with open(pos_corpus) as fd:
		pos_words = fd.read().split('\n')

	with open(neg_corpus) as fd:
		neg_words = fd.read().split('\n')

	with open(input_corpus) as fd:
		input_words = fd.read().replace('\n', ' ').split(' ')

	ext_pos_words = []
	for pos_word in pos_words:
		pos_word = pos_word.replace(' ', '').replace('\n', '')
		if len(pos_word) == 0:
			continue
		tmp_word = [word for word in input_words if word.find(pos_word) != -1]
		# test = '上周一'.find('上')
		ext_pos_words += tmp_word
		if len(tmp_word) > 0:
			print(pos_word + ' ' + ' '.join(tmp_word))


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)

	if len(sys.argv) < 3:
		logging.error('python3 lda_demo.py $input_corpus $input_dict $output_lda')
		exit(-1)

	train_lda(sys.argv[1], sys.argv[2], sys.argv[3])
	# extract_sentiment(sys.argv[1], sys.argv[2], sys.argv[3])
	# corpus = gensim.corpora.MmCorpus(sys.argv[1])
	# diction = gensim.corpora.Dictionary.load(sys.argv[2])
	# lda = gensim.models.ldamulticore.LdaMulticore(corpus=corpus, id2word=diction, num_topics=5, chunksize=10000, passes=1, iterations=70)
	# lda = gensim.models.ldamulticore.LdaMulticore.load("/Users/joshualiu/dev/tmp/lda_model")
	# doc_lda = lda[test_corpus]
	# logging.info(doc_lda)
	# lda.save(sys.argv[3])
	# lda.print_topics(3)
