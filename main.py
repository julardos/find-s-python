import csv

attributes = [['sunny','rain'],
              ['normal','high'],
              ['slow','fast'],
            ]


num_attributes = len(attributes)

print("\n The Given Training Data Set \n")

a = []
with open('data/exercise.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for idx, row in enumerate(reader):
        if idx != 0:
            a.append(row)
            print(row)


print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes
print(hypothesis)

# Comparing with First Training Example 
for j in range(0,num_attributes):
        hypothesis[j] = a[0][j]

# Comparing with Remaining Training Examples of Given Data Set

print("\n Find S: Finding a Maximally Specific Hypothesis\n")

for i in range(0,len(a)):
    if a[i][num_attributes]=='yes':
            for j in range(0,num_attributes):
                if a[i][j]!=hypothesis[j]:
                    hypothesis[j]='?'
                else :
                    hypothesis[j]= a[i][j] 
    print(" For Training Example No :{0} the hypothesis is ".format(i),hypothesis)

print(hypothesis)