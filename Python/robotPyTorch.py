# Object Detection -> SLAM -> Motion

from cortano import RemoteInterface
import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn
from torchvision import transforms
from PIL import Image
import cv2

if __name__ == "__main__":
    robot = RemoteInterface("192.168.50.88")
    model = maskrcnn_resnet50_fpn(pretrained=True, pretrained_backbone=True)
    model.eval()


    while True:
        robot.update()
        color, depth, sensors = robot.read()

        preprocess = transforms.Compose([ transforms.ToTensor(), ])
        input_tensor = preprocess(Image.fromarray(color))
        input_batch = input_tensor.unsqueeze(0)
        with torch.no_grad():
            output = model(input_batch)[0]
        output = {l: output[l].to('cpu').numpy() for l in output}

        print(output)

        cv2.imshow("color",color)
        cv2.waitKey(1)