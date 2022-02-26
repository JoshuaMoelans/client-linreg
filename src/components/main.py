import random
import matplotlib.pyplot as plt
import csv


class LinearRegression:
    eA: int  # error value on a [-eA,eA]
    eB: int  # error range on b [-eB,eB]
    a: int  # a in y=ax+b
    b: int  # b in y=ax+b
    minX: int  # domain lower boundary
    maxX: int  # domain upper boundary

    def __init__(self, errorA=100, errorB=50, minX=20, maxX=120):
        """
        Initialize the Linear Regression Model
        :param errorA: error on a in y = ax+b
        :param errorB: error on b in y = ax+b
        :param minX: minimum x value
        :param maxX: maximum x value
        """
        self.eA = errorA
        self.eB = errorB
        self.minX = minX
        self.maxX = maxX
        self.generate_linear()

    def generate_linear(self, minA=2300, maxA=4600, stepA=100, minB=1000, maxB=3000, stepB=100):
        """
        Function generating coefficients a and b for a linear function y = a*x + b
        :param minA: minimum value for a
        :param maxA: maximum value for a
        :param stepA: step size for a
        :param minB: minimum value for b
        :param maxB: maximum value for b
        :param stepB: step size for b
        :return: void - sets class attribute coefficients a and b values
        """
        # default values for a and b range chosen from data about price per m² for apartments in Belgium
        self.a = random.randrange(minA, maxA, stepA)
        self.b = random.randrange(minB, maxB, stepB)

    def generate_values(self, count):
        """
        Generates specified amount of linear values with random errors, in range between minimum and maximum x values
        :param count: the amount of values to return
        :return: a list of tuples [x,y] where y = (a+eA)*x+(b+eB) where eA and eB are errors on values for a and b.
        """
        valueList = list()
        for i in range(count):
            x = random.randrange(self.minX, self.maxX, 5)
            eA, eB = 0, 0
            if self.eA:
                eA = random.randrange(-self.eA, self.eA, int(self.eA / 10))  # generate error on a
            if self.eB:
                eB = random.randrange(-self.eB, self.eB, int(self.eB / 10))  # generate error on b
            y = (self.a + eA) * x + (self.b + eB)
            valueList.append([x, y])
        return valueList

    def generate_csv(self, count=100):
        """ //todo: replace function with actual Flask calls between back- and frontend
        Generates a csv file
        :param count: amount of points to generate
        :return: void
        """
        v = self.generate_values(count)
        with open('../../public/dataset/points.csv', 'w', newline='') as csvfile:
            fieldnames = ['price', 'area']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for point in v:
                writer.writerow({'price': point[1], 'area': point[0]})
        return

    def generate_example_graph(self, count=10):
        """
        Generates a plot of a random linear function, based on which some tuples with small disturbances are created
        and shown
        :return: void
        """
        self.generate_linear()
        values = self.generate_values(count)
        plt.scatter(*zip(*values))
        x = [self.minX - 5, self.maxX + 5]  # get 2 x values for linear regression line
        y = [(self.a * v + self.b) for v in x]  # generate paired y values
        plt.plot(x, y)
        plt.show()

    def evaluation_run(self):
        """
        Prototype function to test our mission block
        :return: void
        """
        oldPoints: list = list()
        oldValues: list = list()
        while True:
            newPoints = oldPoints + self.generate_values(10)  # add 10 new generated values on top of old points
            oldPoints = newPoints  # set old points for next while-iteration
            plt.scatter(*zip(*newPoints))  # scatter plot of new point set
            if oldValues:
                x = [self.minX - 5, self.maxX + 5]  # get x values for linear regression line
                y = [(oldValues[0] * v + oldValues[1]) for v in x]  # generate paired y values
                plt.plot(x, y, "b--")  # plot line as blue and dotted
            plt.show()  # show scatter and old a,b value line
            # todo: change a,b to front-end input via flask calls
            a, b = self.get_input()  # call input function;
            oldValues = [a, b]
            x = [self.minX - 5, self.maxX + 5]  # get x values for linear regression line
            y = [(a * v + b) for v in x]  # generate paired 'guessed' y values for input a and b
            y2 = [(self.a * v + self.b) for v in x]  # generate actual linear line from model
            plt.scatter(*zip(*newPoints))  # scatter plot of new points
            plt.plot(x, y, "b--")  # plot guessed LR model line as blue dotted
            plt.plot(x, y2, "r-")  # plot actual linear line from model as red full
            plt.show()
            score = self.evaluate_score_interval(newPoints, a, b, intervalTweak=0.5)  # evaluate score
            print(self.a, self.b, "\n", a, b)  # temporary printing for testing a,b values
            if (a == self.a) and (b == self.b):
                print(f"a and b are entirely correct! You scored {score * 100}%")
                break
            elif score >= 0.90:
                print(f"you have a high accuracy linear regression of {score * 100}%!")
                break
            else:
                i = input(f"a and b are incorrect! You scored {score * 100}% Press enter to continue,"
                          f" or type 'stop' to end.")
                if i == "stop":
                    break

    def evaluate_score_interval(self, points, input_a, input_b, intervalTweak=0.5):
        """
        Evaluates score based on whether points fall within error interval of new line
        :param intervalTweak: tweakable value for strictness of interval. <1 → strict | >1 → less strict
        :param points: list of points to base score on
        :param input_a: input a given by user
        :param input_b: input b given by user
        :return: score value
        """
        if intervalTweak == 0:  # temporary pre-condition, todo: write better later on!
            intervalTweak = 0.1
        if not points:  # to avoid division by 0
            return 0
        ctr = 0
        for p in points:
            x, y = p
            interval = (self.eA * x + self.eB) * intervalTweak
            actualY = self.a * x + self.b
            guessY = input_a * x + input_b
            if actualY - interval <= guessY <= actualY + interval:
                ctr += 1
        return ctr / len(points)

    def evaluate_score_k(self, points, input_a, input_b):
        """
        Evaluates score based on k^2 values for each point
        :param points: list of points to base score on
        :param input_a: input a given by user
        :param input_b: input b given by user
        :return: score value
        """
        actual = 0
        user = 0
        maxError = len(points) * (self.eA * self.maxX + self.eB)
        for p in points:
            x, y = p
            actual += abs(y - (self.a * x + self.b))
            user += abs(y - (input_a * x + input_b))
        return abs(actual - user) / maxError

    def get_input(self):
        """ #todo: replace by front-end slider values and/or matplotlib sliders for prototype
        Temporary function to get values for a and b
        :return: a and b values
        """
        a: int = int(input("Enter value for a: "))
        b: int = int(input("Enter value for b: "))
        return a, b


if __name__ == '__main__':
    lg = LinearRegression(errorA=1000, errorB=10000)
    lg.generate_csv(100)
