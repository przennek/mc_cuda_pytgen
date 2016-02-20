import RandomArrayGenerator,  SineWithNoiseGenerator, GaussGenerator

def __main__():
	gen1, gen2 = prepareSineGenerators(0.1, 0.1)
	generateDistribution(gen1, gen2, "Sinus_01_01.txt")
		

def generateDistribution(gen1, gen2, genName):
	output_file = open(genName, 'w')	
	arrSize = 1000
	for i in range(0, arrSize):
		try:
			output_file.write(genName)
		except IOError:
			print "I/O error. Aborting..."
		finally:
			output_file.close()        
		data1 = self.gen1.generateDataSample(arrLen)
        	data2 = self.gen2.generateDataSample(arrLen)
	
			

def prepareSineGenerators(noise1, noise2):
	xgen1 = RandomArrayGenerator.RandomArrayGenerator(-10, 10)
	gen1 = SineWithNoiseGenerator.SineWithNoiseGenerator(xgen1, noise1)
	gen2 = SineWithNoiseGenerator.SineWithNoiseGenerator(xgen1, noise2)
	return gen1, gen2

def prepareGaussGenerators(x1, y1, x2, y2, sigma1, sigma2):
	gen1 = GaussGenerator.GaussGenerator(x1, y1, sigma1)
	gen2 = GaussGenerator.GaussGenerator(x2, y2, sigma2)
	return gen1, gen2
