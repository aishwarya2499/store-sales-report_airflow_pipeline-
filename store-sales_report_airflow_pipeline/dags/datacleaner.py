def data_cleaner():
    import pandas as pd
    import re

    df = pd.read_csv("/usr/local/airflow/store_files_airflow/raw_store_transactions.csv")

    def clean_store_location(st_loc):
        if isinstance(st_loc, str):
            return re.sub(r'[^\w\s]', '', st_loc).strip()
        return ''
    
    def clean_product_id(pd_id):
        if isinstance(pd_id, str):
            matches = re.findall(r'\d+', pd_id)
            if matches:
                return matches[0]
        return pd_id

    def remove_dollar(amount):
        if isinstance(amount, str):
            return float(amount.replace('$', ''))
        return amount

    df['STORE_LOCATION'] = df['STORE_LOCATION'].map(clean_store_location)
    df['PRODUCT_ID'] = df['PRODUCT_ID'].map( clean_product_id)

    for to_clean in ['MRP', 'CP', 'DISCOUNT', 'SP']:
        df[to_clean] = df[to_clean].map(remove_dollar)

    df.to_csv('/usr/local/airflow/store_files_airflow/clean_store_transactions.csv', index=False)