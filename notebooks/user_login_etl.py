# Databricks ETL Notebook
# Loading the json file into spark.
df = spark.read.option("multiline", "true").json("/Volumes/workspace/default/raw_data/user_activity_data.json")
display(df)

# Checking all the schemas.
df.printSchema()

# Cleaning the data. Dropping the duplicate entries and saving the new table.
df_clean = df.dropDuplicates()  
display(df_clean) 
df_clean.write.mode("error").saveAsTable("usr_activity_cleaned_data")

# Show spark tables
spark.sql("SHOW TABLES").show()

# Describe new table
spark.sql("DESCRIBE TABLE usr_activity_cleaned_data").show(truncate=False)
