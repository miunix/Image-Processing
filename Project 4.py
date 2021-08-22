from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(os.path.join(execution_path , "yolo-tiny.h5"))
detector.loadModel()

custom_objects = detector.CustomObjects(cat=True)
detections = detector.detectObjectsFromImage(custom_objects=custom_objects, input_image=os.path.join(execution_path , "cat1.jpg"), output_image_path=os.path.join(execution_path , "cat-box.jpg"), minimum_percentage_probability=30, display_percentage_probability=False, display_object_name=False)

for eachObject in detections:
    print("--------------------------------------")
    print("Box Points: ",eachObject["box_points"])
    print("--------------------------------------")