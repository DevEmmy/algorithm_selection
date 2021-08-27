# algorithm_selection

# Algorithm Selection
This is a Python Program that helps to select the ML Algorithm which has the highest r2_score from sklearn metrics.

## How to Use:
 To use this program, just clone it to your pc in your desired directory and run the git command :
 - git clone https://github.com/DevEmmy/algorithm_selection and there you have the program on your pc
 
 then to use it:
  firstly import it and call the function from it:
  - from algorithm_selection import AlgorithmSelection
  
  Then the next you do is call the function and add the models as a list and add the train and test variables in the following way
   - model = AlgorithmSelection([LinearRegression(), DecisionTreeRegressor()],train_X, test_X, train_y, test_y )
   
  Then by printing the 'model' as above will print the algorithm with the highest r2_score
   - print(model)
   
   Snippet:
   - from algorithm_selection import AlgorithmSelection
   - model = AlgorithmSelection(models = [LinearRegression(), DecisionTreeRegressor()],train_X=train_X, test_X=test_X, train_y=train_y, test_y=test_y )
   - print(model) 
   
   I hope you like this <3
