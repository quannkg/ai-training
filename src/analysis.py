import pandas as pd
from collections import Counter

def count_number_frequency(df):
    all_numbers = []
    for row in df['day_so_trung_thuong']:
        nums = [int(n.strip()) for n in row.split(',')]
        all_numbers.extend(nums)

    freq = Counter(all_numbers)
    freq_df = pd.DataFrame({
        'number': range(1, 46),
        'frequency': [freq.get(i, 0) for i in range(1, 46)]
    }).sort_values(by='frequency', ascending=False)

    return freq_df
