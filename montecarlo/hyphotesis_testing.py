import numpy as np
import pandas as pd

def generate_bootstrap_values(data, estimator, sample_size=None, n_samples=None,
                              random_seed=None, verbose=False, **kwargs) -> list:
    """_summary_

    Parameters
    ----------
    data : list
        The list of values to generate the bootstrap values
    estimator : string
        The estimator to use it can be mean or median
    sample_size : number, optional
        The sample size to use, by default None
    n_samples : number, optional
        The number of iterations, by default None
    random_seed : number, optional
        The reference point or seed, by default None
    verbose : bool, optional
        To print the output of the process, by default False

    Returns
    -------
    list
        List of bootstrap values generated
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
    x : float
        _description_
    y : float
        _description_
    estimator : string
        _description_
    n_iter : number, optional
        _description_, by default None
    two_sided : bool, optional
        _description_, by default True
    random_seed : number, optional
        The reference point or seed, by default None
    verbose : bool, optional
        To print the output of the process, by default False

    Returns
    -------
    list
        The list of sample values 

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
    test : number
        The value to test
    data : number
        The data to test
    alpha : float, optional
        The significance level, by default 0.05

    Returns
    -------
    list
        The list with the p-value and the evaluation True or False
    """   
    bootstrap_values = np.array(data)
    p_value = len(bootstrap_values[bootstrap_values < test]) / len(bootstrap_values)

    p_value = np.min([p_value, 1. - p_value])

    return [p_value, p_value < alpha] 