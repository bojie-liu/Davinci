
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import isnan
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder

if __name__ == '__main__':
	conf = SparkConf().setMaster('local')
	conf.set("spark.sql.warehouse.dir", "E:/spark-warehouse/")
	spark = SparkSession.builder.appName('2.0 ml demo').config(conf=conf).getOrCreate()
	df = spark.read.csv(r'E:\working git\ml-20m\ml-20m\ratings.csv', header=True, inferSchema=True)
	result = []

	for reg in [0.05, 0.1]:
		for rank_param in [20]:
			(training, test) = df.randomSplit([0.8, 0.2])
			als = ALS(maxIter=5, regParam=reg, rank=rank_param, userCol="userId", itemCol="movieId", ratingCol="rating")
			pipeline = Pipeline(stages=[als])
			model = pipeline.fit(training)

			# paramGrid = ParamGridBuilder() \
			# 	.addGrid(als.rank, [10]) \
			# 	.build()

			# training_withoutNAN = training.filter(isnan(training.rating) == False)
			# crossval = CrossValidator(estimator=pipeline,
			# 							estimatorParamMaps=paramGrid,
			# 							evaluator=RegressionEvaluator,
			# 							numFolds=5)

			# model = crossval.fit(training_withoutNAN)
			predictions = model.transform(test)
			predictions_withoutNAN = predictions.filter(isnan(predictions.prediction) == False)
			evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
			rmse = evaluator.evaluate(predictions_withoutNAN)
			result.append((reg, rank_param, rmse))

print(result)