import cv2

def remove_frame_from_video(input_video_path, output_video_path, frame_to_remove):
    # Open the input video
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get video properties
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Check if the frame to remove is within the valid range
    if frame_to_remove < 0 or frame_to_remove >= frame_count:
        print("Error: Frame to remove is out of range.")
        return

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    current_frame = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if current_frame != frame_to_remove:
            out.write(frame)

        current_frame += 1

    # Release everything if job is finished
    cap.release()
    out.release()

    print("Frame removed and video saved successfully.")

# Example usage
input_video_path = 'D102_S4_4_after.avi'
output_video_path = 'D102_S4_4_after_clean.avi'
frame_to_remove = 569  # Frame number to remove (0-based index)

remove_frame_from_video(input_video_path, output_video_path, frame_to_remove)

