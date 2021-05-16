'''
請寫一個程式,Input 是一個數字,Output 是從 1 到這個數字,扣除掉所有 3 的倍
數以及 5 的倍數,但是需要保留同時是 3 和 5 的倍數的總數字數。
(加分題) 請為你的程式寫 unit test。
'''

def divide_count(num):
    count = num - (num//3) - (num//5) + (num//15)
    return(count)

num = 20
print(divide_count(num))