import matplotlib.pyplot as plt

from load_data import structured_dataset

all_delta_1_1 = structured_dataset['data'][0]['Delta_TP9']
all_delta_1_2 = structured_dataset['data'][1]['Delta_TP9']
all_delta_1_3 = structured_dataset['data'][2]['Delta_TP9']
all_delta_1_4 = structured_dataset['data'][3]['Delta_TP9']
all_delta_1_5 = structured_dataset['data'][4]['Delta_TP9']
all_delta_1_6 = structured_dataset['data'][5]['Delta_TP9']
all_delta_1_7 = structured_dataset['data'][6]['Delta_TP9']
all_delta_1_8 = structured_dataset['data'][7]['Delta_TP9']
all_delta_1_9 = structured_dataset['data'][8]['Delta_TP9']
all_delta_1_10 = structured_dataset['data'][9]['Delta_TP9']
all_delta_1_11 = structured_dataset['data'][10]['Delta_TP9']

# print("Lengh of all delta for 1st person for 1st movie = ", len(all_delta_1_1))
# print("Lengh of all delta for 1st person for 2st movie = ", len(all_delta_1_2))
# print("Lengh of all delta for 1st person for 3st movie = ", len(all_delta_1_3))
# print("Lengh of all delta for 1st person for 4st movie = ", len(all_delta_1_4))
# print("Lengh of all delta for 1st person for 5st movie = ", len(all_delta_1_5))

plt.plot(all_delta_1_1, label='1st - baseline')
plt.plot(all_delta_1_2, label='2nd')
plt.plot(all_delta_1_3, label='3rd')
plt.plot(all_delta_1_4, label='4th')
plt.plot(all_delta_1_5, label='5th')
plt.plot(all_delta_1_6, label='6th')
plt.plot(all_delta_1_7, label='7th')
plt.plot(all_delta_1_8, label='8th')
plt.plot(all_delta_1_9, label='9th')
plt.plot(all_delta_1_10, label='10th')


plt.grid()
plt.xlabel('sample [number]')
plt.ylabel('brainwaves [Bels]')
plt.title('Delta_TP9 participant 22 during videos')
plt.legend()
plt.show()

print('end')
