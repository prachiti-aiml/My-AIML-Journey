#Day 43:Pandas GroupBy

import pandas as pd

#Creating sample DataFrame
data = {
    "Name":["Prachiti","Asha","Riya","Sam","Tom","Neha","Raj","Priya"],
    "City":["Mumbai","Delhi","Mumbai","Chennai","Delhi","Mumbai","Chennai","Delhi"],
    "Course":["AI/ML","CS","IT","AI/ML","CS","IT","AI/ML","CS"],
    "Marks":[78,85,92,60,75,88,45,95],
    "Age":[18,19,20,18,21,19,22,20]
}
df = pd.DataFrame(data)
print("DataFrame:\n",df)

#1.Basic groupby
print("\n      GroupBy City       ")
city_groups = df.groupby("City")
print("Mean marks by city:\n",city_groups["Marks"].mean())

#2.Multiple aggregations
print("\nMultiple stats by city:\n",
      df.groupby("City")["Marks"].agg(["mean","max","min","count"]))

#3.GroupBy multiple columns
print("\nGroupBy City and Course:\n",
      df.groupby(["City","Course"])["Marks"].mean())

#4.GroupBy multiple columns
print("\nAverage age by course:\n",
      df.groupby("Course")["Age"].mean())

print("\nMax marks by course:\n",
      df.groupby("Course")["Marks"].max())

#5.size() - count of records per group
print("\nNumber of students per city:\n",
      df.groupby("City").size())

#6.transform() - apply group stats back to original df
df["City_avg_marks"] = df.groupby("City")["Marks"].transform("mean")
print("\nWith city average marks:\n",df)

#7.filter() - filter groups based on condition
high_avg_cities = df.groupby("City").filter(lambda x: x["Marks"].mean() > 75)
print("\nCities with average marks > 75:\n",high_avg_cities)

#Mini Project:Sales Report by Region
sales_data = {
    "Salesperson": ["Asha","Riya","Sam","Tom","Neha","Raj","PRiya","Prachiti"],
    "Region": ["North","South","North","East","South","East","North","South"],
    "Product": ["Laptop","Phone","Laptop","Tablet","Phone","Laptop","Tablet","Phone"],
    "Sales": [50000,30000,45000,25000,35000,60000,40000,28000]
}

sales_df = pd.DataFrame(sales_data)

print("\n     SALES REPORT BY REGION      ")
print("Total sales by region:\n",
      sales_df.groupby("Region")["Sales"].sum())
print("\nAverage sales by region:\n",
      sales_df.groupby("Region")["Sales"].mean())
print("\nBest Product per region:\n",
      sales_df.groupby("Region")["Sales"].max())
print("\nSales count by product:\n",
      sales_df.groupby("Product")["Sales"].count())