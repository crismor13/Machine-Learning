class MP_Neuron:
    
    def __init__(self):
        self.threshold = None
    
    def model(self, inputData):
        result = sum(inputData)
        return (result >= self.threshold)
        
    def predict(self, dataSet):
        resultSet = []
        for dataArray in dataSet:
            result = self.model(dataArray)
            resultSet.append(result)
        return resultSet

neuron1 = MP_Neuron()
neuron1.threshold = 3

print(neuron1.predict([[1,1,0,1],[1,0,1,0],[0,0,0,1]]))