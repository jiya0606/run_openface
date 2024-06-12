#!/bin/bash

# Define paths
PARTICIPANT_VIDEOS_DIR="downloads/avi_videos" #participant_videos
DOCKER_CONTAINER="openface"
DOCKER_WORKDIR="/home/openface-build/build/bin"
DOCKER_OUTPUT="/home/openface-build/processed"
LOCAL_OUTPUT_DIR="processed_csvs"

# Ensure the output directory exists
mkdir -p "$LOCAL_OUTPUT_DIR"

# Iterate over each AVI file in the participant_videos directory
for filepath in "$PARTICIPANT_VIDEOS_DIR"/*.avi; do
  # Extract the filename from the full filepath
  filename=$(basename "$filepath")

  # Copy the AVI file to the Docker container
  echo "Copying $filename to Docker container..."
  docker cp "$filepath" "$DOCKER_CONTAINER:$DOCKER_WORKDIR"

  # Run the FeatureExtraction command inside the Docker container
  echo "Running FeatureExtraction on $filename in Docker container..."
  docker exec "$DOCKER_CONTAINER" "$DOCKER_WORKDIR/FeatureExtraction" -f "$DOCKER_WORKDIR/$filename"

  # Define the expected output CSV filename
  output_csv="${filename%.*}.csv"
  echo "Here is the name of the csv:${filename%.*}"

  # Copy the output CSV file from the Docker container to the local machine
  echo "Copying processed CSV $output_csv from Docker container to local machine..."
  docker cp "openface:/home/openface-build/processed/$output_csv" "$LOCAL_OUTPUT_DIR"
  #docker cp "openface:$DOCKER_CONTAINER:$DOCKER_OUTPUT/$output_csv" "$LOCAL_OUTPUT_DIR"
  #docker cp "$DOCKER_CONTAINER:$DOCKER_WORKDIR/processed/$output_csv" "$LOCAL_OUTPUT_DIR"
done

echo "All files processed successfully."
