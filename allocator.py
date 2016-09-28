class region:
	def __init__(self,regionName,servers):
		self.name = regionName
		availableServers = []
		for i in servers:
			availableServers.append(server(servers[i],i)
		self.priceSortedServers = sorted(priceSortedServers,key=lambda ser:ser.price_per_cpu)
		
		#add server class, add sorting function

class server:
	def __init__(self,price,server_type):
		self.price = price
		self.server_type = server_type.lower()
		if self.server_type == 'large':
			self.cpus = 1
		elif self.server_type == 'xlarge':
			self.cpus = 2
		elif self.server_type == '2xlarge':
			self.cpus = 4
		elif self.server_type == '4xlarge':
			self.cpus = 8
		elif self.server_type == '8xlarge':
			self.cpus = 16
		elif self.server_type == '10xlarge':
			self.cpus = 32
		else:
			raise Exception('Server type "'+self.server_type+'" not recogonized')
		self.price_per_cpu = self.price/self.cpus
		
def calculateCostWithCpus(regionName,priceList,totalCount):
	regionServers = region(regionName,priceList)
	result = []
	serverLeft = totalCount
	sortedServerStack = list(regionServers.priceSortedServers)
	while serverLeft > 0:
		if sortedServerStack[0].cpus <= serverLeft and sortedServerStack[0].price <= sortedServerStack[1].price:
			result.append((i.server_type,(serverLeft/i.cpus) + 1))
			serverLeft = 0
		elif sortedServerStack[0].cpus <= serverLeft:
			result.append((i.server_type, serverLeft/i.cpus))
			serverLeft = serverLeft % i.cpus
			
		sortedServerStack.pop(0)
	
	return result


def calculateCostWithPrice(regionName,priceList,maxPrice,hours):
	regionServers = region(regionName,priceList)
	result = []
	serverLeft = totalCount
	sortedServerStack = list(regionServers.priceSortedServers)
	pricePerHour = maxPrice/hours
	


def get_costs(instances,hours,cpus=None,price=None):
	if cpus == None and price == None:
		raise Exception("Error. No.of cpus and max price can't be both empty")
		return
	result = []
	for regionName in instances:
		resultDict = calculateCostWithCpus(regionName,instances[regionName],cpus)
		
	
	
