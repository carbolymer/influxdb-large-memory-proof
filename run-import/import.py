

from influxdb import DataFrameClient
from pandas import read_hdf

client = DataFrameClient('influxdb', 8086, 'root', 'root', 'no_memory')

def main():
    client.create_database('no_memory')
    print('created db')

    prices = read_hdf('db.hdf', 'stocks')
    print('stocks imported from HDF5 file')

    # we need to reset index to be able to import the rows into influx
    prices = prices.reset_index()
    prices.columns.values[0] = 'symbol'
    prices = prices.set_index(['Date'])

    # divide prices by symbols
    prices_by_symbol = prices.groupby('symbol')
    for group in prices_by_symbol.groups:
        symbol_prices = prices_by_symbol.get_group(group)
        symbol_prices = symbol_prices[['Open', 'High', 'Low', 'Close', 'Volume']]
        client.write_points(symbol_prices, 'prices', tags={'symbol': group})
        print(group + ' saved')
    print('prices written')


if __name__ == '__main__':
    main()
