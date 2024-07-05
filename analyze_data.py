# analyze_data.py

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path, chunk_size=None):
    """Load CSV data into a Pandas DataFrame."""
    if chunk_size:
        return pd.read_csv(file_path, chunksize=chunk_size)
    else:
        return pd.read_csv(file_path)

def clean_data(df):
    """Clean and preprocess data."""
    df['Date'] = pd.to_datetime(df['Date'])  # Convert Date column to datetime
    df.set_index('Date', inplace=True)       # Set Date as index

def analyze_data(df):
    """Perform data analysis."""
    summary_stats = df.describe()
    print(summary_stats)

def visualize_data(df):
    """Visualize data using Matplotlib."""
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Close'], marker='o', linestyle='-', color='b')
    plt.title('Stock Closing Prices over Time')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    # Load data in chunks
    file_path = 'data/AAPL.csv'  
    chunk_size = 10000  
    chunks = load_data(file_path, chunk_size=chunk_size)
    
    # Process each chunk
    for chunk in chunks:
        # Clean data
        clean_data(chunk)
        
        # Analyze data
        analyze_data(chunk)
        
        # Visualize data
        visualize_data(chunk)

if __name__ == '__main__':
    main()

