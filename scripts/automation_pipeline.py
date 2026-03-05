import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import os

# file paths
RAW_DATA = 'data/DataCoSupplyChainDataset.csv'
CLEANED_DATA = 'data/cleaned_supply_chain.csv'
DATABASE = 'data/cleaned_supply_chain.db'
REPORT = 'data/summary_report.txt'

# function for cleaning the dataset
def clean_data(filepath):
    print("Loading data ...")
    df = pd.read_csv(filepath, encoding='latin-1')
    
    # drop these columns
    df = df.drop(columns=['Product Description', 'Order Zipcode', 'Customer Password'], errors='ignore')
    
    # handle missing values
    df['Customer Lname'] = df['Customer Lname'].fillna("Unknown")
    df['Customer Zipcode'] = df['Customer Zipcode'].fillna(0)
    
    # convert Order Date, Shipping Date to datetime format
    df['shipping date (DateOrders)'] = pd.to_datetime(df['shipping date (DateOrders)'], errors='coerce')
    df['order date (DateOrders)'] = pd.to_datetime(df['order date (DateOrders)'], errors='coerce')
    
    # save the cleaned dataset to a new csv file
    df.to_csv(CLEANED_DATA, index=False)
    print(f"Saved cleaned data to {CLEANED_DATA}!")
    return df

# function for loading the cleaned dataset into the database
def load_to_database(df):
    print("Connecting to database ...")
    engine = create_engine(f'sqlite:///{DATABASE}')
    print("Database connected successfully!")
    
    # load the cleaned dataset into a new table in the database
    df.to_sql('cleaned_supply_chain', con=engine, if_exists='replace', index=False)
    print("Data loaded into database successfully!")
    return engine

# analysis function
def run_analysis(engine):
    print("Running analysis ...")
    
    query1 = """
    SELECT "Shipping Mode", count(*) AS total_orders,
    sum("Late_delivery_risk") AS late_deliveries,
    round(sum("Late_delivery_risk") * 100.0 / count(*), 2) AS delivery_delay_rate
    FROM cleaned_supply_chain
    GROUP BY "Shipping Mode"
    ORDER BY delivery_delay_rate DESC
    """

    query2 = """
    SELECT "Market",
    round(sum("Sales"), 2) AS total_sales,
    round(sum("Order Profit Per Order"), 2) AS total_profit,
    count(*) AS total_orders
    FROM cleaned_supply_chain
    GROUP BY "Market"
    ORDER BY total_sales DESC
    """

    query3 = """
    SELECT "Category Name",
    round(sum("Order Profit Per Order"), 2) AS total_profit,
    count(*) AS total_orders
    FROM cleaned_supply_chain
    GROUP BY "Category Name"
    ORDER BY total_profit DESC
    LIMIT 5
    """

    query4 = """
    SELECT strftime('%Y-%m', "order date (DateOrders)") AS order_month,
    count(*) AS total_orders,
    round(sum("Sales"), 2) AS total_sales,
    round(sum("Order Profit Per Order"), 2) AS total_profit
    FROM cleaned_supply_chain
    GROUP BY order_month
    ORDER BY order_month ASC
    """
    
    results = {
        'delivery_delay_rate': pd.read_sql_query(query1, con=engine),
        'revenue_by_market': pd.read_sql_query(query2, con=engine),
        'top_5_profitable_categories': pd.read_sql_query(query3, con=engine),
        'monthly_order_trends': pd.read_sql_query(query4, con=engine)
    }
    print("Analysis completed successfully!")
    return results

# function to generate summary report
def generate_report(results):
    print("Generating summary report ...")
    # create a timestamp for the report
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # write the results to a text file
    with open(REPORT, 'w') as f:
        f.write(f"SUPPLY CHAIN SUMMARY REPORT\nGenerated on {timestamp}\n")
        f.write("="*50 + "\n\n")
        
        f.write("1. Delivery Delay Rate by Shipping Mode:\n")
        f.write(results['delivery_delay_rate'].to_string(index=False))
        f.write("\n\n" + "="*50 + "\n\n")
        
        f.write("2. Revenue by Market:\n")
        f.write(results['revenue_by_market'].to_string(index=False))
        f.write("\n\n" + "="*50 + "\n\n")
        
        f.write("3. Top 5 Most Profitable Categories:\n")
        f.write(results['top_5_profitable_categories'].to_string(index=False))
        f.write("\n\n" + "="*50 + "\n\n")
        
        f.write("4. Monthly Order Trends:\n")
        f.write(results['monthly_order_trends'].to_string(index=False))
    
    print(f"Summary report saved to {REPORT}!")
    
    # main function to run the entire pipeline
def main():
    print("\n" + "="*60)
    print("SUPPLY CHAIN ANALYSIS PIPELINE STARTING ...")
    print("="*60)
    
    # check if the file exists before running the pipeline
    if not os.path.exists(RAW_DATA):
        print(f"Error: Raw data file '{RAW_DATA}' not found. Please check the file path and try again.")
        return

    df = clean_data(RAW_DATA) # clean the dataset
    engine = load_to_database(df) # load the cleaned dataset into the database
    results = run_analysis(engine) # run the analysis queries
    generate_report(results) # generate the summary report
    
    print("\n" + "="*60)
    print("SUPPLY CHAIN ANALYSIS PIPELINE COMPLETED SUCCESSFULLY!")
    print("="*60)
    
main()