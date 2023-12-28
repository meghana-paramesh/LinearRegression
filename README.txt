step1: create a new virtual environment for python (we can also use conda default "base" environment). Example: conda activate base or python -m venv <virtual_environment_name>
step 1.1: If the virtual environment is created using python -m venv <virtual_environment_name>, please activate it using the command "source assignment2_env/bin/activate" (for linux based systems)
step2: install all the requirements from "requirement.txt". Command: pip install -r requirements.txt
step3: run the main file that is Main.py. Command: python Main.py
step4: we can validate the plots generate "initial_plot.png" and "final_plot.png"
step5: we can also validate if the loss is decreasing using training_error.png
step6: Validate the output on the console. I have also added the final values of theta_1, theta_0 and predictions (in 10,000s)
theta_1:  [[1.14305609]]
theta_0:  -3.5077046611764495
predictions for 3.5000:  [[0.49299166]]
predictions for 7.0000:  [[4.49368798]]