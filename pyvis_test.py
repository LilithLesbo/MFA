from pyvis.network import Network

net = Network()
net.add_node(0, label='a')
net.add_node(1, label='b')
net.add_edge(0, 1, title='edge')
