.. include:: Industrial_Quad_Relay.substitutions


.. _industrial_quad_relay_bricklet:

Industrial Quad Relay Bricklet
==============================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_industrial_quad_relay_tilted_350.jpg",
	               "Bricklets/bricklet_industrial_quad_relay_tilted_600.jpg",
	               "Industrial Quad Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_quad_relay_vertical_100.jpg",
	             "Bricklets/bricklet_industrial_quad_relay_vertical_600.jpg",
	             "Industrial Quad Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_quad_relay_horizontal_100.jpg",
	             "Bricklets/bricklet_industrial_quad_relay_horizontal_600.jpg",
	             "Industrial Quad Relay Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_quad_relay_master_100.jpg",
	             "Bricklets/bricklet_industrial_quad_relay_master_600.jpg",
	             "Industrial Quad Relay Bricklet with Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_industrial_quad_relay_brickv_100.jpg",
	             "Bricklets/bricklet_industrial_quad_relay_brickv.jpg",
	             "Industrial Quad Relay Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/industrial_quad_relay_bricklet_dimensions_100.png",
	             "Dimensions/industrial_quad_relay_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* 4 Channel Solid State Relay
* Switch up to 30V with 1.2A
* Galvanically isolated


Description
-----------

The Industrial Quad Relay :ref:`Bricklet <product_overview_bricklets>` can be used to
extend :ref:`Bricks <product_overview_bricks>` by four galvanically isolated solid state relays.
Each channel can switch up to currents up to 1.2 `Ampere <http://en.wikipedia.org/wiki/Ampere>`__
with 30 `Volt <http://en.wikipedia.org/wiki/Volt>`__. 
Output isolation permits the usage without a direct electric connection, 
such that ground loops can be prevented and an additional degree of safety is added.

Typical applications are the interfacing of industrial control, such as PLC's or frequency converters,
or the usage in environments were electrical ground levels can not be connected.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Output Type                       Four galvanically isolated solid state relays
Max. Switching Current            1.2A
Max. Switching Voltage            30V
Isolation                         1500Vrms (datasheet value)
Relay Type                        CPC1020N
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            40 x 40 x 11mm (1,57 x 1,57 x 0,43")
Weight                            8g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/industrial-quad-relay-bricklet/raw/master/hardware/analog-in-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/industrial-quad-relay_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/industrial-quad-relay-bricklet/zipball/master>`__)


Connectivity
------------

The Industrial Quad Relay Bricklet has an 8pole terminal.
Please see the picture below for the pinout.


.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_vertical_350.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay 4 Pinout
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_vertical_1200.jpg


.. _industrial_quad_relay_bricklet_test:

Test your Industrial Quad Relay Bricklet
-------------------------------------------

|test_intro|

|test_connect|.
For a simple test we will connect a battery and a LED to test the Bricklet
(see picture below).


.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_master_600.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_master_1200.jpg

|test_tab|

If everything went as expected you can switch the LED by changing the output
state with the Brick Viewer.

.. image:: /Images/Bricklets/bricklet_industrial_quad_relay_brickv.jpg
   :scale: 100 %
   :alt: Industrial Quad Relay Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_industrial_quad_relay_brickv.jpg

|test_pi_ref|


.. _industrial_digital_quad_relay_programming_interfaces:

Programming Interfaces
----------------------

High Level Programming Interface
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See :ref:`High Level Programming Interface <pi_hlpi>` for a detailed description.

.. include:: Industrial_Quad_Relay_hlpi.table