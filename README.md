# Assignment: Build a Linear Regression Model to Predict Titanic Passenger's Survival

In this task, you are required to create a **linear regression model** that takes passenger features on the Titanic and predicts their survival. The data provided to you contains various columns. Your responsibility is to use these columns as input features (**independent variables**) to train a linear regression model that outputs the **survival** of the passenger (**dependent variable**).

## Requirements

Your code will need to:

- Read in the dataset and extract all columns except **Survived** as the input (**X**).
- Set **Survived** as the target variable (**y**) that we aim to predict.
- Split the dataset into **appropriate training and testing sets** 
- Create and **fit a linear regression model** to the training data.
- Use the trained model to **predict passenger's survival** on the test set and save it to a file.
- Use the `tests.py` file to create a testing class which is able to compute various different metrics of your prediction
- Combine your results in `main.py` to import `linear-regression.py` and `tests.py` to maintain a clean, modular workflow

The end goal is to produce predictions in the shape of an **t×1 dimensional vector** (or tensor), where each element corresponds to the survival for each of the **t** Titanic passengers you have chosen as your test set. Ensure that your code is well-documented and modular, so others can easily read, maintain, and build upon your work.

## Best Practices and Expectations

- Check the dataset for **missing or anomalous values**, and handle these issues appropriately (e.g., **imputation, removal, or other data-cleaning steps**).
- Clearly **separate data-preprocessing steps** from model training and prediction steps.
- Provide **clear function definitions and docstrings**. This will help your colleagues understand the logic and flow of data through the code.
- Include basic **performance metrics** such as:
  - **Mean Squared Error (MSE)**
  - **Mean Absolute Error (MAE)**  
  These will help evaluate how well your model performs.

If you have any questions or run into any issues, please reach out for clarification or assistance.
