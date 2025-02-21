import math

def main():
    print("这是一个软件老化可信度量模型。")

    # Input data as provided
    input_data = [
        "5",
        "MEM 15",
        "STO 4",
        "LOG 7",
        "NUM 2",
        "ARU 2",
        "0.0506 0.1845 0.0238 0.0238 0.0774 0.0774 0.0774 0.0238 0.0238 0.0506 0.0238 0.0238 0.0238 0.1042 0.1845",
        "0.25 0.25 0.25 0.25",
        "0.234 0.1064 0.1064 0.234 0.1064 0.1064 0.1064",
        "0.2 0.8",
        "0.1 0.9",
        "2",
        "0 10",
        "4 7 1 4 1 1 4 1 1 1 4 1 4 1 4",
        "4 1 4 4",
        "1 1 4 1 1 1 7",
        "4 1",
        "1 4",
        "4 7 7 4 9 4 7 7 7 4 7 7 7 9 7",
        "7 9 7 7",
        "7 7 4 10 7 10 9",
        "7 4",
        "7 7"
    ]

    index = 0
    n = int(input_data[index])
    index += 1
    categories = {}
    for _ in range(n):
        parts = input_data[index].split()
        name = parts[0]
        weight = float(parts[1])
        categories[name] = weight
        index += 1

    # Read measurements for each category
    measurements = []
    measurement_values = list(map(float, input_data[index].split()))
    index += 1
    total_measurements = sum(int(categories[name]) for name in categories)
    if len(measurement_values) != total_measurements:
        print("Error: Number of measurements does not match the total expected.")
        return
    ptr = 0
    for name in categories:
        num = int(categories[name])
        measurements.append(measurement_values[ptr:ptr+num])
        ptr += num

    # Read time values
    time_values = []
    time_count = int(input_data[index])
    index += 1
    for _ in range(time_count):
        t = int(input_data[index])
        time_values.append(t)
        index += 1

    # Read configuration parameters
    configurations = []
    for _ in range(time_count):
        config = list(map(int, input_data[index].split()))
        configurations.append(config)
        index += 1

    # Calculate weights p
    p = [0.0] * n
    temp = 0.0
    for i in range(n):
        p[i] = 0.0
        for j in range(n):
            if categories[list(categories.keys())[j]] == 0:
                continue  # Avoid division by zero
            p[i] += categories[list(categories.keys())[i]] / categories[list(categories.keys())[j]]
        p[i] -= 1
        temp += p[i]

    for i in range(n):
        if temp == 0:
            p[i] = 0.0
        else:
            p[i] /= temp

    print("各类别的权重为：", end='')
    for i in range(n):
        print(f"{p[i]:.3f} ", end='')
    print()

    # Placeholder for further calculations (H, U, T)
    # ...

    # Example output (replace with actual calculations)
    print(" 时间             软件可信度")
    for t in time_values:
        print(f"t={t:3d}               1.000")

if __name__ == "__main__":
    main()