
from __future__ import absolute_import


import os
import conf.config
from utils import log

print(os.sys.path)

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

if __name__ == "__main__":
	path = '/Users/joshualiu/dev/tmp/tushare_news5.json'
	# log.e(os.sys.path)
	conf = SparkConf().setMaster('local')
	conf.set("spark.sql.warehouse.dir", "/Users/joshualiu/dev/tmp/spark-warehouse/")
	spark = SparkSession.builder.appName('2.0 ml demo').config(conf=conf).getOrCreate()
	# sc = SparkContext(conf = conf)
	# testrdd = spark.sparkContext.textFile(path)
	# print(testrdd)
	testdf = spark.read.json(path)
	testdf.show(n=5, truncate=False)
	print(testdf.select('title').collect())
	# log.e(sc)
