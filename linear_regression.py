import tensorflow as tf

class LinearRegressionModel(tf.keras.Model):
    def __init__(self, input_dim):
        """
        Initializes a simple linear regression model.

        :param input_dim: Number of input features
        """
        super(LinearRegressionModel, self).__init__()
        
        self.dense = tf.keras.layers.Dense(1, input_dim=input_dim)

    def call(self, inputs):
        """
        Forward pass for the model.

        :param inputs: Input tensor
        :return: Predicted values
        """
        return self.dense(inputs)  # Apply the dense layer to the inputs

    def train_model(self, X_train, y_train, epochs=100, lr=0.01):
        """
        Train the model using Mean Squared Error loss.

        :param X_train: Training features
        :param y_train: Training labels
        :param epochs: Number of training epochs
        :param lr: Learning rate
        """

        # Create an optimizer
        optimizer = tf.keras.optimizers.SGD(learning_rate=lr)

        # Define loss function
        loss_fn = tf.keras.losses.MeanSquaredError()

        # Compile the model
        self.compile(optimizer=optimizer, loss=loss_fn)

        # Train the model
        self.fit(X_train, y_train, epochs=epochs)
       

