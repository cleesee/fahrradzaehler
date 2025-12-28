import os
import requests
import gzip
import shutil

# create the directories
def ensure_data_dir(folder_name: str) -> None:
    os.makedirs(folder_name, exist_ok=True)

# download a file from a url
def download_file(url: str, target_path: str, timeout: int = 30) -> None:
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()
    with open(target_path, "wb") as f:
        f.write(response.content)

# download the files
def download_bike_counter_data(
    folder_name: str,
    start_year: int = 2013,
    end_year: int = 2025,
) -> None:
    base_url = "https://mobidata-bw.de/fahrradzaehldaten/v2/fahrradzaehler_stundenwerten_"
    file_extension = ".csv.gz"

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            filename = f"{year}{month:02d}{file_extension}"
            url = base_url + filename
            file_path = os.path.join(folder_name, filename)

            try:
                download_file(url, file_path)
            except Exception as e:
                print(f"Failed: {url} ({e})")

# unpack the files
def unpack_gz_files(folder_name: str, remove_gz: bool = False) -> None:
    for filename in os.listdir(folder_name):
        if not filename.endswith(".csv.gz"):
            continue

        gz_path = os.path.join(folder_name, filename)
        csv_path = os.path.join(folder_name, filename[:-3])

        try:
            with gzip.open(gz_path, "rb") as f_in:
                with open(csv_path, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)

            if remove_gz:
                os.remove(gz_path)

        except Exception as e:
            print(f"Failed to unpack {gz_path}: {e}")
