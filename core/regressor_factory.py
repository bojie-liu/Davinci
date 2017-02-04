from pyspark.ml.regression import GBTRegressor, RandomForestRegressor

class RegressorFactory(object):
    def __init__(self):
        pass

    def create(regressor_type, input_col="input", output_col="output", *args):
        if regressor_type == "GBT":
            return GBTRegressor(labelCol=input_col, featuresCol=output_col, maxIter=10)
        elif regressor_type == "RF":
            return RandomForestRegressor(labelCol=input_col, featuresCol=output_col)
        else:
            print("Invalid regressor type")

