import matplotlib.pyplot as plt

from load_data import structured_dataset

all_delta_1_1 = structured_dataset['data'][0]['Delta_TP9']
all_delta_1_2 = structured_dataset['data'][1]['Delta_TP9']
all_delta_1_3 = structured_dataset['data'][2]['Delta_TP9']
all_delta_1_4 = structured_dataset['data'][3]['Delta_TP9']
all_delta_1_5 = structured_dataset['data'][4]['Delta_TP9']
print("Lengh of all delta for 1st person for 1st movie = ", len(all_delta_1_1))
print("Lengh of all delta for 1st person for 2st movie = ", len(all_delta_1_2))
print("Lengh of all delta for 1st person for 3st movie = ", len(all_delta_1_3))
print("Lengh of all delta for 1st person for 4st movie = ", len(all_delta_1_4))
print("Lengh of all delta for 1st person for 5st movie = ", len(all_delta_1_5))

plt.plot(all_delta_1_1, label='1st')
plt.plot(all_delta_1_2, label='2st')
plt.plot(all_delta_1_3, label='3st')
plt.plot(all_delta_1_4, label='4st')
plt.plot(all_delta_1_5, label='5st')

plt.grid()
plt.xlabel('sample [number]')
plt.ylabel('brainwaves [Bels]')
plt.title('Delta_TP9 participant 22')
plt.legend()
plt.show()

print('end')
