import os
import numpy as np
import matplotlib.pyplot as pl

files = ["Spikes_Brunnel_A.txt", "Spikes_Brunnel_B.txt", "Spikes_Brunnel_C.txt", "Spikes_Brunnel_D.txt"]
for f in files:
	data = np.genfromtxt(f)
	select= np.array([d for d in data if d[1] < 30])
	data1= select.transpose()
	
	pl.subplot(211)
	pl.title(f)
	pl.scatter(0.1*data1[0],data1[1],alpha=0.8, edgecolors='none');
	pl.xlabel('time [ms]', color = 'black')
	pl.ylabel('neuron ID', color='black')

	pl.subplots_adjust(hspace=0.3)
	pl.subplot(212)
	data = data.transpose()
	n, bins, patches = pl.hist(0.1*data[0], 180, normed=0, alpha=0.75)
	pl.xlabel('time (ms)', color = 'black')
	pl.ylabel('frequency', color = 'black')
	output_filename = os.path.splitext(f)[0] + '.png'
	pl.savefig(output_filename)
	pl.show();


