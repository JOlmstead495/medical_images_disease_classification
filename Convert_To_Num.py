def convert_series_to_float(df):
    '''
    The function will convert every data point in your data frame from a string to a float if possible. If the string
    can't be converted the function will continue on. This is called by wrapper function convert_wrapper().
    
    Parameters:
        df (pandas dataframe): The dataframe that will be converted.
        
    Returns:
        None
    
    '''
    columns=df.columns
    for i in columns:
        try:
            df[i]=df[i].map(lambda x:float(x))
        except Exception:
            pass
        else:continue
    return

def convert_series_to_int(df):
    '''
    The function will convert every data point in your data frame from a string to a int if possible. If the string
    can't be converted the function will continue on. This is called by wrapper function convert_wrapper().
    
    Parameters:
        df (pandas dataframe): The dataframe that will be converted.
        
    Returns:
        None
    
    '''
    columns=df.columns
    for i in columns:
        try:
            df[i]=df[i].map(lambda x:int(x))
        except Exception:
            pass
        else:continue
    return

def convert_wrapper(df,to_int=True):
    '''
    The acts as a wrapper to call convert_series_to_int or convert_series_to_float depending on the what is passed
    into to_int.
    
    Parameters:
        df (pandas dataframe): The dataframe that will be converted.
        to_int (boolean): If True the dataFrame will get converted to int, if False the dataFrame will get converted
        to float.
        
    Returns:
        None
    
    '''
    if to_int:
        convert_series_to_int(df)
    else:
        convert_series_to_float(df)