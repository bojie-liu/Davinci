from pyspark.ml.feature import HashingTF, IDF, Tokenizer, Word2Vec, ChiSqSelector
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

	selector = ChiSqSelector(numTopFeatures=2, featuresCol="features",
                         outputCol="selectedFeatures", labelCol="label")
	selected_result = selector.fit(rescaledData).transform(rescaledData)
	for features_label in selected_result.select("features", "selectedFeatures").take(3):
	    print(features_label)
	# for features_label in rescaledData.select("features", "label").take(3):
	#     print(features_label)

def word2vec_demo():
	# Input data: Each row is a bag of words from a sentence or document.
	documentDF = spark.createDataFrame([
	    ("Hi I heard about Spark".split(" "), ),
	    ("I wish Java could use case classes".split(" "), ),
	    ("Logistic regression models are neat".split(" "), )
	], ["text"])
	# Learn a mapping from words to Vectors.
	word2Vec = Word2Vec(vectorSize=3, minCount=0, inputCol="text", outputCol="result")
	model = word2Vec.fit(documentDF)
	result = model.transform(documentDF)

	for feature in result.select("result").take(3):
	    print(feature)

if __name__ == "__main__":
	conf = SparkConf().setMaster("local").set("spark.sql.warehouse.dir", "E:/spark-warehouse/")
	spark = SparkSession.builder.appName('2.0 ml demo').config(conf=conf).getOrCreate()
	TFIDF_demo()