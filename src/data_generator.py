"""
This is mainly a generator to generate predictable time series data in the required format.
"""

import numpy as np

class DataGenerator:

    def __init__(self):
        """
        Initializes the data generator and generates the data

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        # first thing is that we need to generate our X
        # all data here is normalized to be between 0 and 1
        initial_x_values = np.linspace(1, 10, 100) # generate 100 values between 1 and 10
        # let us generate some random noise to add to the data
        noise = np.random.normal(0, 0.02, 100) # generate 100 values of noise
        # let us generate an additional x value to add to the data
        additional_x = np.linspace(11, 20, 100) # generate 100 values between 11 and 20
        # now, let us make a source
        # source = x + noise + additional_x
        source = initial_x_values + noise + additional_x
        # from this, we can generate our y, as a sine wave
        # we need to convert these two induvidual arrays into a 2D array
        # we can do this by hstack
        self.X = np.hstack((initial_x_values.reshape(-1, 1), additional_x.reshape(-1, 1)))
        self.y = np.sin(source)

    def plot_data(self):
        """
        Plots the generated time series data

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        import matplotlib.pyplot as plt
        plt.plot(self.X)
        plt.plot(self.y)
        plt.show()


    def get_data(self):
        """
        Returns the generated time series data as a tuple

        Parameters
        ----------
        None

        Returns
        -------
        tuple
            A tuple of the generated time series data, separated into X and y
        """
        return self.X, self.y


if __name__ == "__main__":
    # test the data generator
    data_generator = DataGenerator()
    data_generator.plot_data()
    # X, y = data_generator.get_data()

    # print(X)
    # print(y)