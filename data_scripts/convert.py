import json
import os
import shutil

# Confirmed dimensions from your 1280x720 check
IMG_W = 1280
IMG_H = 720

source_dir = 'Images_jpg'
output_dir = 'Training_Data'
json_path = 'ski2dpose_labels.json'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(json_path, 'r') as f:
    data = json.load(f)

ei_labels = {"version": 1, "type": "bounding-box-labels", "boundingBoxes": {}}

print(f"--- Processing {IMG_W}x{IMG_H} Data ---")

count = 0
# Logic mirrors the debug script that worked
for video_id, subfolders in data.items():
    for subfolder_id, frames in subfolders.items():
        for frame_key, frame_info in frames.items():
            
            # Match the specific path: Images_jpg/video_id/sub_id/frame.jpg
            original_path = os.path.join(source_dir, video_id, subfolder_id, f"{frame_key}.jpg")
            
            if os.path.exists(original_path):
                # Create a unique filename so we don't overwrite frames from different videos
                new_filename = f"{video_id}_{subfolder_id}_{frame_key}.jpg"
                target_path = os.path.join(output_dir, new_filename)
                
                shutil.copy(original_path, target_path)
                
                # Use the 'annotation' key that worked in debug
                pts = frame_info.get("annotation", [])
                
                # Convert normalized to pixel values
                xs = [float(p[0]) * IMG_W for p in pts if float(p[0]) > 0]
                ys = [float(p[1]) * IMG_H for p in pts if float(p[1]) > 0]
                
                if xs and ys:
                    # Keep it tight since it's working
                    pad = 10 
                    x_min, x_max = max(0, min(xs)-pad), min(IMG_W, max(xs)+pad)
                    y_min, y_max = max(0, min(ys)-pad), min(IMG_H, max(ys)+pad)
                    
                    ei_labels["boundingBoxes"][new_filename] = [{
                        "label": "Skier",
                        "x": int(x_min),
                        "y": int(y_min),
                        "width": int(x_max - x_min),
                        "height": int(y_max - y_min)
                    }]
                    count += 1

# Save the final label file inside the training folder
with open(os.path.join(output_dir, 'bounding_boxes.labels'), 'w') as f:
    json.dump(ei_labels, f)

print(f"--- SUCCESS: {count} images ready for upload ---")