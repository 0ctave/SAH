import torch
import matplotlib.pyplot as plt
import model
from torchsummary import summary

network = model.Convolution()
summary(network, input_size=(3, 256, 224))

image = torch.rand([3,256,224])



out = network.forward(image)

plt.imshow(out.detach()[0])
plt.show()
