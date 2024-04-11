from customdataset import CatsAndDogsDataset
import torchvision.transforms as transforms
import torchvision
import torch
from torch.utils.data import DataLoader
#https://www.youtube.com/watch?v=ZoZHd0Zm3RY
#load data

dataset = CatsAndDogsDataset(csv_file='cats_dogs.csv', root_dir='cats_dogs_resized',
                             transform = transforms.ToTensor())

train_set,test_set = torch.utils.data.random_split(dataset,[8,2])

#datalaoder loads the data by batch
train_loader = DataLoader(dataset=train_set,batch_size=32,shuffle = True)
test_loader = DataLoader(dataset=test_set,batch_size=32,shuffle = True)


#model

#loss and optimizer

#train network

for epoch in range(num_epochs):
    losses = []

    for batch_idx, (data, targets) in enumerate(train_loader):
        #GET THE DATA TO CUDA IF POSSIBLE
        data = data.to(device=device)
        targets = targets.to(device=device)

        # forward
        scores = model(data)
        loss = criterion(scores, targets)

        losses.append(loss.item())

        #backward
        optimizer.zero_grad()
        loss.backward()

        # gradiant decent or dam step
        optimizer.step()
        
    print(f'Cost at each epoch {epoch} is {sum(Losses)/Len(Losses)}')

#check accuracy on training to see how good our model is

def check_accuracy(loader, model):
    num_correct = 0
    num_samples = 0
    model.eval()

    with torch.no_grad():
        for x, y in loader:
            x = x.to(device=device)
            y = y.to(device=device)

            scores = model(x)
            _, predictions = scores.max(1)
            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)
        #print()...
    model.train()

#print
check_accuracy(train_loader, model)

#print
check_accuracy(test_loader, model)

