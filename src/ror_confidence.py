import math

# Values from our 2x2 table
a = 3035
b = 31249
c = 5238
d = 360992

# Calculate ROR
ror = (a * d) / (b * c)

# Calculate standard error of log(ROR)
standard_error = math.sqrt(
    (1 / a) + (1 / b) + (1 / c) + (1 / d)
)

# Calculate log(ROR)
log_ror = math.log(ror)

# Calculate 95% confidence interval
lower_log = log_ror - (1.96 * standard_error)
upper_log = log_ror + (1.96 * standard_error)

lower_limit = math.exp(lower_log)
upper_limit = math.exp(upper_log)

# Display results
print("Reporting Odds Ratio (ROR):", round(ror, 4))

print("95% Confidence Interval:")
print("Lower limit:", round(lower_limit, 4))
print("Upper limit:", round(upper_limit, 4))

print("\nConfidence interval calculation completed!")