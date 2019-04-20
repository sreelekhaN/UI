import easygui as gui
# The different modules should be called here

def Linear():       
    print("Linear Module called")

def Non_Linear():
    print("Non Linear Module called")

def ANOVA():
    print("ANOVA called")

def ARIMA():
    print("ARIMA")

def synthetic_gen():
    print("Synthetic data generation")




Title="Sri Venkateshwara Book Store"

# Choosing the module
options=["Choice 1: Linear","Choice 2: Non-Linear","Choice 3:ANOVA","Choice 4:ARIMA","Choice 5:Synthetic Data Generation"]

button=gui.buttonbox("Choose the module which has to be run",title=Title,choices=options)

# Running the module fuction based on the option chosen
if button==options[0]:
    Linear()
    button="Linear Function called"
elif button==options[1]:
     Non_Linear()
     button="Non Linear Function called"
elif button==options[2]:
    ANOVA()
    button="ANOVA table"
elif button==options[3]:
    ARIMA()
    button="ARIMA"
elif button==options[4]:
   synthetic_gen()
   button="synthetic data"
else:
    button="Wrong Choice"


gui.msgbox(msg=button,title="Sri Venkateshwara Book Store")
