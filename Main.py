import prefix
import pandas
import subprocess
# Your Trie object will be instantiated and called as such:

trie = prefix.Trie()

#read data
data=pandas.read_csv('')


#execute saax representation from R (seewave package). I don't manage to install sax.py package
command = 'C:/Program Files/R/R-3.4.1/bin/Rscript'
path2script = "C:/Users/mauro/Dropbox/R/to_call_from_python.R"

# Variable number of args in a list. in the R script i want to pass also as argument the alphabet size and PAA parameter
args = ['11', '3', '9', '42']

# Build subprocess command
cmd = [command, path2script]+args

# check_output will run the command and store to result. saax_repr: saax_representation of time series.
saax_repr = subprocess.check_output(cmd, universal_newlines=True)
#join in one str
saax_repr= [''.join(i) for i in saax_repr]
#serie_numerica: time series in difference
trie.insert(saax_repr,serie_numerica,3)

#predictions

predictions=trie.predict("c",saax_repr,serie_numerica)
print(predictions)

#Need a tuning.py performance.py files where i can make tuning parameters: (alphabet size and PAA) and evaluate performance.