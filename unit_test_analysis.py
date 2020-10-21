import VyPRAnalysis as va
import os
"""

Script for generating CI performance testing data by using data from VyPR Analysis Library

"""

"""Initialize db and set monitoring service"""


va.prepare(os.getcwd()+'/data/verdicts.db', logging=True)


"""dictionary of property"""
verdict_data = {}

"""Getting list of all unit tests and functions """

metadata_unit_tests = va.list_test_data()
metadata_function = va.list_functions()[0]

"""getting function calls"""
calls = metadata_function.get_calls()

n_of_calls = len(calls)

"""getting measured value and verdict"""
for (n, call) in enumerate(calls):

	observations = call.get_observations()
	
	observed_value = eval(observations[0].observed_value)	
	
	verdicts = call.get_verdicts()

	for verdict in verdicts:
		if verdict.verdict == 0:
			verdict_data[observed_value] = 'Specification Violation' 
		else:
			verdict_data[observed_value] = 'No violation'



print ('------------------------')
print ('Measured Value , Verdict')
print ('------------------------')
for key in verdict_data:
	print("%-6f,%s" %(key, verdict_data[key]))
va.teardown()
