# Delete the Kubernetes deployment and service
echo "Deleting Kubernetes deployment and service..."

# get these deployments and services out of Kubernetes
kubectl delete -f postgres_persistent.yaml
kubectl delete -f postgres_deployment.yaml
kubectl delete -f kanban_deployment.yaml

# Optionally: Clean up Docker images
# This step is optional and depends on whether you want to remove the Docker image as well
# echo "Removing Docker image..."
# docker rmi my-flask-app:latest

echo "Teardown complete!"