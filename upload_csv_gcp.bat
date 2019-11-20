:: This batch file upload csv files to gcp cloud storage TCCproject
ECHO OFF
cd C:/Users/Robert/AppData/Local/Google/Cloud SDK
call gsutil cp C:/TCC/file_upload/data_raw* gs://tccbucket
timeout 3
