
:breadcrumbs: <a href="../index.html">Home</a> / <a href="../index.html#software">Software</a> / <a href="Brickv.html">Brick Viewer (brickv)</a> / Brick Viewer Installation on Linux

.. _brickv_install_linux:

Brick Viewer Installation on Linux
==================================

The :ref:`Brick Viewer <brickv>` can be installed on Debian based distribution
(Ubuntu, Mint, etc.) from a ``.deb`` file. On other distributions it can be
installed from source.


Debian Package
--------------

First, download the Brick Viewer ``.deb`` from :ref:`here <downloads_tools>`.
Right-click on the file and choose "Open with GDebi Package Installer":

.. image:: /Images/Screenshots/brickv_linux_1_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 1
   :align: center
   :target: ../_images/Screenshots/brickv_linux_1.jpg

Then click "Install Package":

.. image:: /Images/Screenshots/brickv_linux_2_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 2
   :align: center
   :target: ../_images/Screenshots/brickv_linux_2.jpg

Ready:

.. image:: /Images/Screenshots/brickv_linux_3_small.jpg
   :scale: 100 %
   :alt: Brickv installation step 3
   :align: center
   :target: ../_images/Screenshots/brickv_linux_3.jpg

In Ubuntu you can also use the Ubuntu Software Center, other Desktop
environments have very similar tools that practically work the same way.
You can start the Brick Viewer in the application menu under electronic
or in a terminal with::

 brickv

To install Brick Viewer from the terminal use the following::

 wget http://download.tinkerforge.com/tools/brickv/linux/brickv_linux_latest.deb
 sudo apt-get install python python-qt4 python-qt4-gl python-opengl python-serial
 sudo dpkg -i brickv_linux_latest.deb


From Source
-----------

To install Brick Viewer from source, download the source from
:ref:`here <downloads_tools>` and install the dependencies:

* python
* python-qt4
* python-qt4-gl
* python-opengl
* python-serial
* pyqt4-dev-tools

On Debian based distributions you install them via ``apt-get``. On other
distribution you have to search for and install the equivalent packages::

 sudo apt-get install python python-qt4 python-qt4-gl python-opengl python-serial pyqt4-dev-tools

First you have to build the Qt ``.ui`` files (you'll need ``pyuic4`` for that),
change to the folder ``src/`` and run::

 python build_all_ui.py

After that you should be able to start brickv from source, change to the folder
``src/brickv/`` and start with::

 python main.py
