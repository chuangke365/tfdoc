.. _firmwares_and_plugins:

Firmwares and Plugins
=====================

.. note::
 If you accidentally erased the firmware of a Brick or Bricklet, you can
 download the latest firmware and plugin
 versions :ref:`here <downloads_firmwares_plugins>`.

 Only if you want to change something in a firmware of a Brick or a
 plugin of a Bricklet you will need to compile them yourself.


Building a Brick firmware
-------------------------

You can modify and build the Brick firmwares. At the moment there is no
official Brick API or documentation of the Brick firmware code. So you
will need some prior knowledge in C programming to do this.

The source code for all Bricks and Bricklets can be found in the Tinkerforge
`github account <https://github.com/Tinkerforge/>`__. In the following
a small overview on what you have to do to compile the Servo Brick firmware,
as an example.

Clone the Servo Brick repository::

 git clone https://github.com/Tinkerforge/servo-brick.git

Clone the bricklib into the ``software/src/`` folder of the firmware (a symlink
will also work)::

 cd servo-brick/software/src/
 git clone https://github.com/Tinkerforge/bricklib.git

Download and install the GCC none-eabi compiler for ARM from
`CodeSourcery <http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`__

Generate the Makefile in the ``software/`` folder (you will need CMake)::

 cd servo-brick/software/
 ./generate_makefile

Build the firmware::

 cd servo-brick/software/build/
 make

That's it. The ``software/build/`` folder now contains the newly compiled firmware.
``servo-brick.bin``.


.. _flash_firmware_on_brick:

Flash firmware on a Brick
-------------------------

See :ref:`brickv_flash_firmware` in :ref:`Brick Viewer <brickv>` documentation
for more information.


Building a Bricklet plugin
--------------------------

You can modify and build the Bricklet plugins.
You will need knowledge in C programming to do this. The plugins are
compiled as position independent code (so it is easy for the Bricks to
use them). This means that there are lots of C features you might take
for granted that will not work in Bricklet plugins. For example you
can not just call any library functions, the functions have to be provided
by the Brick through the Bricklet API (BA). Global variables have to be
written into the Bricklet Context (BC) and configuration for the Bricklet
can be read from the Bricklet Settings (BS). All of these are provided
by the Bricks to be used by Bricklet plugins. If you think you are up
to that, you should take a look at the source code to see how it exactly
works.

The source code for all Bricks and Bricklets can be found in the Tinkerforge
`github account <https://github.com/Tinkerforge/>`__. In the following
a small overview on what you have to do to compile the Joystick Bricklet
plugin, as an example.

Clone the Joystick Bricklet repository::

 git clone https://github.com/Tinkerforge/joystick-bricklet.git

Clone the bricklib and the brickletlib (you need both) into the ``software/src/``
folder of the plugin (a symlink will also work)::

 cd joystick-bricklet/software/src
 git clone https://github.com/Tinkerforge/bricklib.git
 git clone https://github.com/Tinkerforge/brickletlib.git

Download and install the GCC none-eabi compiler for ARM from
`CodeSourcery <http://www.codesourcery.com/sgpp/lite/arm/portal/subscription?@template=lite>`__

Generate the Makefile in the ``software/`` folder (you will need CMake)::

 cd joystick-bricklet/software
 ./generate_makefile

Build the plugin::

 cd joystick-bricklet/software/build/
 make

That's it. The ``software/build/`` folder now contains the newly compiled plugin:
``joystick-bricklet.bin``


Flash plugin on a Bricklet
--------------------------

See :ref:`brickv_flash_plugin` in :ref:`Brick Viewer <brickv>` documentation for
more information.