# Monitoring-Stack
# Basic Architecture 
Step 1: Ready the data container generating the logs and build the image
- Add all the files from the log_generating_container to the same directory 
- Add an empty folder called "logg" 
- Use the following command to create an image for the application that will be run in a container later\
docker build --tag loggeneration .

Step 2: Initialize the ElasticSearch container 
- Use the following command to initialise the container and start listening at port 9200 for incoming logs\
docker run -p 9200:9200  -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.4.3

Step 3: Initialise the Fluentd container 
- Step 3(a):
  - Add the Dockerfile of the Custom Fluentd image that includes the ElasticSearch Plugin and a folder called conf_files with the config file 'in_docker.conf' within, to the same directory
  - Use the following command to build the Custom Fluentd image\
  docker build --tag custom-fluentd .
- Step 3 (b):
  - Use the following command to initialise the Fluentd container and create an instance of Fluentd (to listen for logs and push them to ElasticSearch)\
  Note: This is the Unified Logging Layer\
  docker run -p 24224:24224 -p 24224:24224/udp -v ~/info_cont:/fluentd/log custom-fluentd -c /fluentd/log/conf_files/in_docker.conf\

Step 4: Initialise the log generating container 
- Use the following command to initialise the container\
docker run --log-driver=fluentd --log-opt tag="docker.{{.ID}}" --log-opt fluentd-address=[HOST_IP_ADDRESS]:24224 loggeneration
