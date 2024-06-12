import os
import subprocess

# Define directories
input_directory = 'downloads/m4v_videos'  # Directory containing M4V files
output_directory = 'downloads/avi_videos'  # Directory where AVI files will be saved

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Function to convert a single video
def convert_video(input_path, output_path):
    # Define the FFmpeg command
    ffmpeg_command = [
        'ffmpeg',
        '-i', input_path,  # Input file
        output_path       # Output file
    ]

    # Run the FFmpeg command
    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"Video converted successfully: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during video conversion: {e}")

# Iterate over all .m4v files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.m4v'):
        input_file_path = os.path.join(input_directory, filename)
        output_file_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.avi")

        # Convert the video
        convert_video(input_file_path, output_file_path)

        # Check if the output file exists
        if os.path.exists(output_file_path):
            print(f"AVI video is available at: {output_file_path}")
        else:
            print(f"Conversion failed, output file not found: {output_file_path}")

print("All files processed successfully.")
