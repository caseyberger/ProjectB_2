# group8-SDS-271
# Monte Carlo Pi Estimation

This Python script contains a class, `MonteCarloPi`, that uses a Monte Carlo simulation to estimate the value of Pi. The theory behind this method is based on the ratio of the areas of a circle and a square.

## Class Attributes

- `radius`: The radius of the square in which the darts are being thrown
- `length`: The size of the square, calculated as twice the radius
- `num_it`: The number of iterations of dart throws
- `num_darts`: The number of dart throws in each iteration, randomly selected from the range (100, 10000)

## Methods

- `throw_dart()`: Simulates a single dart throw and returns True if it lands inside the circle and False otherwise
- `many_throws()`: Simulates a number of dart throws and stores the results in a pandas DataFrame
- `summarize_results(df)`: Summarizes the results of a series of dart throws
- `calc_pi(hit_results_df)`: Estimates the value of Pi based on the ratio of dart throws that landed inside the circle to the total number of throws

## Usage

1. Import the `MonteCarloPi` class from the script.
2. Create an instance of the class, specifying the radius of the square and the number of iterations.
3. Call the `many_throws()` method to simulate a number of dart throws.
4. Call the `summarize_results()` method to summarize the results of the dart throws.
5. Call the `calc_pi()` method to estimate the value of Pi based on the results of the dart throws.
