import re

class Cleaner:
							  
	def __init__(self):
		self._expression = {}
		self._expression['usd_pledged'] = re.compile(r'([A-Z]){2}') 
		self._expression['backers'] = ['failed', 'canceled', 'successful', 'live', 'undefined', 'suspended']
		self._expression['pledged'] = re.compile(r'[\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:?[\d]{2}:?[\d]{2}:?') 
		self._expression['goal'] = re.compile(r'[\d]{4}-[\d]{2}-[\d]{2} [\d]{2}:?[\d]{2}:?[\d]{2}:?') 
		self._expression['deadline'] = re.compile(r'([A-Z]){3}')
		self._expression['currency'] = ['Art', 'Comics', 'Crafts', 'Dance', 'Design', 'Fashion', 'Film & Video', 
										 'Food', 'Games', 'Journalism', 'Music', 'Photography', 'Technology', 'Theater', 
										 'Publishing']
		
	def shift_data_left(self, row):
		"""
		This function checks if there are signs of right shifted data. If right shifted data is detected, 
		the data is shifted to the left to be corrected. If the data was not right shifted no action will be taken.
		
		This method should be called on a matrix the is mostly sorted. 
		
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
		  
		if self._expression['usd_pledged'].match(row['usd_pledged']) != None:
			if row['country'].isnumeric() == True:
				if row['backers'] in self._expression['backers']:
					if row['state'].replace('.','').isnumeric():
						if self._expression['pledged'].match(row['pledged']) != None:
							if row['launched'].isnumeric() == True:
								if self._expression['goal'].match(row['goal']) != None:                         
									if self._expression['deadline'].match(row['deadline']) != None:
										if row['currency'] in self._expression['currency']:
											if self._expression['goal'].match(row['category']) == None:   
												
												#Column 1 is suppose to be apart of column 0, fixed before shifting data left.
												row[0] = row[0] + row[1]
												
												for i in range(1,len(row)-1):
													row[i] = row[i+1]
												
			
		return row