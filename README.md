convert_in_batch.py: 
This code takes the m4v versions of videos (version in google drive) and converts to AVI, which is the required format for OpenFace to run. 
How to use: 
1. Download m4v videos from Google Drive and name appropriately
2. Put videos into a folder and change the input_directory name at the top of the code to match folder path accordingly. The default name is m4v_videos
3. Create an empty folder for the outputted AVI videos and change the output_directory name at the top of the code to match the folder path. The default name is output_directory
4. Run the code

process_videos:
This code takes the AVI videos, runs OpenFace using a Docker container called OpenFace, and outputs the corresponding CSVs. The code will copy the AVI folder to the OpenFace bin, run FeatureDetection, and copy the resulting CSV into the local computer from the docker container.
How to use:
1. At the top of the code, change the following:
    a. PARTICIPANT_VIDEOS_DIR should be the path to the AVI video folder
    b. DOCKER_CONTAINER should be the Docker container name (openface in this case)
    c. DOCKER_WORKDIR should be the path to the docker bin you are using
    d. DOCKER_OUTPUT should be the path to wherever the outputted CSV is stored (manually running openface once might be required to find this path)
    e. LOCAL_OUTPUT_DIR should be the path of the folder where the outputted CSVs should be stored
2. In the terminal, type 'chmod +x run_openface/process_videos.sh' to make the script executable 
3. In the terminal, type './run_openface/process_videos.sh' to run the script
Note: Occasionally some video frames will be corrupt, in which case the frame-remove.py code will remove the corrupt frame. To find which frame this is, 'cat <filename>.csv | cut -d "," -f 1' prints the frame number for every row in the CSV, meaning the frame after the last frame printed is corrupt.

