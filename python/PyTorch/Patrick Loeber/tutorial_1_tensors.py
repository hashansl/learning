import torch

#empty tensor
#x = torch.empty(2,3)
#print(x)

#zeroes ones can be created

#Default float32
x = torch.ones(2,2)
#print(x.dtype)
#print(x.size())

#tensor addition
x1 = torch.rand(2,2)
x2 = torch.rand(2,2)
z = x1+x2
#print(z)

#OR
z= x1.add_(x2)

#slicing
x = torch.rand(5, 3)
#print(x[:,0])

#if we have tensor with one element we can call .item method(only work for one element)
print(x[1,1].item())

#resize tensors
#1D
y = x.view(15)
#Auto one dimention
y = x.view(-1,5)
print(y.size())

