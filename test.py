import paddle.fluid as fluid

image = fluid.data(name="image", shape=[None, 784], dtype='float32')
label = fluid.data(name="label", shape=[None, 1], dtype='int64')
hidden = fluid.layers.fc(input=image, size=100, act='relu')
prediction = fluid.layers.fc(input=hidden, size=10, act='softmax')
loss = fluid.layers.cross_entropy(input=prediction, label=label)
loss = fluid.layers.mean(loss)

sgd = fluid.optimizer.SGD(learning_rate=0.001)
sgd.minimize(loss)

print("test paddle")