
import os
import config
from utils import log

from pyspark import SparkConf, SparkContext

if __name__ == "__main__":
	log.e(os.sys.path)
	conf = SparkConf().setMaster("local").setAppName("main")
	sc = SparkContext(conf = conf)
	log.e(sc)
