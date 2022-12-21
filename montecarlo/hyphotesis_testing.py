import numpy as np
import pandas as pd

def generate_bootstrap_values(data, estimator, sample_size=None, n_samples=None,
                              random_seed=None, verbose=False, **kwargs) -> list:
    """_summary_

    Parameters
    ----------
    data : _type_
        _description_
    estimator : _type_
        _description_
    sample_size : _type_, optional
        _description_, by default None
    n_samples : _type_, optional
        _description_, by default None
    random_seed : _type_, optional
        _description_, by default None
    verbose : bool, optional
        _description_, by default False

    Returns
    -------
    list
        _description_
    """
    if sample_size is None:
        sample_size = 10 * len(data)

    if n_samples is None:
        n_samples = 10 * len(data)

    if random_seed is not None:
        np.random.seed(random_seed)

    bootstrap_values = [estimator(data, **kwargs)]
    for _ in np.arange(n_samples):
        sample = np.random.choice(data, size=sample_size, replace=True)  # Repeticiones aleatorias 

        if verbose:
            print(sample)

        bs = estimator(sample, **kwargs)
        bootstrap_values.append(bs)

    return bootstrap_values

def generate_permutation_samples(x, y, estimator, n_iter=None, two_sided=True,
                                 random_seed=None, verbose=False, **kwargs) -> list:
    """_summary_

    Parameters
    ----------
    x : _type_
        _description_
    y : _type_
        _description_
    estimator : _type_
        _description_
    n_iter : _type_, optional
        _description_, by default None
    two_sided : bool, optional
        _description_, by default True
    random_seed : _type_, optional
        _description_, by default None
    verbose : bool, optional
        _description_, by default False

    Returns
    -------
    list
        _description_

    Raises
    ------
    ValueError
        _description_
    """ 
    if n_iter is None:
        n_iter = (len(x) + len(y)) * 10

    if n_iter < 0: 
      raise ValueError("Value cannot be negative")
  
    if random_seed is not None:
        np.random.seed(random_seed)

    conc_sample = list(x) + list(y)
    batch_1 = len(x)
    batch_2 = len(x) + len(y)
  
    samples = [estimator(x, **kwargs) - estimator(y, **kwargs)]

    
    for _ in np.arange(n_iter):
        perm_sample = np.random.choice(conc_sample, size=len(conc_sample))

        if verbose:
            print(perm_sample)
    
        this_sample = estimator(
            perm_sample[:batch_1], **kwargs) - estimator(
                perm_sample[batch_1:batch_2], **kwargs)
            
        samples.append(this_sample)

    if two_sided:
        samples = [np.abs(s) for s in samples]


    return samples

def get_pvalue(test, data, alpha=0.05) -> list:
    """_summary_

    Parameters
    ----------
    test : _type_
        _description_
    data : _type_
        _description_
    alpha : float, optional
        _description_, by default 0.05

    Returns
    -------
    list
        _description_
    """   
    bootstrap_values = np.array(data)
    p_value = len(bootstrap_values[bootstrap_values < test]) / len(bootstrap_values)

    p_value = np.min([p_value, 1. - p_value])

    return [p_value, p_value < alpha] 