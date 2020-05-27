# Iris classifier with Random forest
## Steps to be followed:

#### Build Docker image
    $ docker build -t iris_rf:0.0.1 .
 
### Start the seldon-core model
    $ docker run --env-file dev.properties -p 30001:5000 -it iris_rf:0.0.1

### test the seldon-core model locally
    $  curl  -s http://localhost:30001/predict -H "Content-Type: application/json" -d '{"data":{"ndarray":[[5.964,4.006,1.081,1.031],[5.964,4.006,0.081,0.031]]}}'
    
### Deploy in k8x cluster
    $ kubectl apply -f deployment/dep.yaml 

### Expose to the outer world with ingress 
    $ kubectl apply -f deployment/ingress.yaml
### Test the deployment 
    $ curl  -s seldon-iris-rf-example-classifier:9090/predict -H "Content-Type: application/json" -d '{"data":{"ndarray":[[5.964,4.006,1.081,1.031],[5.964,4.006,0.081,0.031]]}}'