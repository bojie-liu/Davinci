from pyspark.ml import Pipeline
from pyspark.ml.feature import Word2Vec, HashingTF, IDF

class FeatureFactory(object):
	def __init__(self):
		pass
	
	def create(type, input_col="input", output_col="output", **args):
		if type == "word2vec":
			return Word2Vec(vectorSize=3, minCount=0, inputCol=input_col, outputCol=output_col)
		elif type == "TF-IDF":
			hashingTF = HashingTF(inputCol=input_col, outputCol="rawFeatures", numFeatures=32)
			idf = IDF(inputCol="rawFeatures", outputCol=output_col)
			pipeline = Pipeline(stage=[hashingTF, idf])
			return pipeline
        elif type == "StringIndexer":
            return
		else:
			print("Invalid feature type!")

