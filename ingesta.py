import boto3
import pymysql
import pandas as pd

# Conexión a la base de datos MySQL
conexion = pymysql.connect(
    host="mysql_c",        
    user="root",
    password="utec",
    database="test"        
)

# Leer registros de la tabla "employees"
df = pd.read_sql("SELECT * FROM employees", conexion)
df.to_csv("data.csv", index=False)
conexion.close()

# Subir archivo CSV a S3
ficheroUpload = "data.csv"
nombreBucket = "gcr-output-01"

s3 = boto3.client('s3')
s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)

print("Ingesta completada desde MySQL")
