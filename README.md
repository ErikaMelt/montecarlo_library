# Montecarlo Library

montecarlo-library is a Python library that contains montecarlo simulations functions used in hyphotesis testing such as:

***Permutation Test:***
Also called re-randomization test is an exact statistical hypothesis test making use of the proof by contradiction. A permutation test involves two or more samples. 
The null hypothesis is that all samples come from the same distribution {\displaystyle H_{0}:F=G}{\displaystyle H_{0}:F=G}. Under the null hypothesis, the distribution of the test statistic is obtained by calculating all possible values of the test statistic under possible rearrangements of the observed data. 

***Bootstrap Sample***
Bootstrap Sampling is a method that involves drawing of sample data repeatedly with replacement from a data source to estimate a population parameter.


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

