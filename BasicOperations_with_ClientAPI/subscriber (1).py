from google.cloud import pubsub_v1
import time

#config project and topic 
project_id = "bold-landing-432711-u5"
subscription_id =  "receive_data_gce-sub"


subscriber = pubsub_v1.SubscriberClient()

#no of seconds the subscriber should listen for messages
timeout = 5.0 

#the subscription path method creates a fully qualified identifier in the form 'projects/{project_id}/subscriptions{scbscriptions_id}'

subscription_path = subscriber.subscription_path(project=project_id, subscription=subscription_id)

#receive and acknowlegde the msg
def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    print(f"Received {message}.")
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback)
print(f"Listening for messages on {subscription_path}..\n")


#Wrap subscriber in a 'with' block to automatically call close () when done 
with subscriber:
    try:
        #when timeout is not set, result() will block indefinitley,unless an exception is encountered first
        streaming_pull_future.result(timeout=timeout)

    except TimeoutError:
        streaming_pull_future.cancel() # trigger the shutdown
        streaming_pull_future.result() #block until the shutdown is complete




# callback: This is a function that gets called whenever a message is received.
# message.ack(): Acknowledges the message, telling Pub/Sub that it was successfully processed so that it doesn’t get redelivered.




# subscribe(): Subscribes to the given subscription path and starts listening for messages, using the callback function to process them.
# streaming_pull_future: This holds the future result of the subscription, allowing you to manage it (like canceling it later).
# print(...): Prints a message indicating that the subscriber is listening for messages



# with subscriber:: Ensures that the subscriber is properly closed when done. This is good practice to release resources.
# streaming_pull_future.result(timeout=timeout): Starts the subscription and blocks the program from doing anything else until a timeout occurs (in this case, 5 seconds).
# except TimeoutError:: Catches a TimeoutError, which occurs when the specified timeout is reached.
# streaming_pull_future.cancel(): Cancels the subscription, stopping the message flow.
# streaming_pull_future.result(): Waits until the subscription is fully canceled before the program continues.
