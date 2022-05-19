CREATE EXTERNAL TABLE santander_analytics (
   full_text string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
LOCATION '/twitter/santander_analytics/';