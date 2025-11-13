import csv
class DataItem:
    def __init__(self, line):
        self.move_name = line[0]
        self.genre = line[1]
        self.release_date = line[2]
        self.director = line[3]
        self.budget = line[4]
        self.rating = line[5]
        self.duration_minutes = line[6]
        self.production_company = line[7]
        self.quote = line[8]

def load_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8', newline = '') as f:
        reader = csv.reader(f)
        for line in reader:
            data.append(line)
    return data

def hash(data):
    hash_table = {}
    for line in data:
        for item in line:
            ascii = []
            key = 0
            for char in item:
                ascii.append(ord(char))
            for num in ascii:
                key += num
                hash_table.update({key: item})
    return hash_table

def handle_collision():
    pass

def main():
    data = load_data('MOCK_DATA.csv')
    data.remove(data[0])
    hash_table = hash(data)
    print(hash_table)

if __name__ == "__main__":
    main()
