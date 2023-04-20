def calc (a, action, b):
    result = 0
    if action == '/':
        result += a/b;
    else:
        raise ValueError ("Допускается только действие + ; = ; или * .")
    return result;



n = int(input("Введите число 1: "))

action = input("Введите действие: ")

m = int(input("Введите число 2: "))

print (f"{n}{action}{m}=", calc (n, action, m))
