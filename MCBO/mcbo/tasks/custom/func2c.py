import numpy as np
import pandas as pd
from typing import List, Dict, Any
from mcbo.tasks.task_base import TaskBase

# Helper functions
def myrosenbrock(X):
    X = np.asarray(X).reshape((-1, 2))
    x1, x2 = X[:, 0], X[:, 1]
    fx = 100 * (x2 - x1 ** 2) ** 2 + (x1 - 1) ** 2
    return fx.reshape(-1, 1) / 300

def mysixhumpcamp(X):
    X = np.asarray(X).reshape((-1, 2))
    x1, x2 = X[:, 0], X[:, 1]
    term1 = (4 - 2.1 * x1 ** 2 + (x1 ** 4) / 3) * x1 ** 2
    term2 = x1 * x2
    term3 = (-4 + 4 * x2 ** 2) * x2 ** 2
    fval = term1 + term2 + term3
    return fval.reshape(-1, 1) / 10

def mybeale(X):
    X = (np.asarray(X) / 2).reshape((-1, 2))
    x1, x2 = X[:, 0] * 2, X[:, 1] * 2
    fval = (1.5 - x1 + x1 * x2) ** 2 + (2.25 - x1 + x1 * x2 ** 2) ** 2 + (2.625 - x1 + x1 * x2 ** 3) ** 2
    return fval.reshape(-1, 1) / 50

# MCBO Custom Task Definition
class Func2C(TaskBase):
    
    @property
    def name(self) -> str:
        return 'Func2C'

    def evaluate(self, x: pd.DataFrame) -> np.ndarray:
        y = np.zeros((len(x), 1))  # will be filled with evaluations
        
        for ind in range(len(x)):
            x_ind = x.iloc[ind].to_dict()  # convert to a dictionary
            
            # Extract the nominal parameters (ht0, ht1) and continuous parameters (x0, x1)
            ht_list = [x_ind['ht0'], x_ind['ht1']]
            X_cont = [x_ind['x0'], x_ind['x1']]
            
            # Mathematical operations from original Func2C
            assert len(ht_list) == 2
            X = np.atleast_2d(X_cont) * 2
            ht1, ht2 = ht_list[0], ht_list[1]

            # First categorical choice
            if ht1 == 0:
                f = myrosenbrock(X)
            elif ht1 == 1:
                f = mysixhumpcamp(X)
            else:
                assert ht1 ==2 
                f = mybeale(X)

            # Second categorical choice
            if ht2 == 0:
                f = f + myrosenbrock(X)
            elif ht2 == 1:
                f = f + mysixhumpcamp(X)
            else:
                f = f + mybeale(X)

            # Add evaluation noise
            y_val = f + 1e-6 * np.random.rand(f.shape[0], f.shape[1])
            y[ind, 0] = y_val.astype(float)[0, 0]
            
        return y

    def get_search_space_params(self) -> List[Dict[str, Any]]:
        # Define 2 nominal variables (ht0, ht1) with categories 0, 1, 2
        params = [{'name': f'ht{i}', 'type': 'nominal', 'categories': [0, 1, 2]} for i in range(2)]
        
        # Define 2 continuous variables (x0, x1) with bounds [-1.0, 1.0]
        params.extend([{'name': f'x{i}', 'type': 'num', 'lb': -1.0, 'ub': 1.0} for i in range(2)])
        
        return params

class Func3C(TaskBase):
    
    @property
    def name(self) -> str:
        return 'Func3C'

    def evaluate(self, x: pd.DataFrame) -> np.ndarray:
        y = np.zeros((len(x), 1)) 
        
        for ind in range(len(x)):
            x_ind = x.iloc[ind].to_dict() 
            
            # Extract 3 nominal parameters (ht0, ht1, ht2) and 2 continuous parameters (x0, x1)
            ht_list = [x_ind['ht0'], x_ind['ht1'], x_ind['ht2']]
            X_cont = [x_ind['x0'], x_ind['x1']]
            
            assert len(ht_list) == 3
            X = np.atleast_2d(X_cont) * 2
            ht1, ht2, ht3 = ht_list[0], ht_list[1], ht_list[2]

            # First categorical choice
            if ht1 == 0:
                f = myrosenbrock(X)
            elif ht1 == 1:
                f = mysixhumpcamp(X)
            else:
                f = mybeale(X)

            # Second categorical choice
            if ht2 == 0:
                f = f + myrosenbrock(X)
            elif ht2 == 1:
                f = f + mysixhumpcamp(X)
            else:
                f = f + mybeale(X)
                
            # Third categorical choice (Specific to Func3C)
            if ht3 == 0:
                f = f + 5 * mysixhumpcamp(X)
            elif ht3 == 1:
                f = f + 2 * myrosenbrock(X)
            else:
                f = f + ht3 * mybeale(X)

            # Add evaluation noise
            y_val = f + 1e-6 * np.random.rand(f.shape[0], f.shape[1])
            y[ind, 0] = y_val.astype(float)[0, 0]
            
        return y

    def get_search_space_params(self) -> List[Dict[str, Any]]:
        # Define 3 nominal variables (ht0, ht1, ht2) with categories 0, 1, 2
        params = [{'name': f'ht{i}', 'type': 'nominal', 'categories': [0, 1, 2]} for i in range(3)]
        
        # Define 2 continuous variables (x0, x1) with bounds [-1.0, 1.0]
        params.extend([{'name': f'x{i}', 'type': 'num', 'lb': -1.0, 'ub': 1.0} for i in range(2)])
        
        return params