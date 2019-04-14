daily_sales_replaced = daily_sales.replace(';,;', ';')

#print(daily_sales_replaced)

daily_transactions = daily_sales_replaced.split(',')

#print(daily_transactions)

daily_transactions_split = []
for transactions in daily_transactions:
  daily_transactions_split.append(transactions.split(';'))
#print(daily_transactions_split)

transactions_clean = []

for items in daily_transactions_split:
  for item in items:
    transactions_clean.append(item.strip())
#print(transactions_clean)

customers = []
sales = []
thread_sold = []
i = 0
length = len(transactions_clean)

for i in range(0,length,4):
  customers.append(transactions_clean[i])
for i in range(1,length,4):
  sales.append(transactions_clean[i])
for i in range(2,length,4):
  thread_sold.append(transactions_clean[i])
#for sale in sales:
  #print(sale)
total_sales = 0

for sale in sales:
  sale = float(sale[1:])
  total_sales+=sale
#print(total_sales)
#print(thread_sold)

thread_sold_split = []
for thread in thread_sold:
  if "&" in thread:
    thread = thread.split("&")
    for colour in thread:
      thread_sold_split.append(colour)
  else:
    thread_sold_split.append(thread)
print(thread_sold_split)

def color_count(color):
	return len(list(filter(lambda x: x == color,  thread_sold_split)))

#print(color_count('white'))
colors = ['red','yellow','green','white','black','blue','purple']  

for color in colors:
  print("Thread shed sold {} threads of {} thread today.".format(color_count(color), color))
