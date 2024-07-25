# Intelligent Energy Management System 

## Test
In order to use this program to extract and process data from given API, you can just follow the steps shown as below：

**1. Modify the IP address and user's information to conform to particular space:**
Open `config_main.yaml` and modify the url to where you want to access:
![Alt text](image.png)

Input the right username and password:
![Alt text](image-5.png)

**2. Run script in your terminal:**
We assume that you already have an anaconda base environment. In this case, you only need to run the following command in your terminal:
```bash
python main.py
```

## Expected Results
The program will export four csv files for four different usages:

`ElectricityOptimization_demo3_output1.csv`:
![Alt text](image-1.png)

`EnergyConservingBenefit_demo1_output1.csv`:
![Alt text](image-2.png)

`EnergyTuning_demo1_output1.csv`:
![Alt text](image-3.png)

`SynthesizeEnergyIncome_demo1_output1.csv`:
![Alt text](image-4.png)