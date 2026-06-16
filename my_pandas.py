import pandas as pd
data = {
    "Name" : ["vivek", "leoset", "sher", "saurabh"],
    "Marks" : [98,68,79,67],
    "City" : ["Bhopal", "Indore","Rewa","Bhopal"],
    "Age" : [22,23,19,20]
}
df = pd.DataFrame(data)
# print("df['Name']:\n",df['Name'])
# print(df[df['Marks'] >= 85])
# print("----------")
# def get_grade(x):
#     if x>= 90:
#         return "A"
#     elif x>= 75:
#         return "B"
#     else:
#         return "C"
# df['Grade'] = df['Marks'].apply(get_grade)
# print(df["Grade"])
# print("------------")
# print(df)
# city = df.groupby('City')['Marks'].mean()
# print(city)
# print("_________")
# print(df.groupby('City')['Marks'].mean())

# Example of a decorator
# def my_decorator(func):
#     def wrapper():
#         print("Something before the function runs.")
#         func()
#         print("Something after the function runs.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

df2 = pd.read_csv('stud.csv')
#Cleaning 
specal = r'[^a-zA-Z0-9]'
# num = r'[^0-9]'
df2.to_csv('clean_output.csv',index = False)
df2['Name'] = df2['Name'].str.strip()
df2 = df2.replace(r'\.','',regex= True)
df2['Marks'] = df2['Marks'].astype(str).str.replace(specal,'',regex=True)
df2['Age'] = df2["Age"].astype(str).str.extract(r'(\d+)')
print(df2)
df2.to_csv('clean_output.csv', index=False)
