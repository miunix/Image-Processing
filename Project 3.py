from imageai.Classification import ImageClassification
import os

execution_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsDenseNet121()
prediction.setModelPath(os.path.join(execution_path, "DenseNet-BC-121-32.h5"))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "seaturtle.jpg"), result_count=5 )
for thePrediction, theProbability in zip(predictions, probabilities):
    print(thePrediction , " : " , theProbability)
    
# MobileNetV2 - mobilenet_v2
# ResNet50 - resnet50_imagenet_tf.2.0
# InceptionV3 - inception_v3_weights_tf_dim_ordering_tf_kernels
# DenseNet121 - DenseNet-BC-121-32