import os
import shutil

# Paths
metadata_dir = 'pathfinder32/curv_baseline/metadata/'
images_base_dir = 'pathfinder32/curv_baseline/imgs/'
output_dir = 'dataset/'

# Ensure output directories exist
os.makedirs(os.path.join(output_dir, 'class_0'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'class_1'), exist_ok=True)

# Get list of metadata files
metadata_files = [f for f in os.listdir(metadata_dir) if f.endswith('.npy')]

for metadata_file in metadata_files:
    # Open and read the metadata file as a text file
    metadata_path = os.path.join(metadata_dir, metadata_file)
    with open(metadata_path, 'r') as f:
        lines = f.readlines()

    # Process each line in the metadata
    for line in lines:
        parts = line.strip().split(' ')
        if len(parts) < 4:
            continue  # Skip lines that don't have enough data

        # Extract image folder and filename
        img_folder = parts[0].split('/')[1]  # Extract folder number (e.g., '0')
        img_filename = parts[1]
        label = parts[3]  # Assuming label is in the 4th column (index 3)

        # Source image path
        src_img_path = os.path.join(images_base_dir, img_folder, img_filename)

        # Destination directory based on label
        dest_dir = os.path.join(output_dir, f'class_{label}')
        os.makedirs(dest_dir, exist_ok=True)

        # Destination image path
        # To prevent filename collisions, include the folder number in the filename
        dest_img_path = os.path.join(dest_dir, f"{img_folder}_{img_filename}")

        # Copy image to the destination directory
        if os.path.exists(src_img_path):
            shutil.copyfile(src_img_path, dest_img_path)
        else:
            print(f'Image not found: {src_img_path}')
