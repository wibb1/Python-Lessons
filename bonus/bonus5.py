waiting_list = ['jen', 'ben', 'john']
waiting_list.sort()
for i, item in enumerate(waiting_list):
    row = f"{i}.{item.capitalize()}"
    print(row)