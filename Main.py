import prefix
import pandas
import subprocess
import re
import string
from array import array


#read data
data=pandas.read_csv('C:/Users/mauro/Documents/time_series.csv')


#execute saax representation from R (seewave package). I don't manage to install sax.py package
command = 'C:/Program Files/R/R-3.4.1/bin/Rscript'
path2script = "C:/Users/mauro/Dropbox/R/to_call_from_python.R"

# Variable number of args in a list. in the R script i want to pass also as argument the alphabet size and PAA parameter

serie_numerica=data['qt']
#args for subprocess call
args = [str(i) for i in serie_numerica]

# Build subprocess command
cmd = [command, path2script]+args

# check_output will run the command and store to result. saax_repr: saax_representation of time series.
saax_repr = list(subprocess.check_output(cmd, universal_newlines=True))

#messy results, got to clean it.
for i in range(1,len(saax_repr)):

    saax_repr[i]=re.sub('\s+', '', saax_repr[i])

    for i in range(1, len(saax_repr)):
        saax_repr[i] = re.sub('[^\w\s]', '', saax_repr[i])

saax_repr=[i for i in saax_repr if i in list(string.ascii_lowercase)]
#join in one str

sax_fin = ''
for f in saax_repr:
    sax_fin = sax_fin + f

#saax_repr=array('B', map(ord,saax_repr)).tostring()

#serie_numerica: time series in difference
# Your Trie object will be instantiated and called as such:
trie=prefix.Trie()
trie.insert(sax_fin,serie_numerica,3)

#predictions

predictions=trie.predict("c",saax_repr,serie_numerica)
print(predictions)
print (serie_numerica[179])
#Need a tuning.py performance.py files where i can make tuning parameters: (alphabet size and PAA) and evaluate performance.