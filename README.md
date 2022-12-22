# Montecarlo Library

montecarlo-library is a Python library that contains montecarlo simulations functions used in hyphotesis testing such as:

***Permutation Test:***
Also called re-randomization test is an exact statistical hypothesis test making use of the proof by contradiction. A permutation test involves two or more samples. 
The null hypothesis is that all samples come from the same distribution {\displaystyle H_{0}:F=G}{\displaystyle H_{0}:F=G}. Under the null hypothesis, the distribution of the test statistic is obtained by calculating all possible values of the test statistic under possible rearrangements of the observed data. 

***Bootstrap Sample***
Bootstrapping is any test or metric that uses random sampling with replacement (e.g. mimicking the sampling process), and falls under the broader class of resampling methods. Bootstrapping assigns measures of accuracy (bias, variance, confidence intervals, prediction error, etc.) to sample estimates.[1][2] This technique allows estimation of the sampling distribution of almost any statistic using random sampling methods.[3][4]

Bootstrapping estimates the properties of an estimand (such as its variance) by measuring those properties when sampling from an approximating distribution. One standard choice for an approximating distribution is the empirical distribution function of the observed data. In the case where a set of observations can be assumed to be from an independent and identically distributed population, this can be implemented by constructing a number of resamples with replacement, of the observed data set (and of equal size to the observed data set).

It may also be used for constructing hypothesis tests. It is often used as an alternative to statistical inference based on the assumption of a parametric model when that assumption is in doubt, or where parametric inference is impossible or requires complicated formulas for the calculation of standard errors.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install montecarlo.

```bash
pip install montecarlo
```

## Usage

```python
from montecarlo import hyphotesis_testing

# Generate Bootstrap Sample 
# returns 'list of numbers'
hyphotesis_testing.generate_bootstrap_values(data=list,
                                    estimator=np.median,
                                    sample_size=100,
                                    n_samples=4000,
                                    verbose=True)

# Generate Permutation Samples 
# returns list of values 
data = hyphotesis_testing.generate_permutation_samples(x=values1,
                                    y=values2,
                                    estimator=np.mean,
                                    n_iter=4000)
# Get p-value
# returns a list with the p-value and a bool evaluation value.  
# Example: [0.00024993751562107924, True]
test_val = np.abs(mean diff)
pval = hyphotesis_testing.get_pvalue(test=test_val, data=data)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

