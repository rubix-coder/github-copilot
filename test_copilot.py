"""Linear Regression"""

def linear_regression(x, y):
    """
    Summary:
        Linear regression of y = ax + b
    Args:
        x (numpy.ndarray): x-coordinates of points to be fit
        y (numpy.ndarray): y-coordinates of points to be fit
    Returns:
        tuple: tuple containing:
            a (float): slope of the regression line
            b (float): y-intercept of the regression line
            r (float): correlation coefficient
    """
    # TODO: Calculate linear regression
    a = np.sum(x*y)/np.sum(x**2)
    b = np.sum(y)/np.sum(x**2)
    r = np.sum((y-a*x-b)**2)/np.sum((y-np.mean(y))**2)
    return a, b, r

def loss(y, y_hat):
    """Summary
    Args:
        y (numpy.ndarray): Array containing actual y-coordinates
        y_hat (numpy.ndarray): Array containing predicted y-coordinates
    Returns:
        float: loss
    """
    # TODO: Calculate loss
    loss = np.sum((y-y_hat)**2)/len(y)
    return loss

def gradient(x, y, a, b):       
    """Summary       
    Args:       
        x (numpy.ndarray): x-coordinates of points to be fit       
        y (numpy.ndarray): y-coordinates of points to be fit       
        a (float): slope of the regression line       
        b (float): y-intercept of the regression line       
    Returns:       
        tuple: tuple containing:       
            da (numpy.ndarray): Derivative w.r.t. a (slope)       
            db (numpy.ndarray): Derivative w.r.t. b (y-intercept)       
    """       
    # TODO: Calculate gradient       
    da = np.sum((y-a*x-b)*x)/len(x)       
    db = np.sum((y-a*x-b))/len(x)       
    return da, db


"""Trying out openCV"""

def load_image(path, grayscale=False):       
    """Summary       
    Args:       
        path (str): Path to image       
        grayscale (bool): True loads image as grayscale, False loads image as color       
    Returns:       
        numpy.ndarray: Image loaded from path       
    """       
    # TODO: Load image       
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) if grayscale else cv2.imread(path)       
    return img

def apply_filter(img, kernel):       
    """Summary       
    Args:       
        img (numpy.ndarray): Image to be filtered       
        kernel (numpy.ndarray): Filter to be applied       
    Returns:       
        numpy.ndarray: Filtered image       
    """       
    # TODO: Define kernel size       
    kernel_size = kernel.shape[0]       
    # TODO: Define padding       
    padding = int((kernel_size-1)/2)       
    # TODO: Pad image with appropriate amount of zeros       
    img = np.pad(img, (padding, padding), 'constant', constant_values=(0, 0))       
    # TODO: Define window size       
    window_size = int(img.shape[0]/kernel_size)       
    # TODO: Define stride value       
    stride = int(window_size/2)       
    # TODO: Apply filter to each window       
    filtered_img = np.zeros(img.shape)       
    for i in range(img.shape[0]):       
        for j in range(img.shape[1]):       
            filtered_img[i, j] = np.sum(img[i:i+window_size, j:j+window_size]*kernel)       
    # TODO: Remove padding       
    filtered_img = filtered_img[padding:filtered_img.shape[0]-padding, padding:filtered_img.shape[1]-padding]       
    return filtered_img