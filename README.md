# ez_elm V.0.1
Extreme learning machine classifier for python

*just for biner classes

*still not support for multiclass

## installing ezelm
create folder ezelm in your project folder

clone this repo to that folder

    from ezelm import ezelm
    classifier = ezelm.EzELM()
    classifier.train(X,y,n)        // X is matrix input, y is array output, n is total number perseptron in hidden layer
    classifier.pred(X_test)        // return 1 if true, and -1 if false
    

