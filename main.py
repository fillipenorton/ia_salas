import copy

class Node(object):
	func_a = -1
  destinos = []
  custos = []	

class Application(object):
	records = {}
	def init(self):
		while True:
			sala = raw_input()
			fa = int(raw_input())
			self.create(sala, fa)

	def create(self, s, fa):
    node = Node()
    node.func_a = fa
    self._while(node)
    self.records[sala].append(node)
    print self.records

  def _while(self, node):
    destino = 0
    while (destino != -1):
    	destino = raw_input()
    	if destino != -1:
	    	custo = int(raw_input())
				node.destinos.append(destino)
				node.custos.append(custo)
		return node


app = Application()
app.init()  