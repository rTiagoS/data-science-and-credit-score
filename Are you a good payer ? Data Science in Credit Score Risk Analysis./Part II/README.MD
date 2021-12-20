# Data Science and Credit Risk Modeling - Part II

In this section, our goal is to present some interesting preprocessing steps before train a model to infer the probability of default. Generally, when starting to learn about Data Science, courses prefer to uses only Python to do the whole pipeline. Buuut, that's not all the true. Following are the reasons.

When dealing with Big Data, most of the time, it is not possible to download the dataset to perform preprocessing steps, because it requires so much computational time and space resources. Then, to handle this issue, you are required to perform some preprocessing steps directly on the SQL server - local where the dataset is stored. 
Considering the scenario above, that's what we are going to do: some of the preprocessing steps with Big Query SQL and some if Python. 

(Por uma imagem do pipeline completo aqui ou na parte I).
an application involving a complete machine learning pipeline to infer the probability of default for a given credit borrower. To achieve this goal, the most common data science tools will be used, such as Python and its main data science libs, Big Query SQL and deployment with StreamLit.
In general, consumer loans and credit cards are the most typical retail products where credit risk modelling is applied. 

Our example: Consumer Loans
Dataset used: Lending Club Loan Data (pesquisar mais detalhes sobre ele aqui).

 - - - - - - - - - - - - - - - 
We are going to build a probability of default model, a loss given default model and exposure at default model. All of these will be regression models.


Part II consist of two main phases:

Phase 01: Lending Club dataset preprocessing by using Big Query SQL.

Phase 02: Using phase 01 as starting point , we are going perform others statistical preprocessing steps, but now using some specifics data science tools - Apache Spark and Python.

We are going to deal with Discrete (Categorical, FIni number of values) and Continuous variables (Numerical), infinite numbers of values).

Therefore, the preprocessing for the PD model would consist in transforming all independent variables into suitable categorical variables.


Phase 01 - Details


-> 


Phase 02 - Details

-> Using the dataset proprocessed in phase 01, now we are going prepare it to be trained using a logistic regression classifier. To reach this goal, some statistical preprocessing steps will be executed before. These steps are going to be implemented through popular datascience libs and tools, such as Python, PySpark and others.

-> The established statistical methodology to model probability of default is a logistic regression.
-> The logistic regression estimates the relationship between two things, the logarithm of odds of an outcome of dependente variables and a linear combination of predictors.

-> When it comes to PD models, interpreteability is extremely important as it is required by the regulators. That's why we are using dummy variables. (Binary categorical values).

-> To categorical variables, it was easy to transform them into dummy variables. But and about continuous variables ? That's not very simples. We also need to transform them into categorical variables, but, to do that, it will be extremaly necessary statistical analysis.

-> Just after finishing this step, we are finally ready to fit the dataset in a logistic regression classifier. 
