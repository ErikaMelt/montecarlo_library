import numpy as np
import pandas as pd

def generate_permutation_samples(x, y, estimator, n_iter=None, two_sided=True,
                                 random_seed=None, verbose=False, **kwargs) -> list:
    """_summary_

    Parameters
    ----------
    x : list of floats
        One list of samples to permute 
    y : list of floats 
        Second list of samples to permute
    estimator : statistic estimator mean, median. 
        The statistic function to use 
    n_iter : integer, optional
        The number of iterations, by default None
    two_sided : bool, optional
        The comparison for the null hyphotesys, by default True
    random_seed : float, optional
        the seed, by default None
    verbose : bool, optional
        Display the function information, by default False

    Returns
    -------
    list
        List of samples values calculated based on the estimator
    """

    samples=[]
 
    if n_iter is None:
        n_iter = (len(x) + len(y)) * 10

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

def generate_bootstrap_values(data, estimator, sample_size=None, n_samples=None,
                              random_seed=None, verbose=False, **kwargs):

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

def get_pvalue(test, data, alpha=0.05):
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
    _type_
        _description_
    """    
  
    bootstrap_values = np.array(data)
    p_value = len(bootstrap_values[bootstrap_values < test]) / len(bootstrap_values)

    p_value = np.min([p_value, 1. - p_value])

    return [p_value, p_value < alpha] 

path = '/Users/eo/src/montecarlo_library/montecarlo/tests/data/server_requests.csv'
df = pd.read_csv(path, sep=",")
print(df)


data = generate_permutation_samples(x=df[df.day_type=="workday"].seconds_since_last,
                                    y=df[df.day_type=="weekend"].seconds_since_last,
                                    estimator=np.mean,
                                    n_iter=4000)


print(data)