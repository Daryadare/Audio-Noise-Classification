import torch
from torchvision.models.resnet import _resnet
from torchvision.models import resnet101
import torch.nn as nn


class ResNet101(nn.Module):
    def __init__(self, num_labels:int, device:torch.device):
        super().__init__()

        self.model = resnet101(num_classes=num_labels).to(device)
        self.num_labels = num_labels

    def forward(self, x:torch.Tensor) -> torch.Tensor:
        if x.shape[1] == 1:
            inp = torch.zeros((x.shape[0], 3, *x.shape[2:])).to(x.device)
            inp[:,:] = x
        else:
            inp = x
            
        res = self.model(inp)

        if self.num_labels == 1:
            out = torch.sigmoid(res)
        else:
            out = res

        return out
    

if __name__ == "__main__":
    model = ResNet101(1, device)
    print(model)
    