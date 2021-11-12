import os,io
from google.cloud import videointelligence, storage
#from oauth2client.service_account import ServiceAccountCredentials

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/PRANJALI SAXENA/Desktop/Major project/Video API/video-ai-327613-da0990a26e67.json"
video_client = videointelligence.VideoIntelligenceServiceClient()
features = [videointelligence.Feature.OBJECT_TRACKING]

# Setting credentials using the downloaded JSON file
client = storage.Client.from_service_account_json(json_credentials_path='C:/Users/PRANJALI SAXENA/Desktop/Major project/Video API/video-ai-327613-da0990a26e67.json')
# Creating bucket object
bucket = client.get_bucket('vid-store')
blob = bucket.blob('Butterfly.mp4')
blob.upload_from_filename('C:/Users/PRANJALI SAXENA/Desktop/Major project/Video API/Butterfly.mp4')

#path = "C:/Users/PRANJALI SAXENA/Desktop/Major project/Video API/videoplayback.mp4"
#with io.open(path, "rb") as file:
 #   input_content = file.read()

gcs_uri = 'gs://vid-store/Butterfly'
operation = video_client.annotate_video(
    request={"features": features, "input_uri":gcs_uri}
)
print("\nProcessing video for object annotations.")

result = operation.result(timeout=300)
print("\nFinished processing.\n")

# The first result is retrieved because a single video was processed.
object_annotations = result.annotation_results[0].object_annotations

video_info={}

# Get only the first annotation for demo purposes.
for i, entity in enumerate(object_annotations):
    object_annotation = object_annotations[i]

    
    # Adding value to key='ashwini' as another dictonary
    video_info[i] = {"Entity description":"{}".format(object_annotation.entity.description),"Segment": "{}s to {}s".format(
            object_annotation.segment.start_time_offset.seconds
            + object_annotation.segment.start_time_offset.microseconds / 1e6,
            object_annotation.segment.end_time_offset.seconds
            + object_annotation.segment.end_time_offset.microseconds / 1e6,
        ),"Confidence": "{}".format(object_annotation.confidence)}
    

max_key = video_info[max(video_info, key=lambda v: video_info[v]["Confidence"])] 
print(max_key) 

