# ez_elm
Extreme learning machine classifier for python

create folder ezelm in you project folder

from ezelm import ezelm
classifier = ezelm.EzELM()
classifier.train(X,y,n)        // X is matrix input, y is array output, n is total number perseptron in hidden layer
classifier.pred(X_test)        // return 1 if true, and -1 if false
