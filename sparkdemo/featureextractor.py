from pyspark.ml.feature import HashingTF, IDF, Tokenizer
from pyspark import SparkConf
from pyspark.sql import SparkSession

def TFIDF_demo():
	sentenceData = spark.createDataFrame([
	    (0, "Hi I heard about Spark"),
	    (0, "I I I I I wish Java could use case classes"),
	    (1, "Logistic regression models are neat")
	], ["label", "sentence"])
	tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
	wordsData = tokenizer.transform(sentenceData)
	hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=32)
	featurizedData = hashingTF.transform(wordsData)
	# alternatively, CountVectorizer can also be used to get term frequency vectors

	idf = IDF(inputCol="rawFeatures", outputCol="features")
	idfModel = idf.fit(featurizedData)
	rescaledData = idfModel.transform(featurizedData)
	for features_label in rescaledData.select("features", "label").take(3):
	    print(features_label)

def word2vec_demo:
	

if __name__ == "__main__":
	conf = SparkConf().setMaster("local").set("spark.sql.warehouse.dir", "E:/spark-warehouse/")
	spark = SparkSession.builder.appName('2.0 ml demo').config(conf=conf).getOrCreate()
