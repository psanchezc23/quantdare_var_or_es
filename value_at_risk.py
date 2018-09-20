def value_at_risk(returns, confidence_level=.05):
	"""
	It calculates the Value at Risk (VaR) of some time series. It represents 
	the maximum loss with the given confidence level.
	
	Parameters
	----------
	returns : pandas.DataFrame
		Returns of each time serie. It could be daily, weekly, monthly, ...
		
	confidence_level : int
		Confidence level. 5% by default.
			
	Returns
	-------
	var : pandas.Series
		Value at Risk for each time series.
	
	"""
	
	# Calculating VaR
	return returns.quantile(confidence_level, axis=0, interpolation='higher')