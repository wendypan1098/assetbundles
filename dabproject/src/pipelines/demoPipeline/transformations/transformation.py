import dlt

@dlt.table
def transformation():
    return spark.range(10)
