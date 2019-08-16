# Installation
## Pre-installation
### Setting up environment
Besides installing VisIT, sure you are running an environment with python 2.7. The VisIt library is not compatible with Python 3.
[Download VisIt](https://wci.llnl.gov/simulation/computer-codes/visit/executables)
[Download Anaconda](https://www.anaconda.com/distribution/)
Or
[Download Miniconda](https://docs.conda.io/en/latest/miniconda.html)
[Instructions](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/) for creating environment using Anaconda/Miniconda. Reminder: To activate environment type `conda activate envname`.
You must also add VisIt to your path "C:\Program Files\LLNL\VisIt 3.0.0". 

###Installing PyvisFile
If you are somehow trying to run this package on MacOs or Linux. Follow the instrucitons at this [link](https://mathema.tician.de/software/pyvisfile/)
However, on Windows, we will need to improvise slightly.
(Work In Progress)

## Building ParseLy

Clone the library and navigate to the folder

    git clone https://github.com/hturner08/Parsely
    cd Parsely

Install the dependencies

    pip install pandas
    pip install numpy

Build and install the library

    pip install /path/to/Parsely

## Usage
You can now use and run the scripts found in the bin folder `cd bin`. Run `python <script_name> -h` for more instructions on each script.

## Documentation
Documentation can be found [here](https://github.com/hturner08)
