import numpy as np
import matplotlib.pyplot as plt

np.random.seed(73)
x = np.random.randint(100,size = (10,10))
y = np.random.randint(10, size = (1,10))

def standardize(array):
    if array.shape[0] != 1:
        array = (array - array.mean())/np.std(array, axis = 0)
    else:
        array = (array - array.mean())/np.std(array, axis = 1)        
    return array

def norm(array):
    norm_array = array / np.linalg.norm(array)
    return norm_array

def weight_init(mean = 0, stdev = 0.0006, size = (1,1), mode = 'normal'):
    if mode == 'normal':
        weight = np.random.normal(loc = mean, scale = stdev, size = size)
        #weight = np.random.randn(size[0], size[1]) * np.sqrt(1/size[1])
    elif mode == 'xavier':
        weight = np.random.randn(size[0], size[1]) * np.sqrt(2/(size[0] + size[1]))
    else:
        print("Invalid Mode")
    return weight

def loss(y, yp):
    n = y.shape[1]
    loss = (1/(2 * n)) * np.sum(np.square(yp - y))
    dyp = 1/n * (yp - y)
    #mean_loss = loss.mean()
    return loss, dyp

class LinearLayer:
    
    def __init__(self, insize, neurons, weight_init_mode = 'normal', activation = "ReLU"):
        self.insize = insize[0]
        self.neurons = neurons
        self.weights = weight_init(mode = weight_init_mode, size = (self.neurons, self.insize))
        self.bias = weight_init(mode = weight_init_mode, size = (1,1))
        self.out = np.zeros((self.neurons, insize[1]))
        if activation == 'ReLU':
            self.Act = ReLU(self.out.shape)
        elif activation == 'sigmoid':
            self.Act = Sigmoid(self.out.shape)
        
    def forward(self, inp):
        self.inp = inp
        self.out = np.dot(self.weights, inp) + self.bias
        self.Act.forward(self.out)
    
    def backward(self, ugrad):
        self.Act.backward(ugrad)
        ugrad_act = self.Act.dact
        self.dweight = np.dot(ugrad_act, self.inp.transpose()) #x.transpose is partial derivative at linear layer x
        self.dbias = np.sum(ugrad_act, axis = 1, keepdims = True)
        self.dlin = np.dot(self.weights.transpose(), ugrad_act)
    
    def update(self, learning_rate = 0.0001):
        self.weights = self.weights - learning_rate * self.dweight
        self.bias = self.bias - learning_rate * self.dbias
        
class Sigmoid:
    
    def __init__(self, size):
        self.size = size
        self.out = np.zeros(size)
        
    def forward(self, inp):
        self.out = 1/(1 + np.exp(-inp))
        
    def backward(self, ugrad):
        self.dact = ugrad * self.out * (1 - self.out)
        
class ReLU:
    
    def __init__(self, size):
        self.out = np.zeros(size)
        
    def forward(self, inp):
        self.out = inp * (inp > 0)
        
    def backward(self, ugrad):
        self.dact = ugrad * 1. * (self.out>0)

x = norm(x)
y = norm(y)

w_mode = 'normal'
learning_rate = 0.01
n_epochs = 1000
loss_list_norm = []

#network architechture
layer1 = LinearLayer(x.shape, 5, weight_init_mode = w_mode, activation = "sigmoid")
#layer1_act = Sigmoid(layer1.out.shape)
layer2 = LinearLayer(layer1.out.shape, 1, weight_init_mode = w_mode, activation = "sigmoid")
#layer2_act = Sigmoid(layer2.out.shape)

for epoch in range(n_epochs):
    
    #Layer1 -forward prop
    layer1.forward(x)
    #layer1_act.forward(layer1.out)
    #Layer2 - forward prop
    layer2.forward(layer1.out)
    #layer2_act.forward(layer2.out)
    
    #Computing loss and starting gradient descent
    L, dy = loss(y = y, yp = layer2.out)
    loss_list_norm.append(L)
    
    if epoch % 100 == 0:
        print("Loss at epoch#{0} : {1}".format(epoch, L))
    
    #Layer2 - backward prop
    #layer2_act.backward(dy)
    layer2.backward(dy)
    #Layer1 - backward prop
    #layer1_act.backward(layer2.dlin)
    layer1.backward(layer2.dlin)
    
    #updating weights and biases
    layer2.update(learning_rate = learning_rate)
    layer1.update(learning_rate = learning_rate)
    
plt.plot(loss_list_norm)
plt.ylabel("Train Loss")
plt.xlabel("Epochs")
plt.show()