#!/usr/bin/python env
# -*- coding: utf-8 -*-

"""
Description:
"""

from __future__ import absolute_import

__author__ = "joshliu"


import sys
import logging
import gensim.corpora
import gensim.models
from train_corpus import MMCorpus
import datetime

def test_lda(lda_model_path, input_corpus):
	# corpus = gensim.corpora.MmCorpus(input_corpus)
	corpus = MMCorpus(input_corpus, '/Users/joshualiu/dev/data/tushare/tushare_dict')
	lda_model = gensim.models.ldamulticore.LdaMulticore.load(lda_model_path)
	test_corpus = gensim.corpora.MmCorpus('/Users/joshualiu/dev/data/tushare/tushare_corpus2')
	cm = gensim.models.coherencemodel.CoherenceModel(model=lda_model, corpus=test_corpus, coherence='u_mass')  # tm is the trained topic model
	test = cm.get_coherence()
	diction = gensim.corpora.Dictionary.load('/Users/joshualiu/dev/data/tushare/tushare_dict')
	word_id = diction.doc2bow(['下跌'])
	test = lda_model.print_topic(1, 30)
	test = lda_model.get_term_topics('负面', minimum_probability=0.0001)
	lda_model.print_topics()
	print('load finish')
	doc_lda = lda_model[corpus.doc_bow()]
	print(doc_lda)
	# doc_lda.print_topic(3)
	pass

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)

	# if len(sys.argv) != 3:
	# 	logging.error('python3 lda_demo.py $input_lda $input_corpus')
	# 	exit(-1)

	test_lda('/Users/joshualiu/dev/data/tushare/tushare_ldamodel25', '/Users/joshualiu/dev/data/tushare/tushare_seq_test')
