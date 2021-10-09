import re, gc, json, time, socket
import pandas
from datetime import datetime

class Main : 
	_baseUrl = 'sample.json' # Json file name and path#
	_weight = 'WeightKg' # Weight column name (In Kg) #
	_height = 'HeightCm' # Height column name (In Cm) #
	
	def __init__(self, name):
		self.name = name
		print('Job execution for '+self.name+' get started on '+str(time.strftime('%Y-%m-%dT%H:%M:%S')))
		gc.collect()
		
	# Function for read json file using pandas
	# Returns the data as dataframe
	def loadJson(self,):
		try:
			baseUrl = self._baseUrl
			return pandas.read_json(baseUrl)
		except Exception as e:
			print('Json not loaded properly')
			raise
	
	# Function for return function for BMI (Body Mass Index)
	# Set 'cm' parameter value true if weight column in centimeter otherwise false for meter
	def bmiFunction(self, df, cm=False):
		try:
			#print('BMI calculation started')
			if cm:
				return (df[self._weight]/((df[self._height]/100)*2))
			else:
				return (df[self._weight]/(df[self._height]*2))
		except Exception as e:
			print('Error in BMI calculation !! ')
			raise
	
	# Function return the person category based on BMI value
	def categoryFn(self, x):
		try:
			#print('Category evaluation started')
			if (x <= 18.4) : return 'Underweight'
			elif (18.5 <= x <= 24.9) : return 'Normalweight'
			elif (25.0 <= x <= 29.9) : return 'Overweight'
			elif (30.0 <= x <= 34.9) : return 'Moderately obese'
			elif (35.0 <= x <= 39.9) : return 'Severely obese'
			elif (40.0 <= x) : return 'Very severely obese'
			else : return 'Not Valid'
		except Exception as e:
			print('Error in category evaluation !! ')
			raise
	
	# Function return the person Health Risk based on BMI value
	def healthRiskFn(self, x):
		try:
			#print('HealthRisk evaluation started')
			if (x <= 18.4) : return 'Malnutrition risk'
			elif (18.5 <= x <= 24.9) : return 'Low risk'
			elif (25.0 <= x <= 29.9) : return 'Enhanced risk'
			elif (30.0 <= x <= 34.9) : return 'Medium risk'
			elif (35.0 <= x <= 39.9) : return 'High risk'
			elif (40.0 <= x) : return 'Very high risk'
			else : return 'Not Valid'
		except Exception as e:
			print('Error in healthRisk evaluation !! ')
			raise
	
	# Function for Creating BMI column and append its value
	def addBMI(self, df):
		try:
			print('Creating BMI column')
			df['BMI'] = self.bmiFunction(df,True)
			print('BMI values Appended')
			return df
		except Exception as e:
			print('Error in creating BMI column !!')
			raise
	
	# Function for Creating Category column and append its value
	def addCategory(self, df):
		try:
			print('Creating Category column')
			df['Category'] = df['BMI'].apply(lambda x: self.categoryFn(x))
			print('Category column values Appended')
			#print(df)
			return df
		except Exception as e:
			print('Error in creating Category column !!')
			raise
	
	# Function for Creating Health Risk column and append its value
	def addHealthRisk(self, df):
		try:
			print('Creating HealthRisk column')
			df['HealthRisk'] = df['BMI'].apply(lambda x: self.healthRiskFn(x))
			print('HealthRisk column values Appended')
			#print(df)
			return df
		except Exception as e:
			print('Error in creating Health Risk column !!')
			raise
	
	# Main function 
	def startprocess(self, name=None):
		try:
			print('Reading Json')
			json = self.loadJson()
			print('Adding BMI Column in the table')
			columnBMI = self.addBMI(json)
			print('BMI column Added')
			print('Adding category Column in the table')
			category = self.addCategory(columnBMI)
			print('Category column Added')
			print('Adding Health Risk Column in the table')
			risk = self.addHealthRisk(category)
			print('Health Risk column Added')
			richdata = risk
			print (richdata)
			print('Process completed')
		except Exception as e:
			raise
		
	def __del__(self,):
		print('Job execution for '+self.name+' finished on '+str(time.strftime('%Y-%m-%dT%H:%M:%S')))
		del self
		gc.collect()

if __name__ == "__main__": 
	name = "BMI calculator process started "+ str(socket.gethostbyname(socket.gethostname()))
	try:
		# Invoke startprocess funtion of main class 
		Main(name).startprocess('') 
	except Exception as e:
		print(e)