# Download Service

Microservice for interaction with dummy-pdf-or-png service.

## Build

To build it for production purposes, push the code to git repo, and Github Actions will build the code.

For local env use the command below.

```bash
make build
```

## Run

### Development

For development purpose it runs on Docker.

```bash
make up
```

### Production

To build it for production purposes, push the code to git repo, and Github Actions will build the code.

## Running

The production environment proposal is based on a Minikube instance.

**Create namespace first.**

kubectl apply -f ./sre/infrastructure/kubernetes/namespace.yaml

**Create all resources then.**

kubectl apply -f ./sre/infrastructure/kubernetes -n visma

## Requirements

- make
- docker
- minikube


## Considerations
In a first iteration, I had chosen to do the step 1 and 3 of the hiring assignment. For step 1, I have experience with microservices and APIs and even though I am still recent to GO (I only know and worked on-and-off with it for a year and I have never done an API with it) I wanted to develop the service in this language, so I could learn more about it, while trying my best to ensure clean code practices — e.g I learned about Gorilla mux for HTTP routing and HttpTest for mocking HTTP requests. 

As for step 3, I have worked with Make, Dockerfile and Helm charts (more with the last one) and I knew I wanted to have that, at least to demonstrate the skills I learned (and am constantly learning) about Docker and Helm. Additionally, I have never worked with CI/CD and GCP as a developer/maintainer, but I wanted to challenge myself and show to the team that I am not scared of a challenge and that I will always try my best to learn and put what I am learning into practice. For CI/CD after some research I decided to use GitHub actions and GCP (because I know it is the provider the team works with and why not learn more about it and try something new?).

As an additional step, I decided to provide the necessary configuration to set up a Prometheus and a Blackbox exporter, so we can query the metrics via Prometheus UI and perform Health checks to the Document keeper service, respectively.

After having done all the aforementioned, because I was even more motivated due to the fact that I had managed to put the CI/CD pipeline working and the services running in GKE I decided to just go for it and attempt the step 2.
For step 2, I used Terraform and the material mentioned in the section "Learning resources" to set up and automate the creation/management of the infrastructure of Document keeper. This step still needs some improvements as mentioned in the "Improvements list" section, and it would be where I would focus more if I had more time for the assignment.

## Improvements list
In this section, I will be listing the improvements I would like to perform on this assignment:

1) Define a way to install the helm charts of both Document keeper and Dummy PDF or PNG via helm install and then have a control flow that would allow it to install the charts in a first run and then update them on subsequent runs. Additionally, also apply the control flow to the Prometheus and Blackbox charts.

2) Find a way to install the VPA CRDs in order to be able to deploy the defined VPA's.

3) Fix the permission errors when trying to pull the service images in the new GKE cluster, created via Terraform.

4) Define a release strategy for the images with version management.

## Feedback
Feedback on improvement points, tips to implement the improvement list or just new ideas that can make this service better, more reliable, secure and performative are always welcome and will be discussed and iterated upon. Therefore, feel free to reach out to me either on the CNCF Slack channel or via LinkedIn. :) 

## Maintainers
| name            | Slack            | Channel                            |
|-----------------|------------------|------------------------------------|
| Rita Canavarro  | @rita.canavarro  | Cloud Native Computing foundations |


## Learning resources

Terraform in 15 min - https://www.youtube.com/watch?v=l5k1ai_GBDE

GitHub Actions Tutorial - Basic Concepts and CI/CD Pipeline with Docker - https://www.youtube.com/watch?v=R8_veQiYBjI

GitHub Actions to GCP https://docs.github.com/en/actions/deployment/deploying-to-your-cloud-provider/deploying-to-google-kubernetes-engine

Blackbox exporter https://medium.com/cloud-native-daily/blackbox-exporter-to-probe-or-not-to-probe-57a7a495534b

GCP Terraform tutorial https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/google-cloud-platform-change

GCP Terraform registry https://registry.terraform.io/providers/hashicorp/google/latest

CPU - https://home.robusta.dev/blog/stop-using-cpu-limits