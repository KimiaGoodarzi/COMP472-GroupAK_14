# -*- coding: utf-8 -*-
"""COMP472Part2Evaluation

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NOq7ucUBzzRlS741AcKiMj-QXCLxIB14
"""

#Import torch, numpy and sklearn
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Subset
from torchvision.transforms import v2
from torchvision.datasets import ImageFolder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report,precision_recall_fscore_support

#!gdown 1zWLvGyTRz07z3swsYJwK0_d-MjXgXvHY
#!unzip 'COMP472Data.zip'

#!gdown 1rvlKoAj2c6q6o2fugxaLOeXgfvhhEhbT
#!unzip 'model.zip'

#Load the dataset
path = '/content/COMP472Data'
transform = v2.Compose([v2.ToImage(),v2.Grayscale(),v2.ToDtype(torch.float32, scale=True)])
full_dataset = ImageFolder(path,transform)

#Hyperparameters
ttsplit = 0.2 #Train-Test Split %. Currently 80:20
vtsplit = 0.1 #Train-Validation Split %. Currently 90:10 ONLY splitting the traning data
batch_size = 32 #Batch size for model
# Split dataset indices
train_indices, test_indices = train_test_split(list(range(len(full_dataset))), test_size=ttsplit, random_state=42)
train_indices, val_indices = train_test_split(train_indices, test_size=vtsplit, random_state=42)
# Create subsets
train_set = Subset(full_dataset, train_indices)
val_set = Subset(full_dataset, val_indices)
test_set = Subset(full_dataset, test_indices)
# Create data loaders
train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_set, batch_size=batch_size, shuffle=False)
val_loader = torch.utils.data.DataLoader(val_set, batch_size=batch_size, shuffle=False)

