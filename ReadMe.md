Welcome!  This suite of Python scripts is intended to be used for fitting 
radio-astronomical data obtained from the NsfIntegrate program.

fit_multi.py allows you to fit a scan with up to 4 Gaussian peaks, 
each peak with its own fit-able center, coefficient (height) and full-width at half max

SETTING UP THESE PROGRAMS FOR THE FIRST TIME
The Matplotlib program is required for plotting. PIP install using the command below:
$ pip install matplotlib
The subfolder "data" should contain the programs below.
parameters.txt
plotvel.py
<datafile>.kel

FITTING YOUR DATA
Go to the "data" subfolder and open the file "parameters.txt"
On line 3, enter the name of the kel file that you wish to fit.
Make sure this file is also in the "data" subfolder.
Set values for lower and upper fit threshold velocities in km/s
In the "S" lines, enter the stepsizes and maximum allowed steps

Set values for Peaks A, B, C and D
Flags appear after parameters and should be set to either "0" or "1"
For initial guess, set all flags to "0"
For subsequent fitting, set flags to "1" for parameters you wish to fit
To remove a peak from your fit, set its flags and coefficient to "0"
Save "parameters.txt" after you have made your changes.

Return to folder "fit_multi"
Enter the command below:
$ python fit_multi.py
After running, the program will display the fit to your data.
It will display your best-fit values in the terminal window and store them in a .dat file.
