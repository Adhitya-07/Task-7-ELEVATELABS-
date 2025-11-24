import os
from PIL import Image

input_folder = "images"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

new_size = (800, 800)

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        try:
            img_path = os.path.join(input_folder, file_name)
            img = Image.open(img_path)

            resized_img = img.resize(new_size)

            output_path = os.path.join(output_folder, file_name.split('.')[0] + ".png")

            resized_img.save(output_path)
            print(f"Processed: {file_name}")

        except Exception as e:
            print(f"Error processing {file_name}: {e}")

print("Completed. Check the output folder.")