#Define the architecture each model used
model = nn.Sequential(
    nn.Conv2d(1, 32, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(32),

    nn.Conv2d(32, 64, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(64),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),

    nn.Conv2d(64, 128, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(128),

    nn.Conv2d(128, 128, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(128),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),

    nn.Conv2d(128, 256, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(256),

    nn.Conv2d(256, 256, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(256),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),

    nn.Flatten(),

    nn.Linear(256 * 6 * 6, 256),
    nn.ReLU(),
    nn.BatchNorm1d(256),
    nn.Dropout(0.5),

    nn.Linear(256, 4)
)

model_variant1A = nn.Sequential(
    nn.Conv2d(1, 32, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(32),

    nn.Conv2d(32, 64, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(64),

    nn.Conv2d(64, 64, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(64),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),

    nn.Conv2d(64, 128, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(128),

    nn.Conv2d(128, 128, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(128),

    nn.Conv2d(128, 128, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(128),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),

    nn.Conv2d(128, 256, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(256),

    nn.Conv2d(256, 256, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(256),

    nn.Conv2d(256, 256, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(256),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),

    nn.Flatten(),
    nn.Linear(256 * 6 * 6, 256),
    nn.ReLU(),
    nn.BatchNorm1d(256),
    nn.Dropout(0.5),
    nn.Linear(256, 4)
)

model_variant1B = nn.Sequential(
    nn.Conv2d(1, 32, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(32),

    nn.Conv2d(32, 64, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(64),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),

    nn.Conv2d(64, 128, kernel_size=3, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(128),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),

    nn.Flatten(),
    nn.Linear(128 * 12 * 12, 256),
    nn.ReLU(),
    nn.BatchNorm1d(256),
    nn.Dropout(0.5),
    nn.Linear(256, 4)
)

model_variant2A = nn.Sequential(
    nn.Conv2d(1, 32, kernel_size=5, padding=2),  # Changed to 5x5
    nn.ReLU(),
    nn.BatchNorm2d(32),

    nn.Conv2d(32, 64, kernel_size=5, padding=2),  # Changed to 5x5
    nn.ReLU(),
    nn.BatchNorm2d(64),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),

    nn.Conv2d(64, 128, kernel_size=5, padding=2),  # Changed to 5x5
    nn.ReLU(),
    nn.BatchNorm2d(128),

    nn.Conv2d(128, 128, kernel_size=5, padding=2),  # Changed to 5x5
    nn.ReLU(),
    nn.BatchNorm2d(128),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),

    nn.Conv2d(128, 256, kernel_size=5, padding=2),  # Changed to 5x5
    nn.ReLU(),
    nn.BatchNorm2d(256),

    nn.Conv2d(256, 256, kernel_size=5, padding=2),  # Changed to 5x5
    nn.ReLU(),
    nn.BatchNorm2d(256),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),

    nn.Flatten(),
    nn.Linear(256 * 6 * 6, 256),
    nn.ReLU(),
    nn.BatchNorm1d(256),
    nn.Dropout(0.5),

    nn.Linear(256, 4)
)


model_variant2B = nn.Sequential(
    nn.Conv2d(1, 32, kernel_size=2, padding=1),  # Changed to 2x2
    nn.ReLU(),
    nn.BatchNorm2d(32),
    nn.Conv2d(32, 64, kernel_size=2, padding=1),  # Changed to 2x2
    nn.ReLU(),
    nn.BatchNorm2d(64),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),
    nn.Conv2d(64, 128, kernel_size=2, padding=1),  #2x2
    nn.ReLU(),
    nn.BatchNorm2d(128),
    nn.Conv2d(128, 128, kernel_size=2, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(128),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),
    nn.Conv2d(128, 256, kernel_size=2, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(256),
    nn.Conv2d(256, 256, kernel_size=2, padding=1),
    nn.ReLU(),
    nn.BatchNorm2d(256),
    nn.MaxPool2d(2, 2),
    nn.Dropout(0.25),
    nn.Flatten(),
    nn.Linear(256 * 7 * 7, 256),  # Adjusted input size
    nn.ReLU(),
    nn.BatchNorm1d(256),
    nn.Dropout(0.5),
    nn.Linear(256, 4)
)

#Method to get the predicted and true labels for each model
def evaluate(model,loader):
    model.eval()
    all_preds = []
    all_labels = []
    with torch.no_grad():
        for inputs, labels in loader:
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
    return np.array(all_preds), np.array(all_labels)

#Load all the models from the .pth files
model.load_state_dict(torch.load('/content/model/bestModel.pth', map_location=torch.device('cpu')))
model_variant1A.load_state_dict(torch.load('/content/model/bestmodel_variant1A.pth', map_location=torch.device('cpu')))
model_variant1B.load_state_dict(torch.load('/content/model/bestmodel_variant1B.pth', map_location=torch.device('cpu')))
model_variant2A.load_state_dict(torch.load('/content/model/bestmodel_variant2A.pth', map_location=torch.device('cpu')))
model_variant2B.load_state_dict(torch.load('/content/model/bestmodel_variant2B.pth', map_location=torch.device('cpu')))

"""Main Model"""

#Class names
class_names = full_dataset.classes

#Compute the confusion matrix
pred, true = evaluate(model,test_loader)

#Display the confusion matrix
cm = confusion_matrix(true,pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot()

#Display the classification report
print("Main Model Classification Report:")
print(classification_report(true, pred, target_names=class_names))
print("Main Model Macro/Micro")
macro_p,macro_r,macro_f,_ = precision_recall_fscore_support(true,pred,average='macro')
micro_p,micro_r,micro_f,_ = precision_recall_fscore_support(true,pred,average='micro')
print("Macro: " + str(round(macro_p,3)) + " " + str(round(macro_r,3)) + " " + str(round(macro_f,3)))
print("Micro: " + str(round(micro_p,3)) + " " + str(round(micro_r,3)) + " " + str(round(micro_f,3)))

#Assuming class 3 and class 2 indices are 2 and 1 respectively
class_3_index = 2
class_2_index = 1
import matplotlib.pyplot as plt

#Get the indices where class 3 was mislabeled as class 2
misclassified_indices = np.where((true == class_3_index) & (pred == class_2_index))[0]
for index in misclassified_indices:
    #Retrieve the image and label corresponding to the misclassified index
    image, label = test_set[index]
    #Print the image and the corresponding true label
    print("True label:", class_names[label])
    plt.imshow(image[0,:,:], cmap='gray')
    plt.show()
    plt.axis('off')

"""Variant 1A & 1B"""

#Compute the confusion matrix
pred, true = evaluate(model_variant1A,test_loader)

#Display the confusion matrix
cm = confusion_matrix(true,pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot()

#Display the classification report
print("Model1A Classification Report:")
print(classification_report(true, pred, target_names=class_names))
macro_p,macro_r,macro_f,_ = precision_recall_fscore_support(true,pred,average='macro')
micro_p,micro_r,micro_f,_ = precision_recall_fscore_support(true,pred,average='micro')
print("Macro: " + str(round(macro_p,3)) + " " + str(round(macro_r,3)) + " " + str(round(macro_f,3)))
print("Micro: " + str(round(micro_p,3)) + " " + str(round(micro_r,3)) + " " + str(round(micro_f,3)))

#Compute the confusion matrix
pred, true = evaluate(model_variant1B,test_loader)

#Display the confusion matrix
cm = confusion_matrix(true,pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot()

#Display the classification report
print("Model1B Classification Report:")
print(classification_report(true, pred, target_names=class_names))
macro_p,macro_r,macro_f,_ = precision_recall_fscore_support(true,pred,average='macro')
micro_p,micro_r,micro_f,_ = precision_recall_fscore_support(true,pred,average='micro')
print("Macro: " + str(round(macro_p,3)) + " " + str(round(macro_r,3)) + " " + str(round(macro_f,3)))
print("Micro: " + str(round(micro_p,3)) + " " + str(round(micro_r,3)) + " " + str(round(micro_f,3)))

"""Variants 2A & 2B"""

#Compute the confusion matrix
pred, true = evaluate(model_variant2A,test_loader)

#Display the confusion matrix
cm = confusion_matrix(true,pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot()

#Display the classification report
print("Model2A Classification Report:")
print(classification_report(true, pred, target_names=class_names))
macro_p,macro_r,macro_f,_ = precision_recall_fscore_support(true,pred,average='macro')
micro_p,micro_r,micro_f,_ = precision_recall_fscore_support(true,pred,average='micro')
print("Macro: " + str(round(macro_p,3)) + " " + str(round(macro_r,3)) + " " + str(round(macro_f,3)))
print("Micro: " + str(round(micro_p,3)) + " " + str(round(micro_r,3)) + " " + str(round(micro_f,3)))

#Compute the confusion matrix
pred, true = evaluate(model_variant2B,test_loader)

#Display the confusion matrix
cm = confusion_matrix(true,pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot()

#Display the classification report
print("Model2B Classification Report:")
print(classification_report(true, pred, target_names=class_names))
macro_p,macro_r,macro_f,_ = precision_recall_fscore_support(true,pred,average='macro')
micro_p,micro_r,micro_f,_ = precision_recall_fscore_support(true,pred,average='micro')
print("Macro: " + str(round(macro_p,3)) + " " + str(round(macro_r,3)) + " " + str(round(macro_f,3)))
print("Micro: " + str(round(micro_p,3)) + " " + str(round(micro_r,3)) + " " + str(round(micro_f,3)))