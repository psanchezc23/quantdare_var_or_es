def value_at_risk(assets_returns, confidence_level=.05):
	"""
	It calculates the Value at Risk (VaR) of some time series. It represents 
	the maximum loss with the given confidence level.
	
	:param pandas.DataFrame assets_returns: Returns of each asset. It could be daily, weekly, monthly, ...
	:param int confidence_level: Confidence level. 5% by default.
	
	:return var: Value at Risk for each asset.
	:rtype: pandas.Series
	
	"""
	
	# Calculating VaR
	var =  assets_returns.quantile(confidence_level, axis=0, interpolation='higher')
	
	return var
