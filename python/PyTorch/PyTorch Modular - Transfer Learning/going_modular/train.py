"""
Trains a PyTorch image classification model using device-agnostic code.
"""

import os
import torch
import torchvision

from torchinfo import summary
import data_setup, engine, model_builder, utils,loss_and_accuracy_curve_plotter


from torchvision import transforms
from timeit import default_timer as timer 

# Setup hyperparameters
NUM_EPOCHS = 10
BATCH_SIZE = 32
# HIDDEN_UNITS = 10
LEARNING_RATE = 0.001


#going modular/data/pizza_steak_sushi/train
# Setup directories
train_dir = "/Users/h6x/ORNL/git/learning/python/PyTorch/PyTorch Modular - Transfer Learning/data/pizza_steak_sushi/train"
test_dir = "/Users/h6x/ORNL/git/learning/python/PyTorch/PyTorch Modular - Transfer Learning/data/pizza_steak_sushi/test"

# Setup target device
device = "cuda" if torch.cuda.is_available() else "cpu"


# NEW: Setup the model with pretrained weights and send it to the target device (torchvision v0.13+)
weights = torchvision.models.EfficientNet_B0_Weights.DEFAULT # .DEFAULT = best available weights 
model = torchvision.models.efficientnet_b0(weights=weights).to(device)

# Freeze all base layers in the "features" section of the model (the feature extractor) by setting requires_grad=False
for param in model.features.parameters():
    param.requires_grad = False

# # Create transforms
# manual_transforms = transforms.Compose([
#     transforms.Resize((224, 224)), # 1. Reshape all images to 224x224 (though some models may require different sizes)
#     transforms.ToTensor(), # 2. Turn image values to between 0 & 1 
#     transforms.Normalize(mean=[0.485, 0.456, 0.406], # 3. A mean of [0.485, 0.456, 0.406] (across each colour channel)
#                          std=[0.229, 0.224, 0.225]) # 4. A standard deviation of [0.229, 0.224, 0.225] (across each colour channel),
# ])

# Whatever the tranfer learning model that we select, using auto transforms we can get the transforms(less customization)
auto_transforms = weights.transforms()


# Create DataLoaders with help from data_setup.py
train_dataloader, test_dataloader, class_names = data_setup.create_dataloaders(
    train_dir=train_dir,
    test_dir=test_dir,
    transform=auto_transforms,
    batch_size=BATCH_SIZE
)


# Set the manual seeds
torch.manual_seed(42)
torch.cuda.manual_seed(42)

# Get the length of class_names (one output unit for each class)
output_shape = len(class_names)


# Recreate the classifier layer and seed it to the target device
model.classifier = torch.nn.Sequential(
    torch.nn.Dropout(p=0.2, inplace=True), 
    torch.nn.Linear(in_features=1280, 
                    out_features=output_shape, # same number of output units as our number of classes
                    bias=True)).to(device)

# # Print a summary using torchinfo (uncomment for actual output)
# summary(model=model, 
#         input_size=(32, 3, 224, 224), # make sure this is "input_size", not "input_shape"
#         # col_names=["input_size"], # uncomment for smaller output
#         col_names=["input_size", "output_size", "num_params", "trainable"],
#         col_width=20,
#         row_settings=["var_names"]
# ) 





# # Create model with help from model_builder.py
# model = model_builder.TinyVGG(
#     input_shape=3,
#     hidden_units=HIDDEN_UNITS,
#     output_shape=len(class_names)
# ).to(device)

# Set loss and optimizer
loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),
                             lr=LEARNING_RATE)

start_time = timer()

# Start training with help from engine.py
results = engine.train(model=model,
             train_dataloader=train_dataloader,
             test_dataloader=test_dataloader,
             loss_fn=loss_fn,
             optimizer=optimizer,
             epochs=NUM_EPOCHS,
             device=device)

# End the timer and print out how long it took
end_time = timer()
print(f"Total training time: {end_time-start_time:.3f} seconds")

#plotting the results
loss_and_accuracy_curve_plotter.plot_loss_curves(results)

# # Save the model with help from utils.py
# utils.save_model(model=model,
#                  target_dir="/Users/h6x/ORNL/git/learning/python/PyTorch/PyTorch Modular - Transfer Learning/models",
#                  model_name="05_going_modular_script_mode_tinyvgg_model.pth")