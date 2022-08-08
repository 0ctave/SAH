# importing the libraries
import numpy as np



import torch
from torch.autograd import Variable
from torch.nn import Linear, ReLU, CrossEntropyLoss, Sequential, Conv2d, MaxPool2d, Module, Softmax, BatchNorm2d, Dropout
import torch.nn as nn
from torch.optim import Adam, SGD


class Convolution(nn.Module):
    def __init__(self):
        super(Convolution, self).__init__()

        self.n_layers = 4
        self.cnn_layers = nn.Sequential(
            nn.Conv2d(3, self.n_layers*4, kernel_size=3, stride=1, padding=2),
            nn.ReLU(),
            nn.Conv2d(self.n_layers*4, self.n_layers*4, kernel_size=5, stride=3, padding=2),
            nn.ReLU(),
            nn.Conv2d(self.n_layers*4, self.n_layers*2, kernel_size=3, stride=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(self.n_layers*2, self.n_layers, kernel_size=[3,5], stride=[2,3], padding=1),
            nn.ReLU(),
            nn.Conv2d(self.n_layers, 1, kernel_size = [4,8], stride = [1,1], padding = 0),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.cnn_layers(x)
        return x