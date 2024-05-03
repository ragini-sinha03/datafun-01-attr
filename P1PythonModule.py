'''This module provides a reusable byline for author's services.'''



# import dependencies
import statistics

def main():
    # define variables
    company_name = "ABC Corporation"
    company_description = "Online Clothing store"
    company_established_year = 2010
    company_location = "Washington state"
    accounts = ['Jeans', 'Sweaters', 'Shirts', 'Joggers', 'Pants', 'Blazers']
    account_profit = [2500, 3500, 2900, 1400, 3200, 2000]
    company_sourced_outside_US = False
    yearly_income = sum(account_profit)
    yearly_expenses = 10000
    yearly_profit = yearly_income - yearly_expenses

    smallest = min(account_profit)
    largest = max(account_profit)
    mean = statistics.mean(account_profit)
    mode = statistics.mode(account_profit)
    median = statistics.median(account_profit)
    standard_deviation = statistics.stdev(account_profit)

    # Multiline string using f-string
    byline = f"""
    Name: {company_name}
    Description: {company_description}
    Launching Year: {company_established_year}
    State: {company_location}
    Smallest: {round(float(smallest), 2)}
    Largest: {round(float(largest), 2)}
    Mean: {round(mean, 2)}
    Mode: {round(mode, 2)}
    Median: {round(median, 2)}
    Standard Deviation: {round(standard_deviation, 2)}
    """

    print(byline)

if __name__ == '__main__':
    main()

    
