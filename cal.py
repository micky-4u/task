#  Converting for percentage to decimal 
# percentage value as p_value



def cal(p_value):
    """
    this function converts the prcentage value to its corresponding decimal value
    using the tracking:
    2.5 as 32%
    3.9 as 100%
    
    """
    result = round(((p_value + 89.5)/48.6),1)
    
    print(result)

    

cal(83)
