# colorMixingApp
This is a simple webapp to mix two given colors based on median rgb values. At this time, I am focussing on deploying the webapp in a Kubernetes cluster.

Technologies to be used:
* HTML with Javascript for frontend
* Python Flask framework for Backend
* nginx for load balancing, port-forwarding
* openssl for generating self-signed certificates
* PostgreSQL database (if required, as the site grows)
* docker for containerizing webapp
* Azure for cloud infrastructure
* Azure container registry to store docker images
* Azure Kubernetes cluster (AKS)

## Backend logic
* Ask user to select two colors from dropdown.
* Convert each of the two colors into rgb components. At this time, rgb values of all colors in the dropdown are stored in a json file.
* For each of the RGB values, get the median value of R, G & B.
* Convert the median RGB into hex and display on the webpage as the 'Resultant color'.


### Building a docker image
cd to the directory containing the Dockerfile. In this case, case/cicd/performance_testing/collect_time. Then run the below command to build an image
```bash
docker build -t color_mixing_webapp:latest .
# This returns a docker image id.
```

Running a docker container from the above docker image:
```bash
docker run -d -p 5000:5000 --name color_mixing_webapp --restart always color_mixing_webapp:latest
```
'-p' option binds port 5000 to port 5000 of Docker container. Note, the C++ programs are sending the HTTP requests to port 14373.

'color_mixing_webapp' is the name given to the running container.

'--restart always' ensures the container restarts automatically when interrupted (like a server reboot).


To get into the container environment:
```bash
docker exec -it color_mixing_webapp /bin/bash
```