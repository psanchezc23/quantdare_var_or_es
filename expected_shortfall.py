def expected_shortfall(returns, confidence_level=.05):
	"""
	It calculates the Expected Shortfall (ES) of some time series. It represents 
	the average loss according to the Value at Risk.
	
	Parameters
	----------
	returns : pandas.DataFrame
		Returns of each time serie. It could be daily, weekly, monthly, ...
		
	confidence_level : int
		Confidence level. 5% by default.
			
	Returns
	-------
	es : pandas.Series
		Expected Shortfall for each time series.
	
	"""
	
	# Calculating VaR
	var = value_at_risk(returns, confidence_level)
	
	# ES is the average of the worst losses (under var)
	return returns[returns.lt(var, axis=1)].mean()