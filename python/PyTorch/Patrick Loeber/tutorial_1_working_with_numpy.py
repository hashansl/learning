import torch
import  numpy as np

#ONLY FOR CPU TENSORS
#Tensor to numpy array
a = torch.ones(5)
#print(type(a))
b = a.numpy()
#print(type(b))
#here both objects share the same memory location

#all underscore functions modify our variables in place!!!!


#Numpy to tensor

c = np.ones(5)
#print(type(c))

d = torch.from_numpy(c)
#print(type(d))

#same memory location


#make tensor in the GPU!!!
if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.ones(5, device = device)

    #OR
    y = torch.ones(5)
    y = y.to(device) 

    #this will perform in the GPU
    z=x+y

    #IMPORTANT
    #if we call z.numpy() this will return an error
    #because numpy can only handle cpu tensors

    z = z.to("cpu")
    #this is going to work!


# most of the time we work with gradients so 
# if we turn this on we can check the grads
# by default it is turned off

x = torch.ones(5, requires_grad=True)
print(x)
