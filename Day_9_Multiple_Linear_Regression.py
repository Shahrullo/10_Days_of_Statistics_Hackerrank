import numpy as np

def mul_lin_regression(y, x, x_pred):
    X_t = x.T
    
    X = X_t.dot(x)
    
    X_inv = np.linalg.inv(X) 
    
    X_last = X_inv.dot(X_t)
    
    B = X_last.dot(y)
    
    y_pred = x_pred.dot(B)
    
    return y_pred

def main():
    m, n = map(int, input().strip().split())
    
    y, x, x_pred = [], [], []
    
    for _ in range(n):
        *feat, y_val = map(float, input().strip().split())
        x.append([1] + feat)
        y.append(y_val)
        
    for _ in range(int(input())):
        feat = list(map(float, input().strip().split()))
        x_pred.append([1] + feat)
        
    y = np.array(y)
    x = np.array(x)
    x_pred = np.array(x_pred)
    
    res = mul_lin_regression(y, x, x_pred)
    
    for i in res:
        print(round(i, 2))
        
if __name__ == '__main__':
    main()