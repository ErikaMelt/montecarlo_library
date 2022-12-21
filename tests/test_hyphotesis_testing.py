#!/usr/bin/env python

"""Tests for `dataprocess` package."""

import pytest
import pandas as pd
import numpy as np 

from montecarlo import hyphotesis_testing

PERMUTATION = 'Permutation'
BOOTSTRAP = 'Bootstrap'

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

def get_df(type):
    if type == PERMUTATION:
        path = './tests/data/server_requests.csv'
        return pd.read_csv(path, sep=",")
    else:
        path = './tests/data/web_traffic.csv'
        return pd.read_csv(path, sep=",")

def test_bootstrap_sample():
    df = get_df(BOOTSTRAP)
    medians = hyphotesis_testing.generate_bootstrap_values(data=df.total_visits,
                                    estimator=np.median,
                                    verbose=False)
    assert len(medians) == 611

def test_generate_permutation_samples():
    df = get_df(PERMUTATION)
    data = hyphotesis_testing.generate_permutation_samples(x=df[df.day_type=="workday"].seconds_since_last,
                                        y=df[df.day_type=="weekend"].seconds_since_last,
                                        estimator=np.mean,
                                        n_iter=4000)

    test_val = np.abs(df[df.day_type=="workday"].seconds_since_last.mean() - df[df.day_type=="weekend"].seconds_since_last.mean())
    pval = hyphotesis_testing.get_pvalue(test=test_val, data=data)

    assert pval[0]  == 0.00024993751562107924

