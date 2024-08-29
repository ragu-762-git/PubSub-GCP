This project demonstrates how PubSub is used as a logical glue that loosely couple different services together either in synchronous or asynchronous workflows.

# Description:
We are hosting an imaginary website that allows users to upload images and we want to create a thumbnail image, everytime they do so. The initial image gets written 
to a GCS bucket. This triggers a notification in the form of a message that gets published to our notification topic. We then have a cloud function, which receives a 
push notification from our topic. The cloud function will fire up and create a thumbnail image and writes it to other GCS bucket. This form loose coupling allows us to separate 
the generation of thumbnail images from our main application. So the web performance is not reducing while this takes place. Processing image is more compute intensive than 
the rest of our applicaiton. So, its great that we can scale this component up and down through cloud functions, while using PubSub to join everything together. 


# important points:
I have created the notification configuration for my images bucket using gsutil on the CLI. i.e when a file hits a bkt, a notification (msg) in form of JSON payload 
should be published to the specified pubsub topic
command - (gsutil notification create -f json -e OBJECT_FINALIZE -t projects/projectname/topics/topicname gs://bkt-name)
