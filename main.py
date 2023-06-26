from multiprocessing import Manager, Lock
from producer import producer

if __name__ == "__main__":
    manager = Manager()
    lock = Lock()
    task_queue = manager.list()  # shared list for tasks

    # path to the directory containing images to be processed
    image_dir = "images/collection"

    # path to the reference image
    ref_image = "images/reference"

    producer(task_queue, image_dir, ref_image, lock)

    # Here you would also start your worker processes, which you will implement next.
