#importing Covid from Covid library
from covid import Covid
#intialization Covid()
#covid is variable using for intializating
covid = Covid()
#printing the status of country by country name,eg:india, using covid.  type of inbuild funct
cases = covid.get_status_by_country_name("india")
#output is in dictionary form so using for loob for printing in standard form
for x in cases:
#using print function
print(x,"=",cases[x])
