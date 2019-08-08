# Workflow Manual Outline
This manual will provide you with the instructions needed to calculate neutron and photon heat deposition on a model
## Building and Simulating the Model
  To build the model, we'll be using an excel spreadsheet embedded with Visual Basic code called an Ibuilder. Using this file type, we can generate parametric cases of our model in the cell card format read by MCNP. Once you have your cell cards, you can then run MCNP with the file name as the input. When MCNP is done, it will output a meshtal file.
## Parsing the results
  The next step is to convert the meshtal file to a flat text file readable by our visualization software, VisIt. To do this, we'll use a library called Parsely. The documentation can be found [here](https://github.com/hturner08/Parsely).
## Visualization
  Using the Parsely plotter module, we can graph our results in VisIT. You can either graph a scatterplot or isosurface of the data.
