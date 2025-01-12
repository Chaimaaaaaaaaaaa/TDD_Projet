import csv

class FundingRaised:
    @staticmethod
    def _read_csv(file_path):
        with open(file_path, "rt") as csvfile:
            data = csv.reader(csvfile, delimiter=',', quotechar='"')
            next(data)  
            return [row for row in data]

    @staticmethod
    def _filter_data(data, filters):
        for key, value in filters.items():
            if key not in ['company_name', 'city', 'state', 'round']:
                continue
            index = {
                'company_name': 1,
                'city': 4,
                'state': 5,
                'round': 9
            }.get(key)
            data = [row for row in data if row[index] == value]
        return data

    @staticmethod
    def _map_row(row):
        return {
            'permalink': row[0],
            'company_name': row[1],
            'number_employees': row[2],
            'category': row[3],
            'city': row[4],
            'state': row[5],
            'funded_date': row[6],
            'raised_amount': row[7],
            'raised_currency': row[8],
            'round': row[9]
        }

    @staticmethod
    def where(options=None):
        options = options or {}
        csv_data = FundingRaised._read_csv("../startup_funding.csv")
        filtered_data = FundingRaised._filter_data(csv_data, options)
        return [FundingRaised._map_row(row) for row in filtered_data]

    @staticmethod
    def find_by(options):
        csv_data = FundingRaised._read_csv("../startup_funding.csv")
        filtered_data = FundingRaised._filter_data(csv_data, options)
        if filtered_data:
            return FundingRaised._map_row(filtered_data[0])
        raise RecordNotFound
