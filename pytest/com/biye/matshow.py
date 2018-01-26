import numpy as np
import h5py
f = h5py.File('snapshot_iter_2500.caffemodel.h5','r')
for key in f.keys():
    data=f['data']
    for dkey in data.keys():
        filename = dkey
        layer=data[dkey]
        for lkey in layer.keys():
            filename = filename+"_"+lkey
            dataset=layer[lkey]
            print(lkey,dataset)
            newdata=dataset.value
            savedata=newdata.reshape(-1)
            np.savetxt(filename,savedata)