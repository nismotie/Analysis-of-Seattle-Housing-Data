def slope(x, y):
    top = x.mean()*y.mean() - (x*y).mean()
    bottom = x.mean()**2 - (x**2).mean()
    return round(top/bottom, 2)
    
    
def intercept(y, m, x):
    return round(y.mean() - m*x.mean(), 2)

def prediction(pred_m, x, pred_c):
    return pred_m*x + pred_c

def r_sq(y, pred_y):
    mean_y = y.mean()
    ssres = sum((y - pred_y)**2)
    sstot = sum((y-mean_y)**2)
    return round(1 - ssres/sstot, 2)
    
def regression_machine(x, y):
    m = slope(x, y)
    c = intercept(y, m, x)
    pred_y = prediction(m, x, c)
    r2 = r_sq(y, pred_y)
    return print("Slope: {}\nY-intercept: {}\nR-Squared: {}".format(m, c, r2))
