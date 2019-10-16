def get_user_num():
   user_num = int(input('Enter a number: '))
   print('un: ',str(user_num))
   return user_num

def compute_avg(user_num1,user_num2):
   avg_result = (user_num1 + user_num2)/2
   return avg_result

user_num1 = 0
user_num2 = 0
avg_result = 0

print('#6 Challenge 6-1 Compute the average of two numbers')
user_num1 = get_user_num()
user_num2 = get_user_num()
avg_result = compute_avg(user_num1, user_num2)

print('Avg:', avg_result)
