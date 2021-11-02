import torch
from torch import nn
from torch.nn.functional as F
from torchvision import datasets, transforms

def downloadDataset():
    # Define a transform to normalize the data
    transform = transforms.Compose([transforms.ToTensor(), 
                                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                                    ])

    #Download and load the traning data
    trainset = datasets.MNIST('~/.pytorch/MNIST_data/', download=True, train=True, transform=transform)
    return torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

class Classifier(nn.Model):
    def __init__(self):
        super().__init__()
        # Build a feed-forward network
        # inputs to hidden layer 1 linear transformation
        self.hidden_1 = nn.Linear(784, 128)
        self.hidden_2 = nn.Linear(128, 64)
        self.output = nn.Linear(64, 10) 

    def forward(self, trainloader):
        # Define the loss
        criterion = nn.CrossEntropyLoss()
        # Get our data
        images, labels = next(iter(trainloader))
        # Flatten images
        images = images.view(images.shape[0], -1)
        # Forward pass, get out logits
        model = nn.Sequential(hidden_1, nn.ReLU(),
                            hidden_2, nn.ReLU(), output)
        logits = model(images)
        # Calculate the loss with the logits and the labels
        loss = criterion(logits, labels)
        # Write the result of loss to a file called loss.txt
        with open("loss.txt", "w") as f:
            f.write("Here is the loss with the logits(scores) and the labels\n"+loss)

        return loss

if __name__='__main__':
    this.forward(downloadDataset())


