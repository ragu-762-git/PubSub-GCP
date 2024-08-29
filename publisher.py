from google.cloud import pubsub_v1
import time

#config project and topic 
project_id = "bold-landing-432711-u5"
topic_id =  "receive_data_gce"

publisher = pubsub_v1.PublisherClient()
# the topic path method creates a fully qualified identifier in the form 'projects/{project_id}/topics/{topic_id}'
topic_path = publisher.topic_path(project=project_id, topic= topic_id)

for n in range(1,10):
    data_str = f"Message number  {n}"

    #data must be a byte string
    data  = data_str.encode("utf-8")
    print(data)

    #when you publish a message, the client returns a future
    #set some sleep time between messages
    time.sleep(1)

    future = publisher.publish(topic_path, data)
    print(future.result())


print(f"Published Messages to the topic {topic_path}")



