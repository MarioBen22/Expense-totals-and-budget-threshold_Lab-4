# Mario Benavides
# Program Status - completed
# This program keeps a running total of the expenses for the month
# and displays the amount under or over budget.

# initialize the accumulator
total = 0.00

# Enter amount budgeted for the month
budgeted = float(input('Enter the amount budgeted for the month: $ '))


# enter each of the expenses for the month and keep a running total.
number = float(input('Enter an amount spent (0 to quit): $ '))
total += number


while number != 0:
    number = float(input('Enter an amount spent (0 to quit): $ '))
    total += number
    
print('Budgeted: $ ', format(budgeted, ',.2f'))
print('Spent: $ ', format(total, ',.2f'))


# display the amount that the user is over or under budget.
difference = budgeted - total
over = total - budgeted


if total > budgeted:
    print('You are $', format(over, ',.2f'), 'over budget. PLAN BETTER NEXT TIME!') 
           
elif budgeted > total:
    print('You are $', format(difference, ',.2f'), 'under budget. Good Job!')
            
else:
    print('You were right on budget. Great job!')
