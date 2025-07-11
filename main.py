import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import db_utils
import preprocessing
import model
import predict
import analysis

from src import db_utils, preprocessing, model, predict

VE_SO_TYPE = 'MEGA_6_45'  # hoặc 'POWER_6_55'
MAX_NUMBER = 45 if VE_SO_TYPE == 'MEGA_6_45' else 55
PREFIX = '645' if VE_SO_TYPE == 'MEGA_6_45' else '655'

# Load dữ liệu
# if VE_SO_TYPE == 'MEGA_6_45':
#     df = db_utils.load_vietlott_mega_645_data()
# else:
df = db_utils.load_vietlott_power_655_data()

# Xử lý
X, y = preprocessing.build_training_data(df, max_number=55)

# Mô hình
ml_model = model.build_model(input_dim=X.shape[1], output_dim=55)
ml_model.fit(X, y, epochs=1200, batch_size=16, validation_split=0.2)

# Dự đoán
suggested_numbers = predict.predict_next(ml_model, df)

# In kết quả
formatted = f'{655} K1'
for d in suggested_numbers:
    numbers = ' '.join(f"{n:02d}" for n in d)
    formatted += f' S {numbers}'
print(formatted)



# 4. Predict next
# freq_df = analysis.count_number_frequency(df)
# print(freq_df)
