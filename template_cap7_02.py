from pyspark.sql import SparkSession

class SparkApplication:

    def __init__(self, spark_session):

        self.spark = spark_session

    def read_data(self) : 

        self.df = (
            self.spark
            .read
            .format('parquet')
            .load('path/to/file')
        )

    def data_processing(self) :

        self.df_final = (
            self.df
            .groupby('string_col')
            .agg(f.sum('num_col1').alias('num_col1'),
                f.mean('num_col2').alias('num_col2')
                )
        )

    def write_data(self) :
        (
            self.df_final
            .write
            .format('parquet')
            .save('destination/file')
        )

    def run(self) : 

        self.read_data()
        self.data_processing()
        self.write_data()
    
    if __name__ == "__main__" : 

        spark = (
            SparkSession
            .builder
            .config('serializer','org.apache.spark.serializer.KryoSerializer')
            .getOrCreate()
        )

        spark_app = SparkApplication(spark)
        spark_app.run()