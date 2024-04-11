import torch

weights = torch.ones(4, requires_grad=True)

for epoch in range(3):
    model_output = (weights*3).sum()
    model_output.backward()

    print(weights.grad)

#this is actually wrong. Gradients adds up each iteration
print('--------------------------------------')

weights = torch.ones(4, requires_grad=True)

for epoch in range(3):
    model_output = (weights*3).sum()
    model_output.backward()

    print(weights.grad)

    #this is really important
    #MUST EMPTY the gradients
    weights.grad.zero_()