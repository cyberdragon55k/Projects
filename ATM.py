while True:
    balance=1000003
    
    print('     ATM     ')
    print('''
          1)    balance
          2)    withdraw
          3)    deposit
          4)    quit
          
          ''')
    try:
        option=int(input('enter option: '))
    except Exception as e:
        print('error:' ,e)
        print('enter 1,2,3 or 4 only')
        continue
    if option==1:
        print('balance $',balance)
    if option==2:
        print('balance $',balance)
        withdraw=float(input('enter withdraw amount $'))
        if withdraw>0:
            forewardbalance=(balance-withdraw)
            print('foreward balance $',forewardbalance)
        elif withdraw>balance:
            print('no funs in account')
        else:
            print('none withdraw made')
    if option==3:
            print('balance $',balance)
            deposit=float(input('enter deposit amount $'))
            if deposit>0:
                forewardbalance=(balance+deposit)
                print('forwardbalance $ ',forewardbalance)
            else:
                print('none deposit made')
    if option==4:
                exit()