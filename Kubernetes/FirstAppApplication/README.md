## **Section 1: Create Image**

#### **Active Cloud Shell on GCP**

![My Image](./image/console.png)
![My Image](./image/shell.png)
 
#### **Determine zone support for Intel Haswell Platform**
```
$ gcloud compute zones describe us-west1-b
```
![My Image](./image/zonedetail.png)

#### **reate a staging disk**
```
$ gcloud compute disks create stagingdisk --image-project ubuntu-os-cloud --image-family ubuntu-2004-lts --zone us-west1-b
```
![My Image](./image/disk.png)

*Note: https://cloud.google.com/compute/docs/images/os-details  
Check Ubuntu LTS Image configuration*
![My Image](./image/config.png)
 
#### **Create a nested VM**
```
$ gcloud compute images create nested-vm-image --source-disk=stagingdisk --source-disk-zone=us-west1-b --licenses=https://www.googleapis.com/compute/v1/projects/vm-options/global/licenses/enable-vmx
```
![My Image](./image/nested.png)

 
#### **Delete the source disk we created temporarily as a staging disk**
```
$ gcloud compute disks delete stagingdisk --zone us-west1-b
```
![My Image](./image/deletedisk.png)
 
#### **Create Image**
```
$ gcloud compute instances create nested-vm-image1 --zone us-west1-b --min-cpu-platform "Intel Haswell" --machine-type n1-standard-4 --image nested-vm-image
``` 
![My Image](./image/createimage.png)

#### **Verify VM in Console**
![My Image](./image/verifyimage.png) 


#### **Connect to VM**
![My Image](./image/connectVM1.png) 
![My Image](./image/connectVM2.png)  

#### **Verify the VM is online**
```
$ grep -cw vmx /proc/cpuinfo
```
![My Image](./image/verifyonline.png) 


## **Section 2: Install tools**

## *Install kubectl binary with curl*
[Kubectl Information Page](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/ )


#### **Download the latest release with the command:**
```
$ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" 
```
![My Image](./image/kubectldownload.png) 
 
#### **Validate the binary (optional)**
```
$ curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
$ echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
```
![My Image](./image/kubectlvalidate.png)
![My Image](./image/kubectlvalidate1.png)

#### **Install kubectl**
```
$ sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```
![My Image](./image/kubectlinstall.png)
 
#### **Test to ensure the version you installed is up-to-date:**
```
$ kubectl version --client
```
![My Image](./image/kubectlcheck1.png)
or
```
$ kubectl version --client --output=yaml    
```
![My Image](./image/kubectlcheck2.png)
 
## *Install Minikube*
[Minikube Information Page](https://minikube.sigs.k8s.io/docs/start/ )

#### **Install package**
```
$ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
$ sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
![My Image](./image/minikubeinstall.png)
 
#### **Move minikube**
```
$ sudo cp minikube /usr/bin/
```
![My Image](./image/minikubemove.png)

## *Install Docker*
#### **Install VirtualBox and extension package**
```
$ sudo apt-get install curl wget apt-transport-https virtualbox virtualbox-ext-pack -y
``` 
![My Image](./image/dockerinstall.png)

#### **Install docker.io**
```
$ sudo apt-get install docker.io
```
![My Image](./image/dockerinstall1.png)
 
#### **Verify**
```
$ docker --version
```
![My Image](./image/dockercheck.png)
 
## **Section 3: Prepare Application**

#### **Start Docker and Install Conntrack**
```
$ sudo service docker start
$ sudo apt-get install conntrack
``` 
![My Image](./image/dockerstart.png)
![My Image](./image/conntrackinstall.png)

#### **Start Minikube**
```
$ cd /usr/bin
$ minikube start
```
![My Image](./image/minikubestart.png)
 
#### **Creating files**

* Making a project folder
    ```
    $ mkdir dockerImg
    $ cd dockerImg
    ```
    ![My Image](./image/directory.png)
 
* `$ vi app.js`
    ```
    const http = require('http');
    const os = require('os');

    console.log("Kubia server starting...");

    var handler = function(request, response) {
            console.log("Received request from "+ request.connection.remoteAddress);
            response.writeHead(200);
            response.end("You've hit " + os.hostname() + "\n");
    };

    var www = http.createServer(handler);

    www.listen(8080);
    ```
    ![My Image](./image/app.png)
 

* `$vi Dockerfile`
    ```
    FROM node:7
    ADD app.js /app.js
    ENTRYPOINT [“node”, “app.js”]
    ```
    ![My Image](./image/dockerfile.png)
 

#### **Build docker image**
```
$ sudo docker build -t kubia .
```
![My Image](./image/kubectlcheck1.png)


#### **Run image on a container on localhost**
```
$ sudo docker run --name kubia-container -p 8080:8080 -d kubia
```

#### **Create Account at https://hub.docker.com/ and Login**
 
``` 
$ sudo docker login
```
*Note: create repository in console*

#### **Push Tag to Docker Hub Repository**
```
$ sudo docker tag kubia sharoncao0920/kubernetes_2023:kubia
$ sudo docker push sharoncao0920/kubernetes_2023:kubia  
```
 

## **Section 4: Run Application on Kubernetes**

### **Minikube**

* Get cluster information
    ```
    $ kubectl cluster-info
    ``` 

* ` $vi kubia_rc.yaml`
    ```
    apiVersion: v1
    kind: ReplicationController
    metadata:
    name: kubia
    spec:
    replicas: 3
    selector:
        app: kubia
    template:
        metadata:
        name: kubia
        labels:
            app: kubia
        spec:
        containers:
        - name: kubia-container
            image: sharoncao0920/kebernetes_2023
            ports:
            - containerPort: 8080
    ``` 

* Apply yaml file
    ```
    $ kubectl apply -f kubia-rc.yaml
    ```


* Run image
    ```
    $ sudo docker run -p 8080:8080 -d sharoncao0920/kubernetes_2023
    $ kubectl run kubia --image=sharoncao0920/kubernetes_2023 --port=8080
    ``` 


* Get pods information
    ```
    $ kubectl get pods
    ``` 
    *Note: it may take time to get all pods ready, re-run the command to get updated status*
 

* Start tunnel
    ```
    $ minikube tunnel
    ```

* Open another terminal and expose a service
    ```
    $ kubectl expose pod kubia --type=LoadBalancer --port 8080
    ```

* List services
    ```
    $ kubectl get svc
    ```

* Verify the service is reachable
    ```
    $ curl 10.103.29.158:8080
    ```
 



* Other commands maybe useful

    Show images information on Docker `$ sudo docker images`

    Replication controller information `$ kubectl describe replicationcontrollers/kubia`










GKE

$ gcloud container clusters create kubia --num-nodes=1 --machine-type=e2-micro --region=us-west1

 
Enable Kubernetes API on GCP 
 
 
$ gcloud container clusters create kubia --num-nodes=1 --machine-type=e2-micro --region=us-west1
 
$ kubectl get nodes
 


