#!/bin/bash

# Choose environment: dev or acceptance
ENV=${1:-dev}
BRANCH=$(git rev-parse --abbrev-ref HEAD | sed 's|/|-|g')   # replaces / with -
IMAGE_TAG="mydockerhub/simple-interest-calculator:$ENV-$BRANCH"

echo "Building Docker image $IMAGE_TAG..."
docker build -t $IMAGE_TAG .

echo "Pushing Docker image..."
docker push $IMAGE_TAG

echo "Deploying to Kubernetes..."
kubectl delete deployment simple-interest-calculator --ignore-not-found
sed -i "s|image:.*|image: $IMAGE_TAG|" deployment.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
