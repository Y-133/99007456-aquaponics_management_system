# TEST PLAN:
 * Test plans are very helpful in checking the behaviour of the program, variables and function for different values
------------------------------------------------------------------------------------------------
## How to run the test? ##
* Load the file using the python IDE and run the code
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## FEATURES: ##
####
1. Stock management
2. Farm environment monitoring system
3. Finance management
4. Data record of the production in the farm
5. Emergency farm fire alarm system
----------------------------------------------------------------------------------------------------------------
## High level test plan

## TABLE_NO: HL_1 ##
| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual Out** |**Type Of Test** |    
| :---------: | :----------------------------------------------------------: | :---------: | :---------: | :------------: | :-------------: |
|  H_01       | Input the choices to select menus  | choice =1 | input_material_stock_new | total_purchase_cost | total_purchase_cost | Manual |
|  H_02       |  Input the choices to select menus  | choice =2 |  NA | NA | Output a report on the crop health | Manual |
|  H_03       | Input the choices to select menus   | choice =3 | Harvest details: Amount of fish or plant | Output the income generated| Output the income generated | Manual |
|  H_04       | Input the choices to select menus   | choice =4 | Input a report on the plant health | Display the report | Display the report | Manual |
|  H_05       | Input the choices to select menus   | choice =5 | Plant report: input the chemical levels in the water| Whether the water is safe or not | Whether the water is safe or not | Manual |
|  H_06       | Input the choices to select menus   | choice =6 | Manual on/off fire alarm | Fire alarm on | Manual |
|  H_07       | Input the choices to select menus   | choice = 7| quit | program got closed | Manual | 
 

------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Table no: Low level test plan

## TABLE_NO: LL_1 ##
| **High_leve_Test ID** | **Low_leve_Test ID** | **Description**       | **Exp IN** | **Exp OUT** | **Actual Out** |**Type Of Test**  |    
| :-------------------: | :------------------: | :-------------------: | :--------: | :---------: |:-------------: | :--------------: |
| H_01 | L_1.1 | Input the fish quantity, price | Total cost | Total cost | Manual |
|  | L_1.2 | Input the plant quantity, price | Total cost | Total cost | Mannual |
| H_02 | L_2.1 | Crop report | NA | Plant health report | Plant health report  | Mannual |
| H_03 | L_3.1 | Amount of fish or plant | Output the income generated | Output the income generated |Mannual |
| H_04 | L_4.1 | Plant health | Display the report| Display the report |Mannual |
| H_05 | L_5.1 | Input the nitrite level | Safety level of the water | Safety level of the water |Mannual |
|  | L_5.2 | Input the ammonia level | Safety level of the water | Safety level of the water | Manual |
|  | L_5.3 | Input from the sensor | Safety level of the water | Safety level of the water | Manual |
| H_06 | L_6.1 | Fire alarm override |Manual on fire alarm | Manual on fire alarm  |Mannual |
|  | L_6.2 | Fire alarm override |Manual off fire alarm | Manual off fire alarm  |Mannual |
| H_07 | L_7.1 | Exit the system | Program close | Program close | Manual | 
------------------------------------------------------------------------------------------------
