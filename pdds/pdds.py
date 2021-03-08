import os
import pandas as pd
import matplotlib.pyplot as plt


@pd.api.extensions.register_dataframe_accessor('dataset')
class Dataset:

  """Pandas DataFrame extension to analyse dataset for classification.

  Ex:
    import pandas as pd
    from pdds import pdds

    folder = 'my_images'

    df = pd.DataFrame()
    (df.dataset
      .from_folder(folder)
      .label_by_parent_folder()
      .split_by_stratification(k=4, origin='train', to='valid')
      .split_by_stratification(k=4, origin='train', to='test')
    )

    df.dataset.plot_splits()
    
    df.dataset.count_occurrences()
  """

  def __init__(self, pandas_obj):
    self._obj = pandas_obj


  @property
  def classes(self):
    "Returns the list of classes found in dataset."
    labels = self.labels
    return sorted(list(set(self.labels))) if labels is not None else None


  @property
  def splits(self):
    "Returns the list of splits defined in dataset."
    return sorted(list(set(self._obj['split'].values))
    ) if 'split' in self._obj.columns else None


  @property
  def labels(self):
    "Returns the list of string containing the labels."
    return self._obj['label'].values if 'label' in self._obj.columns else None


  @property
  def y(self):
    "Returns the list of labels encoded as integers."
    classes = self.classes
    labels = self.labels
    return [classes.index(l) for l in labels] if (
        (classes is not None) and (labels is not None)) else None


  def count_occurrences(self):
    "Returns dictionary with counts of samples grouped by label."
    return self._obj[['filepath', 'label']].groupby('label').count()


  def plot_occurrences(self, **kwargs):
    "Plots the counts of samples grouped by label."
    self.count_occurrences().plot.bar(legend=None, **kwargs)


  def count_splits(self):
    "Returns dictionary with counts of samples grouped by types of split."
    return self._obj.groupby(['label', 'split']).count().unstack()


  def plot_splits(self, **kwargs):
    "Plots the count of samples grouped by types of split."
    self.count_splits().plot.bar(**kwargs)
    cols = self.count_splits().columns
    plt.legend(self.splits)


  def split_by_stratification(self, k=1, *,
          origin='train', to='valid',
          overwrite=False,
          ):
    """Splits dataset flipping 'k' samples (or less if not enough) per label.
    
    Args:
      k (int, default 1): maximum samples of every label to flip to new split.
      origin (str, default 'train'): split type from which some will be flipped.
      to (str, default 'valid'): split type the flipped samples will flipped to.
      overwrite (bool, default False): removes previous splits. 
    """
    if overwrite or 'split' not in self._obj.columns:
      self._obj['split'] = origin

    for cls in self.classes:
      mask = (self._obj.label == cls) & (self._obj.split == origin)
      df_cls = self._obj[mask].sample(k)
      self._obj.loc[self._obj.index.isin(df_cls.index), 'split'] = to
      self._obj[self._obj.label == cls]

    return self


  def from_folder(self, folder, include=None, exclude=None):
    """Lists every file in folder and subfolders as sample for dataset.
    
    Args:
      folder (str): absolute path to root of dataset files and subfolders.
      include (list of str, optional): only include filepaths containing these substrings.
      exclude (list of str, optional): exclude all filepaths containing these substrings.
    """

    self.folder = folder
    self.include = include
    self.exclude = exclude

    filepaths = []

    # crawl files in subfolders      
    for root, dirs, files in os.walk(self.folder):
      for file in files:
        filepath = os.path.join(root, file)
        
        add_filepath = True
        if self.include is not None:
          add_filepath = any((_inc in filepath
                                for _inc in self.include))
        if add_filepath:
          if self.exclude is not None:
            add_filepath = all((_exc not in filepath
                                  for _exc in self.exclude))

        if add_filepath:
          #append the file name to the list of paths
          filepaths.append(filepath)

    self._obj['filepath'] = filepaths
    
    return self


  def label_by_function(self, func):
    """Labels each sample by a function with filepath as argument (lambda file:).

    Args:
      func (lambda function): returns class label (str) from argument filepath.
    """
    self._obj['label'] = [func(f) for f in self._obj.filepath]
    return self


  def label_by_parent_folder(self):
    """Labels each sample by the name of its parent folder.

    Args:
      func (lambda function): returns class label (str) from argument filepath.
    """
    return self.label_by_function(lambda fname: fname.split('/')[-2])
