from random import random,seed,randint

classes = [i for i in range(10)]
dataset = [randint(0,9) for i in range(int(input('Enter input set size.\n')))]
frequency_observed = [dataset.count(classes[index]) for index in range(10)]
frequency_expected = len(dataset)/len(classes)
deviation = [frequency_observed[index]-frequency_expected for index in range(10)]
deviation_squared = [deviation[index]**2 for index in range(10)]
normalized = [deviation_squared[index]/frequency_expected for index in range(10)]
summation = sum(normalized)

print("Classes\n",classes,"\n\n",
	"Dataset\n",dataset,"\n\n",
	"Frequency Observed",frequency_observed,"\n\n",
	"Frequency Expected",frequency_expected,"\n\n",
	"Deviation",deviation,"\n\n",
	"Deviation Squared",deviation_squared,"\n\n",
	"Normalized",normalized,"\n\n",
	"Summation",round(summation,2),"\n\n")

if(summation>-0.05 and summation<16.9):
	print("Valid.")
else:
	print("Invalid.")