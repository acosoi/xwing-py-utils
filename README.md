# xwing-py-utils
A collection of useful Python scripts for X-Wing: The Miniatures Game by Fantasy Flight Games

There's no single purpose to these scripts, they simply function as sort of command-line squad builder and inventory management system.

The scripts are dependent on [xwing-data](https://github.com/guidokessels/xwing-data) by [Guido Kessels](https://github.com/guidokessels) for all of the data and images.

## inventory.py

Takes a list of purchases (defined in `purchases.js`) and generates the user's inventory (see `output.md` for an example of what is generated based on the current contents of `purchases.js`)

Example usage:

```
python inventory.py
```

`inventory.py` has a couple of hardcoded paths that will be removed from the source code in a later commit:

```
printer = MarkdownPrinter('../xwing-data/images')
dataDirectory = '../xwing-data/data/'
```
