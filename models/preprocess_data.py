def load_and_clean_data():
    import os
    import pandas as pd

    data_dir = 'models'
    df_list = []

    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            filepath = os.path.join(data_dir, filename)
            print(f"📥 Loading: {filepath}")

            df = pd.read_csv(filepath)
            df.columns = df.columns.str.strip()

            if 'Label' not in df.columns:
                print(f"⚠️ Skipping {filename} — No 'Label' column")
                continue

            df['Label'] = df['Label'].apply(lambda x: 0 if str(x).strip().upper() == 'BENIGN' else 1)
            df_list.append(df)
    df.to_csv("models/original_dataset.csv", index=False)
    if not df_list:
        raise ValueError("❌ No valid CSV files with 'Label' column were found.")

    return pd.concat(df_list, ignore_index=True)
