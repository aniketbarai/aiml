from sklearn.linear_model import LinearRegression

x = []
y = []

n = int(input("Enter number of data points: "))

for i in range(n):
    a = float(input("Enter X value: "))
    b = float(input("Enter Y value: "))
    x.append([a])
    y.append(b)

model = LinearRegression()
model.fit(x, y)

value = float(input("Enter X value to predict: "))
result = model.predict([[value]])

print("Predicted Y value:", result[0])