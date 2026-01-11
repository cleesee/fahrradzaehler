import os
import pandas as pd
from tqdm import tqdm

# load the data from files
def load_csv_folder_to_dataframe(
    folder_name: str,
    parse_dates: bool = True,
) -> pd.DataFrame:
    all_files = sorted(
        os.path.join(folder_name, f)
        for f in os.listdir(folder_name)
        if f.endswith(".csv")
    )

    if not all_files:
        raise ValueError(f"No CSV files found in {folder_name}")

    df_list = []

    for file in tqdm(all_files, desc="Loading CSV files", unit="file"):
        try:
            df = pd.read_csv(
                file,
                encoding="utf-8",
                low_memory=False,
                na_values=["na", "NA", "null"],
                parse_dates=["iso_timestamp"] if parse_dates else None,
            )
            df_list.append(df)

        except Exception:
            # tqdm stays clean; failures don’t spam output
            continue

    if not df_list:
        raise RuntimeError("No CSV files could be loaded successfully")

    df_loaded = pd.concat(df_list, ignore_index=True)

    if parse_dates:
        df_loaded["iso_timestamp"] = pd.to_datetime(
            df_loaded["iso_timestamp"], utc=True
        )

    print("Load summary")
    print(f"- Files loaded: {len(df_list)}")
    print(f"- Total rows: {len(df_loaded)}")
    print(
        f"- Date range: {df_loaded['iso_timestamp'].min()} "
        f"to {df_loaded['iso_timestamp'].max()}"
    )
    print(
        f"- Unique stations: {df_loaded['counter_site'].nunique()}"
    )

    return df_loaded
