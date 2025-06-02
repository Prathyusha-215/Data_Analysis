import math

def calculate_stats(data):
    if not data:
        return "No data provided."
    
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    std_deviation = math.sqrt(variance)

    return {
        "Mean": mean,
        "Variance": variance,
        "Standard Deviation": std_deviation
    }

# Example usage:
data_input = input("Enter numbers separated by commas: ")
data = list(map(float, data_input.split(',')))

result = calculate_stats(data)

for k, v in result.items():
    print(f"{k}: {v:.4f}")