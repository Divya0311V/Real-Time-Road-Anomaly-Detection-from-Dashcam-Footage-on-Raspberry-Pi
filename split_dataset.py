import os
import shutil
import random

# Paths
dataset_path = "Pothole Dataset"
images_path = os.path.join(dataset_path, "")
labels_path = os.path.join(dataset_path, "")

# Create train/val folders
for folder in ["images/train", "images/val", "labels/train", "labels/val"]:
    os.makedirs(os.path.join(dataset_path, folder), exist_ok=True)

# Get all images
all_images = [f for f in os.listdir(dataset_path) if f.endswith(".jpg")]
random.shuffle(all_images)

split_ratio = 0.8  # 80% train, 20% val
split_index = int(len(all_images) * split_ratio)

train_images = all_images[:split_index]
val_images = all_images[split_index:]

# Move images and labels
for img_list, split_type in zip([train_images, val_images], ["train", "val"]):
    for img_file in img_list:
        label_file = img_file.replace(".jpg", ".txt")

        # Move image
        shutil.move(os.path.join(dataset_path, img_file),
                    os.path.join(dataset_path, f"images/{split_type}/{img_file}"))

        # Move label
        shutil.move(os.path.join(dataset_path, label_file),
                    os.path.join(dataset_path, f"labels/{split_type}/{label_file}"))

print("Dataset split completed!")
