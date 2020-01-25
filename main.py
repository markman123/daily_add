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
        r = requests.post(url, data={"url": url, "capture_all": "on"})
        job_id = re.findall("var JOB_ID = \"(.+)\"", r.text) 
        if len(job_id) > 0:
            print(f"https://web/archive.org/save/status/{job_id[0]}")
        

if __name__ == '__main__':
    run("","")