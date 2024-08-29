# Simple-Pub-Sub-operation-using-Compute-Engines-in-GCP
This folder describes a basic pub/sub operation such as publishing messages to a topic from a python application running in one Compute engine (publisher) to another python application running in other compute engine instance (subscriber) using Pub/Sub Client API library.

# Note:
Whenever we create a new Compute Engine instance (n1-standard - 3GB RAM and 1CPU-OS-Linux_debian) and use python to interact with any GCP services through Client API libraries, follow the below steps in SSH terminal:
1. update the VM - (sudo apt-get update)
2. Make sure python installed - (python --version)
3. create a virtual python environment"

   3.a. Install the virtual environment package - (sudo apt install python3.11-venv)

   3.b. create the virtual env - (python3 -m venv myenv)

   3.c. activate the virtual env - (source myenv/bin/activate)

5. Now install the pip - (sudo apt-get install python3-pip)
6. install the required gcp client libraries ; for example - (pip install google-cloud-pubsub)
   
**In this basic operations in pubsub, we have created 2 compute engines, one as publisher and other as subscriber. We have to set up the above environment in both engines which are running the python application.**
