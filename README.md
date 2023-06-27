# Face Recognition Task Queue

This application is designed to perform facial recognition on a collection of images in parallel using Python's multiprocessing library. The main goal is to match faces in a collection of images to a given reference image. Matched images are then copied to the 'matches' directory.

## Main Components

- **ImageTask:** A data class that represents a task to compare an image from a collection with a reference image.
- **Producer:** A function that creates tasks for each image in the collection and adds them to a multiprocessing queue.
- **Worker:** A function that picks up tasks from the queue, performs face recognition, and checks if the face in the given image matches the face in the reference image. If a match is found, the image is copied to the 'matches' directory.
- **Main:** A script that manages the sharing of tasks between the producer and worker using a multiprocessing queue.

## Usage

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the repository's directory.
3. Make sure you have Python 3.8 or later installed.
4. Install the necessary dependencies by running the command: `pip install dlib numpy face-recognition opencv-python dataclasses`
5. Place your collection of images in the "images/collection" directory and the reference image in the "images/reference" directory (Make sure that the reference image name is "image".
6. There are some photos in the directories you are welcome to use if you just want to test out the code, if not - feel free to delete them.
7. Run the main script by typing the command: `python main.py`
8. The script will print whether each image in the collection matches the reference image, and if a match is found, the image will be copied to the 'matches' directory.

## Dependencies

This project uses the following Python packages:
- os
- multiprocessing
- dlib
- numpy
- face-recognition
- cv2
- dataclasses


