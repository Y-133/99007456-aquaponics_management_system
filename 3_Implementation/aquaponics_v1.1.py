# AQUAPONIC MANAGEMENT SYSTEM

import  datetime
import random
now = datetime.datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

class Plant_Management:
    
    def __init__(self):
        print("PLANT_MANAGEMENT SYSTEM")
        self.old_nitrite_tester_value = 0
        self.old_nitrite_tester_qnt = 0
        self.nitrite_tester_qnt = 0

        self.old_ammonia_tester_value = 0
        self.old_ammonia_tester_qnt = 0
        self.ammonia_tester_qnt = 0
        
        total_nitrite_tester_qnt = 0
        total_ammonia_tester_qnt = 0

        self.old_fish_food_value = 0
        self.old_fish_food_qnt = 0
        self.fish_food_qnt = 0
        
        #old_valueflag = False
        #1

    #def input_material_stock_consumption(self):
     #   print("print the staus of the stocks\n")  #excel store
    
    def input_material_stock_new(self):
        
        #purchase 
        self.one_pHreader_price =input("Enter the pH reader_price\n")    #1000
        
        self.old_nitrite_tester_qnt = self.nitrite_tester_qnt
        self.old_nitrite_tester_value += (self.one_nitrite_tester_price * self.nitrite_tester_qnt)   

        self.one_nitrite_tester_price = input("Enter nitrite_tester_price\n")   #1 * 1200#per month
        self.nitrite_tester_qnt = input("Enter nitrite_tester_qantity purchased\n")   #1 * 1200#per month

        #old_valueflag =True

        total_nitrite_tester_price = (self.one_nitrite_tester_price * self.nitrite_tester_qnt) + self.old_nitrite_tester_value 
        total_nitrite_tester_qnt = self.old_nitrite_tester_qnt + self.nitrite_tester_qnt
#2----------------------------------------------------------------------------------------------------------------

        self.old_ammonia_tester_qnt = self.ammonia_tester_qnt
        self.old_ammonia_tester_value += (self.one_ammonia_tester_price * self.ammonia_tester_qnt)   

        self.one_ammonia_tester_price = input("Enter nitrite_tester_price\n")   #1 * 1200#per month
        self.ammonia_tester_qnt = input("Enter nitrite_tester_qantity purchased\n")   #1 * 1200#per month

        total_ammonia_tester_price = (self.one_ammonia_tester_price * self.ammonia_tester_qnt) + self.old_nitrite_tester_value 
        total_ammonia_tester_qnt = self.old_ammonia_tester_qnt + self.ammonia_tester_qnt
       
#3-------------------------------------------------------------------------------------------------------------------------------------
        self.old_fish_food_qnt = self.fish_food_qnt
        self.old_fish_food_value += (self.one_fish_food_price * self.fish_food_qnt)   

        one_fish_food_price = input("Enter fish food price per kg:\n")
        fish_food_qnt = input("Enter fish food qantity purchased in kg\n")

        total_fish_food_price = (self.one_nitrite_tester_price * self.nitrite_tester_qnt) + self.old_nitrite_tester_value 
        total_fish_food_qnt = self.old_fish_food_qnt + self.fish_food_qnt
        
        #print(f"\nDATE:{}\n ")
#--------------------------------------------------------------------------------------------     
        self.miscellenious = input("Total of other expesnses\n")
        total_purchase_cost = self.total_nitrite_tester_qnt + self.total_ammonia_tester_qnt + self.fish_food_qnt + self.one_pHreader_price +  self.total_sapling_cost
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
    #def stock_status(self):

    def harvest_details(self):
        print("print the harvest status\n") #daily update, #excel store

        #input when to harvest the fish
        harvest_income = 0
        harvest_item = {}
        while True:
            self.item_name = input("Enter the item name(with breed):\n")
            self.weight = input("Enter the weight of item harvestd\n")
            self.market_price =input("enter the selling price of the item")
            self.total_market_price = self.weight *  self.market_price

            harvest_item[self.item_name] =[self.weight,  self.market_price, self.total_market_price]
            
            choice = input("Want to enter more itmes?\nEnter 1 To continue\nEnter 2 To exit")
            if( choice == 1):
                continue
            elif(choice == 2):
                break
            else:
                print("Invalid input\n")

        i =0
        harvest_keys = harvest_item.keys()
        for key in harvest_item:
            harvest_income += harvest_item [ harvest_keys[i] ][2]
            i+=1
        print("Harvest income:%.2f",harvest_income )
    #def auto_refill(self):
    #    print("auto reminder of the monthly must check ")  #remind to check/ disp the important parameters in a gist


