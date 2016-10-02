

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
			raise Exception('Server type "'+self.server_type+'" not recognised')
		self.price_per_cpu = self.price/self.cpus


class region:
	def __init__(self,regionName,servers):
		self.name = regionName
		self.availableServers = []
		for i in servers:
			self.availableServers.append(server(servers[i],i))
		self.priceSortedServers = sorted(self.availableServers,key=lambda ser:ser.price_per_cpu)
		
def calculateCostWithCpus(regionName,priceList,totalCount,hours):
	regionServers = region(regionName,priceList)
	result = []
	serverLeft = totalCount
	totalCost = 0
	sortedServerStack = list(regionServers.priceSortedServers)
	while serverLeft > 0:
		if sortedServerStack[0].cpus <= serverLeft and sortedServerStack[0].price <= sortedServerStack[1].price:
			result.append((sortedServerStack[0].server_type,int(serverLeft/sortedServerStack[0].cpus) + 1))
			totalCost += (int(serverLeft/sortedServerStack[0].cpus) + 1)*sortedServerStack[0].price
			serverLeft = 0
		elif sortedServerStack[0].cpus <= serverLeft:
			result.append((sortedServerStack[0].server_type, int(serverLeft/sortedServerStack[0].cpus)))
			serverLeft = serverLeft % sortedServerStack[0].cpus
			totalCost += (int(serverLeft/sortedServerStack[0].cpus))*sortedServerStack[0].price
		sortedServerStack.pop(0)
	return {'region':regionName, 'total_cost':totalCost * hours, 'servers':result}


def calculateCostWithPrice(regionName,priceList,maxPrice,hours):
	regionServers = region(regionName,priceList)
	result = []
	#serverLeft = totalCount
	sortedServerStack = list(sorted(regionServers.availableServers,key=lambda ser:ser.price))
	pricePerHour = float(maxPrice)/float(hours)
	totalCost = 0
	while pricePerHour > 0 and sortedServerStack:
		if sortedServerStack[0].price <= pricePerHour:
			totalCost += int(pricePerHour/sortedServerStack[0].price) * sortedServerStack[0].price
			result.append((sortedServerStack[0].server_type, int(pricePerHour/sortedServerStack[0].price)))
			pricePerHour = pricePerHour % sortedServerStack[0].price
		sortedServerStack.pop(0)
	
	return {'region':regionName, 'total_cost':totalCost*hours, 'servers':result}

def calculateCostWithPriceAndCpu(regionName,priceList,maxPrice,minCpu, hours):
	regionServers = region(regionName,priceList)
	cpuHired = 0
	moneyLeft = float(maxPrice)/float(hours)
	result = []
	totalCost = 0
	cpuPriceSortedList = list(regionServers.priceSortedServers)
	while cpuHired < minCpu and cpuPriceSortedList:
		if cpuPriceSortedList[0].price <= moneyLeft:
			cpuHired += cpuPriceSortedList[0].cpus * int(moneyLeft/cpuPriceSortedList[0].price)
			totalCost += int(moneyLeft/cpuPriceSortedList[0].price) * cpuPriceSortedList[0].price
			result.append((cpuPriceSortedList[0].server_type,int(moneyLeft/cpuPriceSortedList[0].price)))
			moneyLeft = moneyLeft % cpuPriceSortedList[0].price
		cpuPriceSortedList.pop(0)
        return {'region':regionName, 'total_cost':totalCost*hours,'servers':result}


def get_costs(instances,hours,cpus=None,price=None):
	if cpus == None and price == None:
		raise Exception("Error. No.of cpus and max price can't be both empty")
		return
	result = []
	if price and cpus:
		for regionName in instances:
			result.append(calculateCostWithPriceAndCpu(regionName,instances[regionName],price,cpus,hours))
	elif price:
		for regionName in instances:
			result.append(calculateCostWithPrice(regionName, instances[regionName],price,hours))
	elif cpus:
		for regionName in instances:
			result.append(calculateCostWithCpus(regionName, instances[regionName], cpus,hours))
	return result
		
	
	
