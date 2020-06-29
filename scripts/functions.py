def mean_encoding(df, cols, target):
	for c in cols:
		means = df.groupby(c)[target].mean()
		df[c] = df[c].map(means)

	return df