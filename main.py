import pandas as pd
from scipy.stats import shapiro, mannwhitneyu, ttest_ind, levene

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Read the data
df = pd.read_excel('Data/lokanta.xlsx')

# Create groups and calculate means
smoking = df[df['Sigara_icen'] == 'Evet']['Toplam_hesap']
non_smoking = df[df['Sigara_icen'] == 'Hayır']['Toplam_hesap']

mean_smoking = smoking.mean()
mean_non_smoking = non_smoking.mean()

# Check for the normality assumption
shapiro_smoking = shapiro(smoking)
shapiro_non_smoking = shapiro(non_smoking)

# Levene test for variance homogeneity
levene_test = levene(smoking, non_smoking)

# Perform t-test with equal variance assumption
ttest_equal_var = ttest_ind(smoking, non_smoking, equal_var=True)

# Mann-Whitney U test
mannwhitneyu_test = mannwhitneyu(smoking, non_smoking)

# Print the results
print("Mean Total Bill for Smoking Customers:", mean_smoking)
print("Mean Total Bill for Non-Smoking Customers:", mean_non_smoking)

print("Normality Test Result for Smoking Customers (Shapiro):", shapiro_smoking)
print("Normality Test Result for Non-Smoking Customers (Shapiro):", shapiro_non_smoking)

print("Levene Test Result for Variance Homogeneity:", levene_test)
print("Mann-Whitney U Test Result:", mannwhitneyu_test)

print("T-Test Result with Equal Variance Assumption:", ttest_equal_var)

print("Mann-Whitney U Test Result:", mannwhitneyu_test)


# Verileri oluşturun
data = {
    'Measure': ['Mean Total Bill', 'Mean Total Bill', 'Normality Test (Shapiro)', 'Normality Test (Shapiro)',
                'Variance Homogeneity (Levene)', 'Mann-Whitney U Test', 'T-Test (Equal Variance Assumption)'],
    'Category': ['Smoking Customers', 'Non-Smoking Customers', 'Smoking Customers', 'Non-Smoking Customers',
                 'Variance Homogeneity', 'Mann-Whitney U Test', 'T-Test'],
    'Result': [255.45, 246.01, 'p-value=0.6856', 'p-value=0.9313', 'p-value=0.9709', 'p-value=0.1018', 'p-value=0.1271']
}

# DataFrame oluşturun
result_df = pd.DataFrame(data)

# Sonuçları görüntüleyin
print(result_df)