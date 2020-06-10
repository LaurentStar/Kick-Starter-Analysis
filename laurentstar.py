import re

class Cleaner:
							  
	def __init__(self):
		self._expression = {}
		self._expression['country'] = re.compile(r'([A-Z]){2}')
		self._expression['state'] = ['failed', 'canceled', 'successful', 'live', 'undefined', 'suspended']
		self._expression['deadline & launched'] = re.compile(r'[\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:?[\d]{2}:?[\d]{2}:?') 
		self._expression['currency'] = re.compile(r'([A-Z]){3}') 
		self._expression['main_category'] = ['Art', 'Comics', 'Crafts', 'Dance', 'Design', 'Fashion', 'Film & Video', 
												 'Food', 'Games', 'Journalism', 'Music', 'Photography', 'Technology', 'Theater', 
												 'Publishing']


	def shift_data_left(self, row):
		
		"""
		self function checks if there are signs of right shifted data. If right shifted data is detected, 
		the data is shifted to the left to be corrected. If the data was not right shifted no action will be taken.

		self method should be called on a matrix the is mostly sorted. 

		Parameters
		----------
			row : an pandas series or row from a pandas dataframe

		Big-O-Notation Estimate
		-----------------------
			Best:         O(n)    //Fair-er-ish....
			Average:      O(n)    //Fair...
			Worst:        O(n^2)  //OUCH!!!

		Returns
		-------
			pandas-series, 1D-array, dataframe-row : The dataframe row with swapped around data.


		INPUT <<<<      df = pd.DataFrame({'numbers' : [1, 2, 3, 4, 'i'], 'letters' : ['a', 'b', 'c', 'd', 5]}) 
						data_swap(df.iloc[0])

		OUTPUT >>>>     {'numbers' : [1, 2, 3, 4, 5], 'letters' : ['a', 'b', 'c', 'd', 'i']}
		"""
		
		
		shift = 0 # The number of times the data was potentially shifted to the right. This is potentially not accually detected.
		
		if isinstance(row['Unnamed:16'],float):
			shift = 4
		elif isinstance(row['Unnamed:15'], float):
			shift = 3
		elif isinstance(row['Unnamed:14'], float):
			shift = 2
		elif isinstance(row['Unnamed:13'], float):
			shift = 1
			
		# This create a list of column names in the correct order to check if data was shifted. The order is important for this check.
		cols = tuple(row.index[::-1][shift:]) 
		
		# These if statement check if the data was shifted at any point it messes up the data wasn't shifted.
		if shift > 0:   
			# should contain a datatype that usd_pledged would have
			if isinstance(row[cols[0]], float):
				
				if self._expression['country'].match(row[cols[1]]) != None:
					
					#Should contain a datatype expected in the backers columns
					if row[cols[2]].isnumeric():
											
						if row[cols[3]] in self._expression['state']:
							
							# Should contain a dataetype expected in pledged
							if row[cols[4]].isnumeric() == True:
								
								if self._expression['deadline & launched'].match(row[cols[5]]) != None:
									
									# Check for datatype expected in goal
									if row[cols[6]].isnumeric():
										
										if self._expression['deadline & launched'].match(row[cols[7]]) != None:
								
											if self._expression['currency'].match(row[cols[8]]) != None:                         
																						  
												if row[cols[9]] in self._expression['main_category']:                                                                                  
													for i in range(shift):
														row['name'] += ' ' + row[i+1]

													for i in range(1,len(cols)):
														row[i] = row[i+shift]
														
													for i in range(len(cols)+1, len(row)):
														row[i] = ''
		return row