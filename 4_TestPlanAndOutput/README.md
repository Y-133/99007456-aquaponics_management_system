# TEST PLAN:
 * Test plans are very helpful in checking the behaviour of the program, variables and function for different values
------------------------------------------------------------------------------------------------
## How to run the test? ##
* Load the Simulide file and arduino file in Simulide software and run the project.  
* RTD sensor value is changed using the knob feature and corresponding temperature change can be observed.
* Use the control buttons to move the space ship.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## FEATURES: ##
####
1. OLED screen
2. Effective auto cooling system
3. Portable console and has an USB chargeable features.
4. Powerful audio
####
----------------------------------------------------------------------------------------------------------------
## High level test plan

## TABLE_NO: HL_1 ##
| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual Out** |**Type Of Test** |    
| :---------: | :----------------------------------------------------------: | :---------: | :---------: | :------------: | :-------------: |
|  H_01       | Console shall turn on and the game runs | Power supply | Game running without error| no error |Mannual |
|  H_02       | Audio output: When the console is turned on the speaker shall turn on| Signal from the controller | Speaker works | no error |Mannual |
|  H_03       | RTD sensor working is checked by varying the temperature | The temperature knob in the IDE is changed to obervee the change in temperature| Temperature change and auto cooling system turns on | no error |Mannual |
|  H_04       | Fan runs when poewred using the PWM signal from the controller | Controller signal | Fan turns on | Fan turns on  |Mannual |
|  H_05       | Fan turns off after cooling the console  |  Controller signal | Fan turns off | Fan turns off  |Mannual |
|  H_06       | OLED screen turns on and the game is viewed | Controller signal | Displays game | Game is displayed |Mannual |


------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Table no: Low level test plan

## TABLE_NO: LL_1 ##
| **High_leve_Test ID** | **Low_leve_Test ID** | **Description**       | **Exp IN** | **Exp OUT** | **Actual Out** |**Type Of Test**  |    
| :-------------------: | :------------------: | :-------------------: | :--------: | :---------: |:-------------: | :--------------: |
| H_01 | L_01.1 | Console shall turn on with 5V | 5V supply | Game running without error | The game starts run with audio ouput| mannual |
| H_02  | L_2.1 | Audio output: When the console is turned on the speaker shall turn on  |  Signal from the controller |Speaker works |The intro notes and the game sound is played using the speaker | mannual |
| H_03 | L_3.1 | RTD sensor working is checked by varying the temperature | The temperature knob in the IDE is changed to obervee the change in temperature |Temperature change and auto cooling system turns on | no error |Mannual |
| H_04  | L_.4.1| Fan runs when poewred using the PWM signal from the controller | Controller signal | Fan turns on | Fan turns on  |Mannual ||
|  H_05 | L_5.1 | Fan turns off after cooling the console  |  Controller signal | Fan turns off | Fan turns off  |Mannual |
|  H_06 | L_6.1 | OLED screen turns on and the game is viewed | Controller signal | Displays game | Game is displayed |Mannual |
------------------------------------------------------------------------------------------------
