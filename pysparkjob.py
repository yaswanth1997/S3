
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window


spark = SparkSession.builder.appName("CarPricesAnalysis").getOrCreate()

#loading the dataset from s3
data_uri = "s3://your-bucket-name/prices_clean.csv"
df = spark.read.csv(data_uri, header=True, inferSchema=True)

# Get the models in every make with the highest price.
d1_result = df.groupBy("Make").agg(F.max("Price").alias("MaxPrice")) \
    .join(df, ["Make", "Price"], "inner") \
    .select("Make", "Model", "MaxPrice")

# Get the models in every make every year with the highest price.
window_spec = Window.partitionBy("Make", "Year").orderBy(F.desc("Price"))
d2_result = df.withColumn("rank", F.row_number().over(window_spec)) \
    .filter(F.col("rank") == 1).drop("rank")

# Get the models whose price is greater than the average price by make.
avg_prices = df.groupBy("Make").agg(F.avg("Price").alias("AvgPrice"))
d3_result = df.join(avg_prices, "Make", "inner") \
    .filter(F.col("Price") > F.col("AvgPrice")) \
    .select("Make", "Model", "Price", "AvgPrice")

# Get the number of models released by each maker.
d4_result = df.groupBy("Make").agg(F.countDistinct("Model").alias("NumModels"))

# Show or collect the results
d1_result.show()
d2_result.show()
d3_result.show()
d4_result.show()
