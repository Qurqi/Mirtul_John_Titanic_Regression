import tensorflow as tf
from sklearn.metrics import mean_squared_error, mean_absolute_error

class ModelEvaluation:
    def __init__(self, model, X_test, y_test):
        """
        Initializes model evaluation.

        :param model: Trained model
        :param X_test: Test features
        :param y_test: Test labels
        """
        self.model = model
        self.X_test = X_test
        self.y_test = y_test

    def predict(self):
        """
        Generates predictions using the trained model.
        """
        pass  # Implement model predictions
        predictions = self.model(self.X_test)
        print("Where my crystal ball?")
        print("...")
        print("...")
        print("...")
        print("...Ah!")
        print("Predicting...")
        return predictions
    
    def evaluate_mse(self):
        """
        Computes Mean Squared Error (MSE).
        """
        pass  # Implement MSE calculation
        mse = mean_squared_error(self.y_test, self.predict())
        print("Evaluating MSE...")
        print("You failed.")
        print("...")
        print("Kidding :)")
        print(f'Mean Squared Error: {mse}')
        return mse
    def evaluate_mae(self):
        """
        Computes Mean Absolute Error (MAE).
        """
        pass  # Implement MAE calculation
        mae = mean_absolute_error(self.y_test, self.predict())
        print("Calculate MAE? Absoultely!")
        print("Evaluating MAE...")
        print(f"Mean Absolute Error: {mae}")
        return mae
        