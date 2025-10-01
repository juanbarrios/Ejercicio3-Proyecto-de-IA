# -*- coding: utf-8 -*- 
import io
from app import model, imagenet_class_index
import torchvision.transforms as transforms
from PIL import Image
import torch.nn.functional as F

def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize(256, interpolation=transforms.InterpolationMode.BILINEAR),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    print("evaluando imagen en la red...")
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    probabilities = F.softmax(outputs, dim=1)
    score_tensor, position_tensor = probabilities.max(1)
    position = position_tensor.item()
    score = score_tensor.item()
    print("max-position: {} max-score: {:.3f}".format(position, score))
    array = imagenet_class_index[str(position)]
    clase_id = array[0]
    clase_nombre = array[1]
    print("clase: {} {}".format(clase_id, clase_nombre))
    return clase_id, clase_nombre
