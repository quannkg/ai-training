import numpy as np

def to_one_hot(numbers, max_number):
    one_hot = [0] * max_number
    for n in numbers:
        n = int(n)
        if n < 1 or n > max_number:
            raise ValueError(f"Số {n} vượt ngoài 1–{max_number}")
        one_hot[n - 1] = 1
    return one_hot

def build_training_data(df, max_number=55):
    df["numbers"] = df["day_so_trung_thuong"].apply(
        lambda s: [int(x.strip()) for x in s.split(",")]
    )
    df["one_hot"] = df["numbers"].apply(lambda x: to_one_hot(x, max_number))

    X = df["one_hot"].values[:-1].tolist()
    y = df["one_hot"].values[1:].tolist()
    return np.array(X), np.array(y)

