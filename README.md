# ANT
Machine Learning plugin for Rhino\grasshopper based on Python\ [scikit-learn](http://scikit-learn.org/) module.
![scikit_grass](https://cloud.githubusercontent.com/assets/6969514/26666295/73118c52-469f-11e7-9c9b-b2f44c41ab3a.png)

![image](https://user-images.githubusercontent.com/6969514/29434744-9754a562-83a4-11e7-95ce-7ae55a254bd1.png)

## Goal.
This project aims to develop a machine learning plugin for Rhino\Grasshopper by making use of the well-known Python module (Scikit-learn) using Rhnio-Common C# and python programming language to bring sophisticated Machine-Learning supervised and unsupervised learning methods to be handy to regular designers and architects. It is open source and is released under BSD "simplified" licence.

![sphx_glr_plot_classifier_comparison_001](https://user-images.githubusercontent.com/6969514/29195926-8023baae-7e31-11e7-93af-4c3d946cc451.png)
image source : [scikit-learn website](http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html#sphx-glr-auto-examples-classification-plot-classifier-comparison-py)

# Supports:
## 1. Linear Models: 
![image](https://user-images.githubusercontent.com/6969514/29232437-e488b232-7eeb-11e7-9c93-98e4a1b2ea71.png)

                1. ARDRegression ---- Bayesian ARD regression.
                2. BayesianRidge ---- Bayesian ridge regression
                3. ElasticNet ---- Linear regression with combined L1 and L2 priors as regularizer.
                4. ElasticNetCV ---- Elastic Net model with iterative fitting along a regularization path
                5. Lars ---- Least Angle Regression model a.k.a.
                6. LarsCV ---- Cross-validated Least Angle Regression model
                7. Lasso ---- Linear Model trained with L1 prior as regularizer (aka the Lasso)
                8. LassoCV ---- Lasso linear model with iterative fitting along a regularization path
                9. LassoLars ---- Lasso model fit with Least Angle Regression a.k.a.
                10. LassoLarsCV ---- Cross-validated Lasso, using the LARS algorithm
                11. LassoLarsIC ---- Lasso model fit with Lars using BIC or AIC for model selection
                12. LinearRegression ---- Ordinary least squares Linear Regression.
                13. LogisticRegression ---- Logistic Regression (aka logit, MaxEnt) classifier.
                14. LogisticRegressionCV ---- Logistic Regression CV (aka logit, MaxEnt) classifier.
                15. MultiTaskLasso ---- Multi-task Lasso model trained with L1/L2 mixed-norm as regularizer
                16. MultiTaskElasticNet ---- Multi-task ElasticNet model trained with L1/L2 mixed-norm as regularizer
                17. MultiTaskLassoCV ---- Multi-task L1/L2 Lasso with built-in cross-validation.
                18. MultiTaskElasticNetCV ---- Multi-task L1/L2 ElasticNet with built-in cross-validation.
                19. OrthogonalMatchingPursuit ---- Orthogonal Matching Pursuit model (OMP)
                20. OrthogonalMatchingPursuitCV ---- Cross-validated Orthogonal Matching Pursuit model (OMP)
                21. PassiveAggressiveClassifier ---- Passive Aggressive Classifier
                22. PassiveAggressiveRegressor ---- Passive Aggressive Regressor
                23. Perceptron 
                24. RandomizedLasso ---- Randomized Lasso.
                25. RandomizedLogisticRegression ---- Randomized Logistic Regression
                26. RANSACRegressor ---- RANSAC (RANdom SAmple Consensus) algorithm.
                27. Ridge ---- Linear least squares with l2 regularization.
                28. RidgeClassifier ---- Classifier using Ridge regression.
                29. RidgeClassifierCV ---- Ridge classifier with built-in cross-validation.
                30. RidgeCV ---- Ridge regression with built-in cross-validation.
                31. SGDClassifier ---- Linear classifiers (SVM, logistic regression, a.o.) with SGD training.
                32. SGDRegressor ---- Linear model fitted by minimizing a regularized empirical loss with SGD
                33. TheilSenRegressor ---- Theil-Sen Estimator: robust multivariate regression model.
                34. lars_path ---- Compute Least Angle Regression or Lasso path using LARS algorithm [1]
                35. lasso_path ---- Compute Lasso path with coordinate descent
                36. lasso_stability_path ---- Stability path based on randomized Lasso estimates
                37. logistic_regression_path ---- Compute a Logistic Regression model for a list of regularization parameters.
                38. orthogonal_mp ---- Orthogonal Matching Pursuit (OMP)
                39. orthogonal_mp_gram ---- Gram Orthogonal Matching Pursuit (OMP)
## 2. Support Vector Machines
![image](https://user-images.githubusercontent.com/6969514/29232457-f94e15fe-7eeb-11e7-90c0-6129a6969e99.png)

		1.Support Vector Classifier SVC
                2.Linear Support Vector Classifier LinSVC
                3.Nu Support Vector Classifier NuSVC
                4.Support Vector Regression SVR
                5.Linear Support Vector Regression LinSVR
                6.Nu Support Vector Regression NuSVR
                7.One Class Support Vector Machines
## 3. Decision Trees
![image](https://user-images.githubusercontent.com/6969514/29233405-e90e07bc-7ef0-11e7-8a97-2680267abc12.png)

                1. DecisionTreeClassifier ------ A decision tree classifier.
                2. DecisionTreeRegressor  ------  A decision tree regressor.
                3. ExtraTreeClassifier ------   An extremely randomized tree classifier.
                4. ExtraTreeRegressor ------    An extremely randomized tree regressor.
## 4. Nearest Neighbors
![image](https://user-images.githubusercontent.com/6969514/29234176-7d74135c-7ef5-11e7-946d-25f6680f4aca.png)

                1. (Not Supported Yet) NearestNeighbors -------- Unsupervised learner for implementing neighbor searches. 
                2. KNeighborsClassifier --------  Classifier implementing the k-nearest neighbors vote.
                3. (Not Supported Yet) RadiusNeighborsClassifier --------  Classifier implementing a vote among neighbors within a given radius
                4. KNeighborsRegressor --------   Regression based on k-nearest neighbors.
                5. RadiusNeighborsRegressor --------   Regression based on neighbors within a fixed radius.
                6. NearestCentroid --------   Nearest centroid classifier.
                          (IN PROGRESS ... )
                //7. BallTree -------- BallTree for fast generalized N-point problems
                //8. KDTree  -------- KDTree for fast generalized N-point problems
                //9. LSHForest --------   Performs approximate nearest neighbor search using LSH forest.
                //11. KernelDensity--------    Kernel Density Estimation
                //12. kneighbors_graph --------  Computes the (weighted) graph of k-Neighbors for points in X
                //13. radius_neighbors_graph -------- Computes the (weighted) graph of Neighbors for points in X
