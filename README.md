# &#x2615; Tools for classification dataset 

This Pandas extension provides additional tools to analyse and handle a dataset for a classification task in Machine Learning. It is an useful complement for other frameworks such as PyTorch or FastAI.


<p>&nbsp;</p>

# &#9196; Install

This module can be installed directly from the github repository by running the following:
```
!pip install --upgrade git+git://github.com/diogodutra/pandas_dataset.git
```

Next, import the `pdds` module to your Python code after importing Pandas:
```
import pandas as pd
from pdds import pdds
```

Alternatively, the repository can be cloned to a local folder but the import is a bit nastier and it is not covered in this tutorial.


<p>&nbsp;</p>

# &#128187; Usage

Now your Pandas DataFrames are supercharged with additional methods in the new `dataset` namespace, as shown on the example below:


```
df = pd.DataFrame()

(df.dataset
  .from_folder('my_classified_images')
  .label_by_parent_folder()
  .split_by_stratification(k=4, origin='train', to='valid')
  .split_by_stratification(k=4, origin='train', to='test')
)

df.dataset.plot_splits() 
```

Other remarkable tools are crawling files in subfolders, getting indices of subsets (ie: split, class) and plotting counts of samples grouped by different criteria. Know all properties and methods with `help(df.dataset)`.

<p>&nbsp;</p>

# 📬 Get in touch

Feel free to contact me at anytime should you need further information about this project or for any other Machine Learning and Data Scientist:
- &#128100; Personal Web: [diogodutra.github.io](https://diogodutra.github.io)
- ![](https://i.stack.imgur.com/gVE0j.png) LinkedIn: [linkedin.com/in/diogodutra]()