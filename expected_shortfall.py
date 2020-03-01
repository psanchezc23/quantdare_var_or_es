def expected_shortfall(assets_returns, confidence_level=.05):
	"""
	It calculates the Expected Shortfall (ES) of some time series. It represents 
	the average loss according to the Value at Risk.
	
	:param pandas.DataFrame assets_returns: Returns of each asset. It could be daily, weekly, monthly, ...
	:param int confidence_level: Confidence level. 5% by default.
	
	:return expected_shortfall: Expected Shortfall for each time series.
	:rtype: pandas.Series
	
	"""
	
	# Calculating VaR
	var = value_at_risk(assets_returns, confidence_level)
	
	# ES is the average of the worst losses (under var)
	expected_shortfall = assets_returns[assets_returns.lt(var, axis=1)].mean()
	
	return expected_shortfall
