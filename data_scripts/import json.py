"""
Debug script to inspect the structure of the ski2dpose_labels.json file.
It prints the first available video, subfolder, and frame data.
"""
import json

# Load the dataset JSON
with open('ski2dpose_labels.json', 'r') as f:
    data = json.load(f)

# Drill down: Get the first video -> first subfolder -> first frame key
vid_id = list(data.keys())[0]
sub_id = list(data[vid_id].keys())[0]
frame_id = list(data[vid_id][sub_id].keys())[0]

# Print details to verify structure and content
print(f"Video ID: {vid_id}")
print(f"Subfolder ID: {sub_id}")
print(f"Frame ID: {frame_id}")
print(f"Data inside this frame: {data[vid_id][sub_id][frame_id]}")