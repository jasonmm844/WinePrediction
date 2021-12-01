# WinePrediction
On EC2 instance:
  Ports 80 must be open for Docker later
  CLI must be copied into /home/ec2-user/.aws/credentials
  use `pip3 install flintrock` to install flintrock to create spark clusters
  `flintrock configure` to create configuration file
  us editor to modify ~/.config/flintrock/config.yaml
    edit ...
    edit ...
    edit number of slaves to 3  
  flintrock launch <cluster name>
  
  `wget  https://dlcdn.apache.org/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz` to download spark tarball
  `tar xzvf spark-3.2.0=bin-hadoop3.2.tgz`
  change to spark directory
  `export SPARK_HOME=`pwd``
  `export PYTHONPATH=$(ZIPS=("$SPARK_HOME"/python/lib/*.zip); IFS=:; echo "${ZIPS[*]}"):$PYTHONPATH`
  
  In order to run winetraining.py with spark use:
    `spark-3.2.0-bin-hadoop3.2/bin/spark-submit  --master local[4] winetraining.py <dataset to train> <saved model name>`
  
  In order to run wineprediction.py with 1 spark machine use:
    `spark-3.2.0-bin-hadoop3.2/bin/spark-submit  --master local wineprediction.py <testing dataset> <model to load>`
  
  
  To install docker use:
    `sudo amazon-linux-extras install docker`
    `sudo service docker start`
    `sudo usermod -a -G docker ec2-user` so ec2-user has privileges for running docker
   
  
