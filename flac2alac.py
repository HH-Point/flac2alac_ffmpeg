import os
import subprocess

# Request target directory from the user
target_dir = input("Enter the target directory path: ")

# Iterate through the files in the target directory
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.lower().endswith(".flac"):
            # Generate input and output file paths
            input_file = os.path.join(root, file)
            
            # Create ALAC folder within the file's parent directory if it doesn't exist
            alac_dir = os.path.join(os.path.dirname(input_file), "ALAC")
            if not os.path.exists(alac_dir):
                os.makedirs(alac_dir)
            
            output_file = os.path.join(alac_dir, os.path.splitext(file)[0] + ".m4a")

            # Execute FFmpeg command to convert FLAC to ALAC
            command = [
                "ffmpeg",
                "-i", input_file,
                "-map_metadata", "0",  # Retain metadata
                "-c:a", "alac",
                "-vn",  # Ignore video streams
                "-y",  # Overwrite existing files
                output_file
            ]
            subprocess.run(command)

print("Conversion completed. ALAC files are saved in the respective ALAC folders.")
