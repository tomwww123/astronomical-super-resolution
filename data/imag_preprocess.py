import os
import random
from PIL import Image


def resize_and_shuffle_images(input_dir, output_dir, target_size=(256, 256)):
    # Create the output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    # List to store paths of all images
    all_images = []

    # Traverse through all subdirectories in the input directory
    for subdir, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                # Full path of the image
                image_path = os.path.join(subdir, file)
                all_images.append(image_path)

    # Shuffle the list of all images
    random.shuffle(all_images)

    # Process and save each image with sequential names
    for i, image_path in enumerate(all_images):
        try:
            # Open the image
            with Image.open(image_path) as img:
                # Resize the image to the target size
                img_resized = img.resize(target_size, Image.ANTIALIAS)

                # Convert to 3-channel (RGB) if not already in that mode
                if img_resized.mode != 'RGB':
                    img_resized = img_resized.convert('RGB')

                # Save the resized image to the output directory with sequential naming
                output_path = os.path.join(output_dir, f"image{i + 1}.jpg")
                img_resized.save(output_path, 'JPEG')

                print(f"Processed and saved: {output_path}")

        except Exception as e:
            print(f"Error processing {image_path}: {e}")


def resize_images(input_dir, output_dir, target_size=(256, 256)):
    # Create the output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    # Traverse through all subdirectories in the input directory
    for subdir, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                # Full path of the image
                image_path = os.path.join(subdir, file)

                try:
                    # Open the image
                    with Image.open(image_path) as img:
                        # Resize the image to the target size
                        img_resized = img.resize(target_size, Image.ANTIALIAS)

                        # Convert to 3-channel (RGB) if not already in that mode
                        if img_resized.mode != 'RGB':
                            img_resized = img_resized.convert('RGB')

                        # Save the resized image to the output directory with the original filename
                        output_path = os.path.join(output_dir, file)
                        img_resized.save(output_path, 'JPEG')

                        print(f"Processed and saved: {output_path}")

                except Exception as e:
                    print(f"Error processing {image_path}: {e}")

input_dir = 'dataset/test/256x256'  # Replace with your input directory path
output_dir = 'dataset/test/64x64'  # Replace with your output directory path
resize_images(input_dir, output_dir,(64, 64))
