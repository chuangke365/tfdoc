
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="API_Bindings.html">API Bindings</a> / MATLAB - API Bindings

.. _api_bindings_matlab:

MATLAB - API Bindings
=====================

**Requirements**: MATLAB or Octave with Java support.

The bindings (:ref:`download <downloads_bindings_examples>`) consist of
two .jar files with the bindings for all Tinkerforge Bricks and Bricklets
for MATLAB and Octave (in ``matlab/Tinkerforge.jar``) and
(in ``octave/Tinkerforge.jar``) respectively. The source (in ``matlab/source/``)
for MATLAB and (in ``octave/source/``) for Octave and all available
Matlab and Octave examples (in ``matlab/examples/``) and (in ``octave/examples/``).


Testing an Example on MATLAB
----------------------------

First thing you have to make sure is that the Java support for MATLAB is
configured properly. Currently MATLAB only works with Java version 1.6.
So if you have some other version of Java installed on your system then
you have to make sure that MATLAB Java uses Java version 1.6.

Usually MATLAB is by default configured with Java support.

You can verify the MATLAB Java interface with the following command::

 version -java

Execute this command from your MATLAB console.

If it is made sure that MATLAB has the Java interface properly configured
the next thing to make sure is to add the ``Tinkerforge.jar`` file to the
``javaclasspath`` of MATLAB. To do this, place the ``Tinkerforge.jar`` file
for MATLAB to the MATLAB installation root directory.

Then add the following line::

 $matlabroot/Tinkerforge.jar

to the file located at,
<MATLAB_INSTALLATION_ROOT>/toolbox/local/classpath.txt

This applies for both Windows and Linux installation of MATLAB.

Now all the MATLAB examples can be tried out simply by executing them
form MATLAB console.


Testing an Example on Octave
----------------------------

Just like MATLAB for Octave it is important to verify that java support
is enabled. For Linux install Octave and the package ``octave_java`` from the
distribution's official repository. This should make Octave's Java support
properly configured. Now add the following line::

 javaaddpath("<PATH/TO/Tinkerforge.jar>");

to the file located at,
~/.octaverc

If this file is not there then create one. After adding this line
restart Octave if you had any running Octave console. Now the exmaples
can be executed from Octave console.

For using these bindings with Octave in Windows you need to setup the
MinGW version of Octave. This version comes preconfigured with Java support
enabled by default. Follow the instructions from here to set up Octave
in Windows::

 http://wiki.octave.org/Octave_for_Microsoft_Windows
 
Once Octave setup is complete then run Octave console and from the console
add the ``Tinkerforge.jar`` file for Octave with the following command::

 javaaddpath("<PATH_TO_Tinkerforge.jar>");

Now all the examples should be able to execute from Octave console.


API Documentation and Examples
------------------------------

Links to the API documentation for the IP Connection, Bricks and Bricklets as
well as the examples from the ZIP file of the bindings are listed in the
following table.

.. include:: API_Bindings_MATLAB_links.table

Further project descriptions can be found in the :ref:`kits <index_kits>` section.