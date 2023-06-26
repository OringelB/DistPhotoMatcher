import os
from multiprocessing import Manager, Lock
from dataclasses import dataclass
from image_task import ImageTask


def producer(task_queue, directory, reference_image, lock):
    for filename in os.listdir(directory):
        # if filename.endswith(".jpg") or filename.endswith(".png"):  # adjust this as needed
        image_path = os.path.join(directory, filename).replace("\\", "/")
        task_queue.put(ImageTask(image_path, reference_image))  # use put method to add tasks to the queue
        print(f"Added task for image: {image_path}")

    


