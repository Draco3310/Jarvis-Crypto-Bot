import yfinance as yf

class DataAcquisition:
    """
    DataAcquisition class for acquiring historical price data from different sources.
    """

    def __init__(self):
        self.sources = {
            'yahoo_finance': self.get_data_yahoo_finance
        }

    def get_data(self, source, symbol, start_date, end_date, interval='1d'):
        """
        Acquire historical price data for the given cryptocurrency symbol and date range from the specified source.
        """
        if source not in self.sources:
            raise ValueError(f"Unsupported data source: {source}")
        
        return self.sources[source](symbol, start_date, end_date, interval)

    def get_data_yahoo_finance(self, symbol, start_date, end_date, interval='1d'):
        """
        Acquire historical price data for the given cryptocurrency symbol and date range from Yahoo Finance.
        """
        try:
            data = yf.download(f'{symbol}-USD', start=start_date, end=end_date, interval=interval)
            data.rename(columns={'Close': f'{symbol}_price'}, inplace=True)
            return data
        except Exception as e:
            print(f"Error downloading {symbol} from Yahoo Finance: {e}")
            return None

    # Add more data sources as needed.
