import py200513.calculator_v2.calculator_functions_arithmetic as arith
import py200513.calculator_v2.calculator_functions_logical as logi



print('===  Program start  ===')
a = float(input('Input a numeric literal'))
b = float(input('Input a numeric literal'))


print(arith.add(a, b))
print(arith.sub(a, b))
print(arith.mul(a, b))
print(arith.div(a, b))
print(arith.pow(a, b))


print(logi.and_func(a, b))
print(logi.or_func(a, b))
print(logi.not_func(a))

print('Program terminated')
