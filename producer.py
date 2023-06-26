import os
from multiprocessing import Manager, Lock
from dataclasses import dataclass
from image_task import ImageTask


def producer(task_queue, directory, reference_image, lock):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # adjust this as needed
            image_path = os.path.join(directory, filename)
            with lock:
                task_queue.append(ImageTask(image_path, reference_image))


