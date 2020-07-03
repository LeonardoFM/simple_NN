import csv
import random

dataset=[]

with open('data.csv') as _file:
    data = csv.reader(_file,delimiter=',')
    for line in data:
        line = [float(elemento) for elemento in line]
        dataset.append(line)

    def treino_teste_split(dataset, percent):
        
        data_treino = random.sample(dataset, percent*len(dataset)//100)
        data_teste = [data for data in dataset if data not in data_treino]
        def montar(dataset):
            x, y = [], []
            for data in dataset:

                x.append(data[1:3])
                y.append(data[0])
            return x, y

        x_train, y_train = montar(data_treino)
        x_test, y_test = montar(data_teste)

        return x_train, y_train, x_test, y_test

    x_treino, y_treino, x_teste, y_teste = treino_teste_split(dataset, 80)

    def sign(u):
        return 1 if u>=0 else -1

    def adjust(w, x, d, y):
        learning_rate = 0.01
        return w + learning_rate * (d - y) * x

    def perceptron_fit(x, d):
        epoca=0
        w = [random.random() for i in range(3)]
        # print(w)
        while True:
            erro=False
            for i in range(len(x)):
                u = sum([w[0]*-1, w[1]*x[i][0], w[2]*x[i][1]])
                y=sign(u)
                if y!=d[i]:
                    w[0]=adjust(w[0],-1,d[i],y)
                    w[1]=adjust(w[1],x[i][0],d[i],y)
                    w[2]=adjust(w[2],x[i][1],d[i],y)
                    erro = True
            epoca+=1
            if erro is False or epoca==1000:
                break
        print(epoca)
        return w
    
    w_fit = perceptron_fit(x_treino, y_treino)    
    # print(w_fit)
    def perceptron_predict(x_test, w_adjusted):
        y_predict = []
        for i in range(len(x_test)):
            predict = sum([w_adjusted[0]*-1,w_adjusted[1]*x_test[i][0],w_adjusted[2]*x_test[i][1]])
            y_predict.append(sign(predict))
        return y_predict

    y_v = perceptron_predict(x_teste,w_fit)
    # print(y_v)

    def accur(y_test,y_v):
        total = 0
        for i in range(len(y_test)):
            if y_test[i] == y_v[i]:
                total+=1
        return total / len(y_v)
    accuracy = accur(y_teste, y_v)
    print(accuracy)
    