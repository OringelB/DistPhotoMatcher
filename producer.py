import os
from multiprocessing import Manager, Lock
from dataclasses import dataclass
from image_task import ImageTask

def producer(task_queue, directory, reference_image, lock):
    # Iterate through each file in the given directory
    for filename in os.listdir(directory):
        # Construct a path to the image by joining the directory path and filename
        # and replace backslashes with forward slashes to maintain OS compatibility
        image_path = os.path.join(directory, filename).replace("\\", "/")
        
        # Create an ImageTask object with the path of the current image and the reference image,
        # then put it into the task queue for the workers to process
        task_queue.put(ImageTask(image_path, reference_image))
        
        print(f"Added task for image: {image_path}")
