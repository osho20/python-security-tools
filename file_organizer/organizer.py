import os
import shutil

source_folder = "test_folder"

for file in os.listdir(source_folder):
    filepath = os.path.join(source_folder, file)

    if file.endswith(".jpg"):
        shutil.move(filepath, os.path.join(source_folder, "images", file))

    elif file.endswith(".pdf"):
        shutil.move(filepath, os.path.join(source_folder, "documents", file))