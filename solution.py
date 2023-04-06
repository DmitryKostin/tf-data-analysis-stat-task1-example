import pandas as pd
import numpy as np


chat_id = 944932368

def solution(x: np.array) -> float:
    n = len(x)  
    t = 30  
    sample_mean = np.mean(x)  
    lambda_hat = sample_mean / t
    return lambda_hat
