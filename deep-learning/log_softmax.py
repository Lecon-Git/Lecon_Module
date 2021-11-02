# My solution on log_softmax exercise

import torch
from torch import nn
from torch.nn.functional import F
from torchvision import dataset, transforms

# Download and transforms our train set
transform = transforms.Compose([
    transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])
trainset = dataset.MNIST('~/.pytorch/MNIST_data/', download=True, train=True, transform=transform) 
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

# Here is a FFNN
model = nn.Sequential(  nn.Linear(784, 128), 
                        nn.ReLU(),
                        nn.Linear(128, 64), 
                        nn.ReLU(),
                        nn.Linear(64, 10), 
                        nn.LogSoftmax(dim=1)
                    )

# Compute the loss
criterion = nn.NLLLoss()

# Get the data
images, labels = next(iter(trainloader))

# Fatten images
images = images.view(image[0], -1)

# Forward pass, get out scores
scores = model(images)

# Compute loss of the model
loss = criterion(scores, labels)

# Show result
print(loss)

