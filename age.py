driving = input('請問你有開過車嗎：')
if driving != '有' and driving != '沒有':
	print('請輸入有或者沒有')
	raise ＳystemExit
age = input('請輸入你的年齡：')
age = int(age) # casting




if driving == '有':
    if age >= 18:
    	print('You pass the exam')
    else:
    	print("it's werid, how?" )
elif driving == '沒有':
    if age >= 18:
    	print('趕快去考試！！！')
    else:
    	print('加油！快可以考了')