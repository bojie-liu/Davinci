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
import gensim.summarization.summarizer


if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)

	lda_model_path = '/Users/joshualiu/dev/data/tushare/tushare_ldamodel5'
	test_corpus = ['涨', '涨']
	# diction = gensim.corpora.Dictionary.load('/Users/joshualiu/dev/data/tushare/tushare_dict')
	# test_bow = diction.doc2bow(test_corpus)
	lda_model = gensim.models.ldamulticore.LdaMulticore.load(lda_model_path)
	test = lda_model.get_term_topics('负面', minimum_probability=0.001)
	pass