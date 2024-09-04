#! /bin/bash
from sklearn import tree

# tree -> decision tree

x = [[181,80,44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166,65,40], [190,90,47], [175,64,39],[177,70,40],[171, 75, 42], [181,85, 43]]
male='male'
female='female'
y = [male, female,  female, female, male, male, male, female, female, male]

#dir(tree)

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(x, y)

prediction = classifier.predict([[190, 79,  59]])

print('Prediciton: ' + str(prediction))
