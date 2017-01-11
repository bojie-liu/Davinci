from pyspark.ml.classification import LogisticRegression, GBTClassifier

class ClassifierFactory(object):
    def __init__(self):
        pass

    def create(type, input_col="input", output_col="output", *args):
        if type == "LR":
            return LogisticRegression(labelCol=input_col, featuresCol=output_col, maxIter=10, regParam=0.3, elasticNetParam=0.8)
        elif type == "GBT":
            return GBTClassifier(labelCol=input_col, featuresCol=output_col, maxIter=10)
        else:
            print("Invalid classifier type")