class Crop_production(Plant_Management):  #plant tech maintenance
    
    def cooler_system(self, farm_temp_in):
        farm_temp = farm_temp_in
        idle_temp = 25
        if farm_temp in range(23, 25):
            print("The farm is in idle temperature\n")
        elif farm_temp > 27:
            print("Farm is getting hot")
            delay = farm_temp - idle_temp
            delay = delay/5

            while True:
                print("Farm temp:%.2f", farm_temp)
                ac = farm_temp - delay
                farm_temp = ac

                if (farm_temp in range(24.5 -26.5) ):
                    break

        elif  (farm_temp < 23) :
            while True:
                print("Farm temp:%.2f", farm_temp)
                ac = farm_temp + delay
                farm_temp = ac

                if (farm_temp in range(24.5 -26.5) ):
                    break

    def emergency_exit(self, override):
        #this program to exit the program
        print("exit\n")
        if(farm_temp > 57): #fire alarm on: 57 celcius
            print("WARNING: FIRE DETECTED\nFire alarm on")
            fire_alarm_status = True
            sprinklers_status = True
        if(farm_temp <37):
            print("The farm is in normal temp\n")
            fire_alarm_status = False
            sprinklers_status = False
        
        #Mannual override
        fire_alarm_mannual = override
        if( fire_alarm_mannual == 1):
            fire_alarm_status = False
            sprinklers_status = False

        else:
            fire_alarm_status = True
            sprinklers_status = True

    def sapling_grow_essentials(self):  #water quality monitored at the tanks where the plants are grown
        
        print("print he plant status\n")  #sensor o/p, water chemical levels, excel store
        nitrite_levels = input("Enter the nitrite levels(ppm)\t") 
        pH_levels = input("Enter the pH levels") 
        ammonia_levels = input("Enter the nitrate levels(ppm)\t") 

        if(nitrite_levels >1 ): #in ppm
            print("nitrite level is %f\nWarning: Danger for fish\n", nitrite_levels)

        elif(nitrite_levels >2 ):
            print("nitrite levels are at dangerous high\n", nitrite_levels)
            alarm_status = True
            for i in range(10):
                i +=1
            alarm_status = False

        else:
            print("Nitrites are at safer levels\n")

        if(ammonia_levels >0.25 ): #in ppm
            print("ammonia level is %f\nWarning: Danger for fish\n", ammonia_levels)
        elif(ammonia_levels >2 ):
            print("nitrite levels are at dangerous high\n", nitrite_levels)
          
            alarm_status = True
            for i in range(10):
                    i +=1
            alarm_status = False

        else:
            print("ammonia is at safer levels\n")

        if(pH_levels != 6 ): #in ppm
            print("pH level is %f\nWarning: Danger for fish\npH levels%f:", pH_levels)
            if(pH_levels < 6):
                print("WARNING: The water is ACIDIC\npH levels%f:", pH_levels)
            elif(pH_levels > 6):
                print("WARNING:The water is BASIC\npH level%f:", pH_levels )
            elif(pH_levels >7.5 or pH_levels <5.5)
                print("pF levels at dangerous levels: %.2f",pH_levels)
                
                alarm_status = True 
                for i in range(10):  #turning on the alarm for the 10 sec 
                    i +=1
                alarm_status = False
                
        else:
            print("pH levels are at safer levels %f\n", pH_levels)

        farm_temp = random.randit(23, 35) #temp in celcius
        cooler_system(farm_temp)   ##########Crop_production
                

    def input_crop_health(self):
        #health of the plants   export tp excel
        disease_name = input("Enter Identified disease if any?") 
        self.health = input("Enter the small description on the plant health ")
    
    def crop_report(self, disease_name):    
        print("Nitirite levels %f\nAmmonia levels:%f\npH levels:%f\n", nitrite_levels, ammonia_levels, pH_levels)
        print(f"{date_time}\n{disease_name}\n",self.health) 


class Finance(Plant_Management):   #def in (protected)
    def plant_expense():  #daily i/p, excel store
        print("print the expense of the company")
        salary = input("Enter the total salary expense")
        total_employee_benifits_cost = input("Enter the total employee benifits cost")
        emp_expense = salary + total_employee_benifits_cost   #-----> paid holiday, OT, tech_upgradation,

        self.tank_clean = input("Enter the cost to clean the tank") # to prevent the anaerobic reaction
        self.building_maintenance_cost =input("general maintenance cost")
        total_maintenance_cost = self.tank_clean + self.building_maintenance_cost

        transportation_cost = input("Enter the cost to transport the goods")
        expense = total_purchase_cost + total_maintenance_cost + emp_expense + transportation_cost

        print("Expense to the company:%f", expense)        

    def plant_sales():
        print("sales of company")
        _income = harvest_income 

    def plant_profit():
        print("profits") #calc the profit
        _profits = income - expense  
#-------------------------
    def plant_report(self):
        print()   
          
class initial_interface(Plant_Management, Crop_production, Finance):
    print("\t\tWELCOME TO THE AQUAPONICS SYSTEM MANAGEMENT\nEnter the login details")
    
    print("\nEnter your choice to enter the system")
    
    UI_choice = input("1. To enter new material stock\n2.Crop report\n3.Harvest details\n4.Plant health\n5.Harvest details\n6.To override the emergency alarm\n7.To exit the system ")

    def switch(UI_choice):
        match UI_choice:
            case 1:  #disp all variables, 
                input_material_stock_new()
            case 2:
                crop_report()
            case 3:
                harvest_details()
            case 4:
                input_crop_health()
            case 5:
                plant_report()
            case 6:
                emergency_exit() 
            case 7:
                quit() #sys.exit("Exiting the system\nThank you")

#object declaration
plant_management = Plant_Management()
#plant_management.material_stock_status() 
crop_production = Crop_production() 

def main():
    print("main function")
    initial_interface()
    login_creation =0

if __name__ == '__main__':
    main()


