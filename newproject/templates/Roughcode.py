#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 12:22:44 2017

@author: ryno
"""


########Rough pieces of code for other scripts


#feature extraction for sklearn svm

X= [{'A': 1, }

}]

from sklearn.feature_extraction import DictVectorizer
vect = DictVectorizer(sparse= False).fit(X)
print(vect.transform(X))
print ("feature names: %s" % vect.get_feature_names() )