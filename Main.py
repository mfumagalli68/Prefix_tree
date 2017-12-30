import prefix
import pandas
import subprocess
# Your Trie object will be instantiated and called as such:

trie = prefix.Trie()
#pass data
data=pandas.read_csv('')

command = 'Rscript'
path2script = 'path/to your script/max.R'

# Variable number of args in a list
args = ['11', '3', '9', '42']

# Build subprocess command
cmd = [command, path2script] + args

# check_output will run the command and store to result
saax_repr = subprocess.check_output(cmd, universal_newlines=True)
saax_repr= [''.join(i) for i in saax_repr]
#serie_numerica serie numerica in differenze da prendere dal dataset
trie.insert(saax_repr,serie_numerica,3)

#predictions

predictions=trie.predict("c",saax_repr,serie_numerica)
print(predictions)
