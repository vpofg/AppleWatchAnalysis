import csv

def main():
    with open('data/aw_fb_data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            
            
if __name__ == '__main__':
    main()
    