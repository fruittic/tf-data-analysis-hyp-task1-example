import pandas as pd
import numpy as np


chat_id = 224851402 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  alpha = 0.07
  count = np.array([x_success, y_success])
  nobs = np.array([x_cnt, y_cnt])
  zstat, p_value = proportions_ztest(count=count, nobs=nobs, alternative='larger')
  return p_value < alpha
