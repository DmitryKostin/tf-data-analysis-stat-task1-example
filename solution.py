import pandas as pd
import numpy as np


chat_id = 944932368

def solution(x: np.array) -> float:
    n = len(x) 
    t = 30
    sample_mean = np.mean(x) 
    sample_var = np.var(x, ddof=1) 
    lambda_hat = (sample_var - sample_mean) / (t*(n-1))
    return lambda_hat
