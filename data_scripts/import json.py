import json

with open('ski2dpose_labels.json', 'r') as f:
    data = json.load(f)

# Get the first video, first subfolder, and first frame to see the keys
vid_id = list(data.keys())[0]
sub_id = list(data[vid_id].keys())[0]
frame_id = list(data[vid_id][sub_id].keys())[0]

print(f"Video ID: {vid_id}")
print(f"Subfolder ID: {sub_id}")
print(f"Frame ID: {frame_id}")
print(f"Data inside this frame: {data[vid_id][sub_id][frame_id]}")