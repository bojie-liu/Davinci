#!/usr/bin/python env
# -*- coding: utf-8 -*-

"""
Description:
"""

__author__ = "joshliu"

import os
import logging
import logging.config


def get_logger(logger_name):
	_current_dir = os.path.dirname(os.path.realpath(__file__))
	logging.config.fileConfig(_current_dir + "/logging.conf")
	return logging.getLogger(logger_name)

#deprecated
_verbose = True

def i(msg):
	if _verbose == True:
		print(msg)
	return

if __name__ == "__main__":
	logger = get_logger("root")
	logger.info("hello")
