## Installation Instructions
### Pre-installation
Besides installing VisIT, sure you are running an environment with python 2.7. The VisIt library is not compatible with Python 3.

[Downloading Anaconda](https://www.anaconda.com/distribution/)
Or
[Download Miniconda](https://docs.conda.io/en/latest/miniconda.html)

[Instructions](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/) for creating environment using Anaconda/Miniconda. Reminder: To activate environment type `activate envname`.

### Building ParseLy

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
