# Run the select-reviews.yaml NoSqlBench script. 
#  - 10,000 cycles
#  - 20 threads

username=<your-clientId-goes-here>
password=<your-password-goes-here>
secureconnectbundle=/home/gcross/secure-connect-cassio-db.zip

echo Starting the NoSqlBench script
./nb5 run driver=cqld4 workload=select-reviews cycles=10000 threads=20 username=$username password=$password secureconnectbundle=$secureconnectbundle --progress console:10s --report-csv-to metrics
