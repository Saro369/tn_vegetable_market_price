# Vegetable Price Data Extraction Project

This project scrapes vegetable price data for a specific district in India. It does so for a specified date range and exports the collected data to an Excel file. The project is set up to run in a Python environment.

## Setup

1. Clone the repository to your local machine.
2. Install Python 3.8 or higher.
3. Install the required Python libraries using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Install a compatible ChromeDriver version (corresponding to the installed Chrome browser version) and ensure that it is available on the system's PATH.

## Configuration

1. Copy the `.env.example` file and rename the copy to `.env`.

    ```bash
    cp .env.example .env
    ```

2. Edit the `.env` file and set the following variables:

    - `OUTPUT_PATH`: Path to the directory where the Excel files will be saved.
    - `DIST`: The district in India for which to scrape the vegetable price data.
    - `BASE_URL`: The base URL of the Vegetable Market Price website.
    - `START_DATE` and `END_DATE`: The date range for which to scrape the data, in the format `YYYY-MM-DD`.

## Running the Script

To start the data extraction process, run the `data_extraction.py` script:

```bash
python data_extraction.py
```

## Contributing

Contributions are welcome. Please open an issue to discuss your idea before implementing it.

## License

This project is licensed under the terms of the MIT license. See LICENSE for more details.