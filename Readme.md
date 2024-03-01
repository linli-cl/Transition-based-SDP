# Transition based Statistical Dependency Parsing

1. Introduction:

Dependency parsing is a fundamental task in Natural Language Processing (NLP), which focuses on analyzing the syntactic structure of sentences by parsing the dependencies between words. 

The main goal of this project is to implement a dependency parser based on a transition-based system in statistical methods, trained on English and German data in CoNLL06 format. Finally, the obtained parser and model are used to analyze the English and German test datasets to obtain the dependency relations for each word in each sentence and return the analysis result file.

2. Overview
* Decoding algorithm:	    Transition-based, ArcStandard(has three transitions: left arc, right arc and shift).
* The feature model: 	    Based on Niver(2008) and Zhang and Niver(2011).
    * Integrating Graph-Based and Transition-Based Dependency Parsers, Niver(2008)
    * Transition-based Dependency Parsing with Rich Non-local Features, Niver(2011)
* Machine learning method: Multi-class perceptron.
* Evaluation : 		    Unlabeled attachment score(UAS).

3. Project Specification

Please see the file "Transition-based_Project Report.pdf"