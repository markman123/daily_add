import requests
import re

def run(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    data = open("watch.txt","r").readlines()
    for itm in data:
        url = f"https://web.archive.org/save/{itm.strip()}"
        r = requests.get(url)
        if "content-location" in r.headers.keys():
            print(f"https://web.archive.org{r.headers['content-location']}")
        
        

if __name__ == '__main__':
    run("","")