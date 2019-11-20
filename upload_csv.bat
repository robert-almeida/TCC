:: This batch file upload csv files to AWS S3
ECHO OFF
cd C:\TCC\file_upload
$ aws s3 cp C:\TCC\file_upload\data_raw.csv s3://buckettcc/
timeout 3


