
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import isnan

if __name__ == '__main__':
	conf = SparkConf().setMaster('local')
	conf.set("spark.sql.warehouse.dir", "E:/spark-warehouse/")
	spark = SparkSession.builder.appName('2.0 ml demo').config(conf=conf).getOrCreate()
	df = spark.read.csv(r'E:\working git\ml-20m\ml-20m\ratings.csv', header=True, inferSchema=True)
	(training, test) = df.randomSplit([0.8, 0.2])
	als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating")
	model = als.fit(training)

	predictions = model.transform(test)
	predictions_withoutNAN = predictions.filter(isnan(predictions.prediction) == False)
	evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
	rmse = evaluator.evaluate(predictions_withoutNAN)
	print("rmse = " + str(rmse))