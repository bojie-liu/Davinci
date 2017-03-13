#!/usr/bin/python env
# -*- coding: utf-8 -*-

"""
Description:
"""

__author__ = "joshliu"

import logging
import gensim.corpora
import gensim.models

if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO)

	# lda = gensim.models.ldamulticore.LdaMulticore(corpus=corpus.corpus(), id2word=corpus.dictionary(), num_topics=100, chunksize=10000, passes=1)
	# lda = gensim.models.ldamulticore.LdaMulticore.load("/Users/joshualiu/dev/tmp/lda_model")
	# doc_lda = lda[test_corpus]
	# logging.info(doc_lda)
	# lda.print_topics(20)
