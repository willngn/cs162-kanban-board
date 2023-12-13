# Set Docker environment to Minikube's Docker daemon
echo "Setting Docker environment to Minikube's Docker daemon..."
eval $(minikube docker-env)

# Build the Docker image
echo "Building Docker image..."
docker build -t kanban .

# Apply the Kubernetes configurations
echo "Applying Kubernetes deployments and services..."
kubectl apply -f postgres_persistent.yaml
kubectl apply -f postgres_deployment.yaml
sleep 10
kubectl apply -f kanban_deployment.yaml
sleep 10

echo "Setup complete!"