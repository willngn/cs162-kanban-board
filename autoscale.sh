# Bring metrics-server into Kubernetes
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# enable the metrics-server addon
minikube addons enable metrics-server

# Activate the auto-scaling behavior given CPU threshold of 50%, 1 minimum pod and at max 10
kubectl autoscale deployment kanban-deployment --cpu-percent=50 --min=1 --max=10               

# Observe how the app auto-scales
kubectl get hpa kanban-deployment --watch