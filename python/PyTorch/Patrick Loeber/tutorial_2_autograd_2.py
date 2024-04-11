import torch

x = torch.randn(3, requires_grad=True)
print(x)

#multiple ways to do this
#x.reqired_grad(False)
#x.detach()
# with torch.no_grad():
x.requires_grad(False) 
print(x)
