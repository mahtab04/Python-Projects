from sklearn.neighbors import KNeighborsClassifier

#[Height,Weight,Shoesize]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

#Fit trains the model
clf = KNeighborsClassifier()
clf = clf.fit(X, Y)

#prediction
prediction = clf.predict([[170,87,37]])

#print output
print(prediction)