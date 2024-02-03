
# Statistical Analysis of Restaurant Data

This Python script performs a statistical analysis on a dataset from a restaurant, comparing total bills and customer satisfaction between smoking and non-smoking customers.

## Dependencies
- pandas
- scipy.stats

## Features
- Reads data from an Excel file named `lokanta.xlsx` located in the `Data` directory.
- Calculates the mean total bill for smoking and non-smoking customers.
- Performs Shapiro-Wilk test to check the normality of the distribution of total bills for both groups.
- Conducts Levene's test to assess the homogeneity of variances between the two groups.
- Applies a t-test with the assumption of equal variances to compare the means of the two groups.
- Utilizes the Mann-Whitney U test as a non-parametric test to compare the two groups.
- Generates a summary DataFrame that presents the results of the statistical tests performed.

## Usage
1. Ensure the dataset `lokanta.xlsx` is placed in the `Data` directory.
2. Install the required Python packages.
3. Run the script to perform the analysis and view the results.

## Output
- The script outputs the mean total bills for smoking and non-smoking customers.
- Results from the Shapiro-Wilk test, Levene's test, Mann-Whitney U test, and t-test are printed to the console.
- A DataFrame summarizing the test results is also displayed.

## Note
- The script assumes that the dataset has a column named `Sigara_icen` to distinguish between smoking and non-smoking customers and a column named `Toplam_hesap` for the total bill amount.
