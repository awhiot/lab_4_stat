import pandas as pd
import matplotlib.pyplot as plt


def make_hist(attribute: str):
    plt.hist(df[attribute])
    plt.xlabel(attribute)
    plt.ylabel('amount of people')
    plt.title('the number of sick and non-sick')
    plt.title(f'people and their {attribute}')
    plt.show()

    plt.hist(df[attribute])
    plt.xlabel(attribute)
    plt.ylabel('amount of people')
    plt.hist(df[df['chd'] == 1][attribute])
    plt.title(f'people and their {attribute}')
    plt.show()


df = pd.read_csv('cardio_train2.csv')

make_hist('sbp')
make_hist('ldl')
make_hist('alcohol')
make_hist('tobacco')
make_hist('obesity')
make_hist('age')

print('full dataset')
print(df.describe())
print('only people without issues')
print(df[df['chd'] == 0].describe())
print('only people with issues')
print(df[df['chd'] == 1].describe())
