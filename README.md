# Assignment: Build a Linear Regression Model to Predict Stock 'Open' Prices

In this task, you are required to create a **linear regression model** that takes specific stock market features and predicts the **'open' price**. The data provided to you contains the following columns: **'high', 'low', 'close', 'adj close', and 'volume'**. Your responsibility is to use these columns as input features (**independent variables**) to train a linear regression model that outputs the **'open' price** (**dependent variable**).

## Requirements

Your code will need to:

- Read in the dataset and extract the columns **'high', 'low', 'close', 'adj close', and 'volume'** as the input (**X**).
- Set the **'open' price** as the target variable (**y**) that we aim to predict.
- Split the dataset into **appropriate training and testing sets** 
- Create and **fit a linear regression model** to the training data.
- Use the trained model to **predict 'open' prices** on the test set and save it to a file.
- Use the `tests.py` file to create a testing class which is able to compute various different metrics of your prediction
- Combine your results in `main.py` to import `linear-regression.py` and `tests.py` to maintain a clean, modular workflow

The end goal is to produce predictions in the shape of an **n×1 dimensional vector** (or tensor), where each element corresponds to a forecasted **'open' price** for a single data point. Ensure that your code is well-documented and modular, so others can easily read, maintain, and build upon your work.

## Best Practices and Expectations

- Check the dataset for **missing or anomalous values**, and handle these issues appropriately (e.g., **imputation, removal, or other data-cleaning steps**).
- Clearly **separate data-preprocessing steps** from model training and prediction steps.
- Provide **clear function definitions and docstrings**. This will help your colleagues understand the logic and flow of data through the code.
- Include basic **performance metrics** such as:
  - **Mean Squared Error (MSE)**
  - **Mean Absolute Error (MAE)**  
  These will help evaluate how well your model performs.

By following these guidelines, you will create a **reproducible and efficient workflow** that highlights your ability to transform stock market data into **actionable predictive insights**. 

If you have any questions or run into any issues, please reach out for clarification or assistance.
