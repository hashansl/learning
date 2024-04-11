import torch

x = torch.randn(5, requires_grad=True)
# print(x)

#pytorch will create a computaional graph for us
y = x+2

# print(y)

z = y*y*2
z =z.mean()
# print(z)


z.backward() #dz/dx gradiant of z with respect to x

# if z is not an sclar value we need to give set of data inside backward()

print(x.grad)
print(y.grad)


