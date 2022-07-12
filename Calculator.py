class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for x in args:
            result = result * x
        return result

    @staticmethod
    def divide(*args):
        total = args[0]
        for i in args[1:]:
            total /= i
        return total

    @staticmethod
    def subtract(*args):
        total = args[0]
        for i in args[1:]:
            total -= i
        return total


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
