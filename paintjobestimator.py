#This program estimates the number of gallons of
#paint and the labor cost involved based on
#a set labor price and user supplied square footage and cost
#of paint per gallon
import math

def main():
    another_estimate = 'y' #loop control variable
    
    SQ_FT_PER_GALLON = 350 #amount of area a gallon of paint covers
    LABOR_HRS_PER_GALLON = 6 #hours it takes to use a gallon of paint   
    SQ_FT_PER_HOUR = SQ_FT_PER_GALLON / LABOR_HRS_PER_GALLON
    LABOR_COST_PER_HR = 62.25     

    #Allows user to perform more than one estimate
    while another_estimate == 'y' or another_estimate == 'Y':
        
        #Get square footage from the user
        while True:
            try:                
                square_feet = int(input('Enter the square footage: '))
                if square_feet <= 0:
                    print("Negative times are not allowed.")
                    continue
            except ValueError:
                print('The value you entered is invalid. ' +
                      'Only numerical values are valid.')
            else:
                break
        print()

        #Get the price of a gallon of paint from the user
        while True:
            try:
                paint_price = float(input('Enter gallon price of paint: '))
                if paint_price <= 0:
                    print("Negative times are not allowed.")
                    continue

            except ValueError:
                print('The value you entered is invalid. ' +
                      'Only numerical values are valid.')
            else:
                break
        
        print()   
            
        #call total_gallons_paint function and assign it to
        #total_gallons variable
        total_gallons = get_total_gallons_paint(square_feet, SQ_FT_PER_GALLON)        

        #Call total_hrs_labor function and assign it to total_hrs variable
        total_hrs= get_total_hrs_labor(square_feet, SQ_FT_PER_HOUR)

        #Call total_cost_paint function and assign it to total_paint variable
        total_paint = get_total_cost_paint(paint_price, total_gallons)
        
        #Call total_cost_labor function and assign it to total_labor variable
        total_labor = get_total_cost_labor(
             square_feet, SQ_FT_PER_HOUR, LABOR_COST_PER_HR)
        
        job_price = total_paint + total_labor
        

        #output
        print('The amount of paint required to paint', square_feet,
              'square feet is', total_gallons, 'gallon(s)')
        print()
        print('The amount of labor it would take to paint', square_feet,
              'square feet is', format(total_hrs, ',.1f'), 'hours')
        print()
        print('The total cost of paint is $', format(total_paint, ',.2f'),
            sep='')
        print()
        print('The total cost of labor is $', format(total_labor, ',.2f'),
            sep='')
        print()
        print('the total cost to paint ', square_feet, ' square feet is $',
              format(job_price, ',.2f'), sep='')        
        print()
        
        another_estimate = input(
            'Would you like to do another estimate? (y/n): ')

#Calculate total gallons of paint needed
def get_total_gallons_paint(square_feet, sq_ft_per_gallon):
    return int(math.ceil(square_feet / sq_ft_per_gallon))

#Calculate total hours of labor required 
def get_total_hrs_labor(square_feet, Sq_ft_per_hr):
    return square_feet / Sq_ft_per_hr

#Calculate total cost of paint for the job
def get_total_cost_paint(price, gallons):
    return price * gallons

#Calculate total cost of labor for the job
def get_total_cost_labor(square_feet, sq_ft_per_hr, labor_cost_per_hr):
        return (square_feet / sq_ft_per_hr) * labor_cost_per_hr
#Call main function
main()

        
    
