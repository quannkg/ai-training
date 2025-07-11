import numpy as np

def predict_next(model, df, max_number=55, top_k=3):
    # Lấy dữ liệu mới nhất làm input
    last_input = df["one_hot"].iloc[-1]
    input_arr = np.array([last_input])

    # Dự đoán xác suất từng số
    prob = model.predict(input_arr)[0]

    # Lấy top_k bộ số từ xác suất cao
    results = []
    for _ in range(top_k):
        indices = np.argsort(prob)[-6:]  # lấy 6 số cao nhất
        chosen = sorted([i + 1 for i in indices])
        results.append(chosen)
        prob[indices] = 0  # để vòng sau lấy bộ khác

    return results
