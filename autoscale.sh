kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

minikube addons enable metrics-server

kubectl autoscale deployment kanban-deployment --cpu-percent=50 --min=1 --max=10               

kubectl get hpa kanban-deployment --watch