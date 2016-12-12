
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression

if __name__ == '__main__':
	conf = SparkConf().setMaster('local')
	conf.set("spark.sql.warehouse.dir", "E:/spark-warehouse/")
	spark = SparkSession.builder.appName('2.0 ml demo').config(conf=conf).getOrCreate()
	df = spark.read.csv(r'E:\git\ml-20m\ml-20m\genome-tags.csv', header=True, inferSchema=True)
	lr = LogisticRegression(maxIter=10, regParam=0.01)
	pipeline = Pipeline(stages=[lr])
	model = pipeline.fit(df)
	test = spark.createDataFrame([
    (1, 9),
    (2, 10),
    (3, 11),
    (4, 12)], ["id", "tagId"])
	prediction = model.transform(test)
	selected = prediction.select("id", "tagId", "prediction")
	for row in selected.collect():
		print(row)
