def mean_encoding(df, cols, target):
	"""
	This function encode columns with the technique known as mean/target/likelihood encoding. It should be 
	called when a feature has many classes / high cardinality. one hot encoding would create too many dimensions

	Parameters
	----------
	df     : Pandas dataframe : The original dataset you want to encode
	cols   : list of strings  : The column string names you want to encoded. It should be encapsulated in a list.
	target : string           : the string name of the target column you want to use to encode the predictor columns

	Returns
	-------
	pandas-data
	"""
	
	for c in cols:
		means = df.groupby(c)[target].mean()
		df[c] = df[c].map(means)

	return df
	
	
def ci_and_point_estimate(data_dict, name):
    """
    This function calculate the confidence_interval of a bootstrap sample. 

    Parameters
    ----------
    data_dict : dictionary : A dictionary containing string key and list values pairs
    name      : string     : the name of the statistic being point estimated

    Returns
    -------
    dictionary with keys as the column name and values as confidence_interval, point_estimate
    """
    statistic = {'statistic_name': name}
    
    for i in data_dict.items():   
        sample = np.array(i[1])
        sample_mean = i[1].mean()
        z_critical = st.norm.ppf(0.975)
        sigma = i[1].std()
        standard_error = sigma/np.sqrt(i[1].size)
        margin_of_error = z_critical * standard_error/np.sqrt(i[1].size)
        confidence_interval = (sample_mean-margin_of_error, sample_mean+margin_of_error)

        statistic[i[0]] =[confidence_interval, sample_mean]
        
    return statistic