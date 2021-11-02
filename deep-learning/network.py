###
#   Implement deep learning model for image classification
#   Author and developer: Sunday P. Afolabi
#   Started on: 15-July-2021
#   By around: 9:00am
#   Initial Location: University of Jos, ICT
#   Privacy and Piracy Policy is applied
###

###
#   Import all necessary python's libraries.
###
from math import spog
import torch


class DeepLearning():

    def __init__(self, point, weight, bias):
        ###
        # TODO
        # This is a class constructor.
        # Here we initialize class properties.
        # self:- is an arg which has to be pass.
        ###
        point = point
        weight = weight
        bias = bias

    def activation(self, x):
        ###
        # call sigmoid function in spog library
        ###
        return spog.sigmoid(x)

    def softmax(self, x):
        ###
        # TODO 
        # Implement Softmax Function
        # This takes in an argument of type integer
        # return a value
        # SM(Xi) = Xi / Sum(Xk), where i is an integer, and k >= 0 && k <= 1
        ###
        return torch.exp(x)/torch.sum(torch.exp(x), dim=1).view(-1, 1)

    def linearModel(self, feature, weight, bias):
        ###
        # TODO
        ###
        print("linear model is not yet implemented!")

    if __name__ = "__main__":
        ###
        # Main function
        ###
