# Jason Martin
# CS643-851
# December 1, 2021
# Prediction Testing for Wine Quality


from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.regression import LinearRegression
from pyspark.ml.regression import LinearRegressionModel
from pyspark.ml.feature import VectorAssembler
from pyspark.mllib.evaluation import RegressionMetrics
import pandas as pd
import numpy
import sys

# Full path to training dataset
if len(sys.argv) < 3:
    print("Usage: wineprediction.py <csv dataset> <model name> [-v]")
    sys.exit(-1)

csvpath = sys.argv[1]

# Get spark context/session
sc= SparkContext()
sqlContext = SQLContext(sc)
sc.setLogLevel("OFF")

# Read in csv file
df = sqlContext.read.option("delimiter",";").csv(csvpath, header=True, inferSchema=True)

# Assemble columns together with a features column to prepare data
feature_columns = df.columns[:-1]
assembler = VectorAssembler(inputCols=feature_columns,outputCol="features")
test = assembler.transform(df)
if len(sys.argv) == 4 and sys.argv[3] == '-v':
    test.show()

model = LinearRegressionModel.load(sys.argv[2])

# Gather summary of the model evaluation to acquire mean absolute error, root mean squared error, and root squared for a regression model
eval_sum = model.evaluate(test)
print("Mean Absolute Error:" + str(eval_sum.meanAbsoluteError))
print("Root Mean Squared Error: " + str(eval_sum.rootMeanSquaredError))
print("R Squared: " + str(eval_sum.r2))

# Predict the output for the data for the quality of the wine
predictions = model.transform(test)
if len(sys.argv) == 4 and sys.argv[3] == '-v':
    predictions.select(predictions.columns[11:]).show()
