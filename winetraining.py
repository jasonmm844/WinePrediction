# Jason Martin
# CS643-851
# December 1, 2021
# Wine Quality Parallel Model Training


from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
import pandas as pd
import numpy
import sys

# Full path to training dataset
if len(sys.argv) < 3:
    print("Usage: wineprediction.py <csv dataset> <model to save>")
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
df_2 = assembler.transform(df)
df_2.show()

# Create training set create linear regression model, and train the model for quality prediction
lr = LinearRegression(featuresCol="features",labelCol=df.columns[-1])
model = lr.fit(df_2)

# Save model for docker image to load
model.save(sys.argv[2])
