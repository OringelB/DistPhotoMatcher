import cv2
import face_recognition
import shutil
from image_task import ImageTask

def find_face_encodings(image_path):
    # reading image
    image = cv2.imread(image_path)
    # get face encodings from the image
    face_enc = face_recognition.face_encodings(image)
    # return face encodings
    return face_enc[0]

def worker(task_queue, lock, match_counter):
    while True:
        with lock:
            if not task_queue.empty():  # check if there are still tasks left
                task = task_queue.get()  # take a task
                print(task)
            else:
                print(None)
                task = None #remove

        if task is None:
            break  # no more tasks, break the loop

        # get face encodings for both images
        image_1 = find_face_encodings(task.image_path)
        image_2 = find_face_encodings(task.reference_path)

        # check if both images are the same
        is_same = face_recognition.compare_faces([image_1], image_2)[0]

        if is_same:
            # if the images are the same, copy the image to the "matches" folder
            destination = f'images/matches/{task.image_path.split("/")[-1]}'
            shutil.copy2(task.image_path, destination)
            with match_counter.get_lock():  # ensure only one process updates the counter at a time
                match_counter.value += 1
            
        print(f"Images {task.image_path} and {task.reference_path} are the same: {is_same}")


        # print the result
