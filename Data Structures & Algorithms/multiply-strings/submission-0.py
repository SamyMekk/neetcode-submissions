class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1==0 or num2==0:
            return "0"
        else:
            num1 = int(num1)
            num2= int(num2)
            prod_num = num1*num2
            return str(prod_num)