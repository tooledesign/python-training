## Download and Extract the Repository
Navigate to [Github](https://github.com/tooledesign/python-training) and **click code > download zip**

![image](https://github.com/user-attachments/assets/b1549bbf-b2f7-4b1d-bb66-c5bf16988c9d)

Extract the zipped folder to a location on your computer (e.g., C:\code\python-training-main)

## Open the Project in VS Code
Click on the Explorer icon (2 papers) and open the folder location where python-training-main was extracted to.

![image](https://github.com/user-attachments/assets/85a6e19e-57f3-41b7-b9ec-15d162879eab)

## Open the Terminal in VS Code

Next, click **View > Terminal**

Click the drop down to change to **Command Prompt**

![image](https://github.com/user-attachments/assets/60691b20-33a0-4475-98be-0a73e65b9e3b)

## Set up a Virtual Environment

type ```python -m venv venv```

type ```venv/scripts/activate```

![image](https://github.com/user-attachments/assets/b63758fe-0f64-44a9-a4f9-f75cc029a4bb)

## Install Dependencies

Type ```python -m pip install -r requirements.txt```

This process takes about 8 minutes to run.  During this process you may notice a pop up asking to install the python extension.  Click **yes/allow** when this happens.

This is what you will see at the start of the command running:

![image](https://github.com/user-attachments/assets/0bd6cf36-4011-48b3-a8b8-358e5a441999)

This is what you will see when the command ends:

![image](https://github.com/user-attachments/assets/40af5080-380e-4107-afd2-781755c56caa)

## Confirm Environment Setup is Done

Open 01B Basic Data and run (play sign) the Load Dependencies cell.  This will prompt to install the Jupyter extension.  Click **yes/allow**.  Once Jupyter is installed, click **select a python environment** in the search bar and select your virtual environment **venv (Python 3.13.2)**

Your cell should show a green check and duration of how long it took to execute the cell if successful.

![image](https://github.com/user-attachments/assets/a840d0fb-0b1a-4217-983f-a3600e2c54c0)















