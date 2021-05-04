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