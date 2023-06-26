from multiprocessing import Manager, Lock, Process, Value
from producer import producer
from worker import worker
import time

if __name__ == "__main__":
    manager = Manager()
    lock = Lock()
    task_queue = manager.Queue()  # shared queue for tasks

    # path to the directory containing images to be processed
    image_dir = "images/collection"

    # path to the reference image
    ref_image = "images/reference/image.JPG"

    producer(task_queue, image_dir, ref_image, lock)

    # start worker processes
    worker_processes = []
    match_counter = Value('i', 0)  # shared counter for matches
    start_time = time.time()
    for _ in range(4):  # adjust the number of workers as needed
        p = Process(target=worker, args=(task_queue, lock, match_counter))
        p.start()
        worker_processes.append(p)

    # wait for all workers to finish
    for p in worker_processes:
        p.join()

    elapsed_time = time.time() - start_time
    print(f"All tasks completed in {elapsed_time} seconds.")
    print(f"Number of matches: {match_counter.value}")
