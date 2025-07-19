# Things to do

- Optimise Docker container size. *One way to achieve this could be customising the requirements.txt file for each container.*
- Improve the backend performance. *Mostly on the DB side, by optimising queries and considering creating indexes and partitioning tables.*
- Improve data ingestion ETL. *Maybe reducing the number of files to upload.*
- More endpoints could be implemented allowing for more dataset coverage.
- OR, some tables could be dropped from the ingestion pipeline to just load the needed data tables for the existing endpoints.