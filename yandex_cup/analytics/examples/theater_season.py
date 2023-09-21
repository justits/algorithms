import pandas as pd

FILE_PATH = 'data/ticket_logs.csv'

if __name__ == "__main__":
    tickets = pd.read_csv(FILE_PATH, names=['performance', 'phone'])
    tickets['phone'] = tickets.apply(lambda x: "".join(filter(str.isalnum, x.phone)), axis=1)
    tickets.drop_duplicates(inplace=True)

    print(tickets.performance.value_counts())