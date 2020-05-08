from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            res = prefixNode.suffixes('', [])
            if res is not None:
                print('\n'.join(prefixNode.suffixes('', [])))
            else:
                print("no suffixes")
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');
