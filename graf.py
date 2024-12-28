import matplotlib.pyplot as plt

class Graph:
    def __init__(self,month,values):
        self.month = month
        self.values = values

    def show(self):
        plt.bar(self.month,self.values,label="Слова")
        plt.xlabel("Месяц года")
        plt.ylabel("Слова в месяц")
        plt.title("График")
        plt.legend()
        plt.show()


