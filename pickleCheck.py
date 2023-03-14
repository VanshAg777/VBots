import pickle
import constants as c

with open('data/fitnessValues{0}_{1}.pkl'.format(str(c.numpyseed), str(c.randomseed)), 'rb') as f:
    fitness = pickle.load(f)
    print(fitness)
    print(len(fitness))
    f.close()