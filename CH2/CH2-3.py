# 小数点绝对值的最大和最小
import sys
sys.float_info.max
print(sys.float_info.max)

sys.float_info.min
print(sys.float_info.min)

# 以下符号是检测小数点是十进制还是二进制，在语言中只有0和1是二进制，所以用来算不太够。
from decimal import Decimal
print(Decimal.from_float(0.5))
print(Decimal.from_float(0.3))

# 以下函数可以同时求算两数商和余数。/是除号，求的是商。%是求余数的符号。
print(divmod(120,55))
print(divmod(100,55))
print(divmod(450,55))

