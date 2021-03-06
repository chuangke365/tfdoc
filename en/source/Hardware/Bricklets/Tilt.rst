
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Tilt Bricklet
:shoplink: ../../../shop/bricklets/tilt-bricklet.html

.. include:: Tilt.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _tilt_bricklet:

Tilt Bricklet
=============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_tilt_tilted_350.jpg",
	               "Bricklets/bricklet_tilt_tilted_600.jpg",
	               "Tilt Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_tilt_vertical_100.jpg",
	             "Bricklets/bricklet_tilt_vertical_600.jpg",
	             "Tilt Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_tilt_horizontal_100.jpg",
	             "Bricklets/bricklet_tilt_horizontal_600.jpg",
	             "Tilt Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_tilt_tilted_back_100.jpg",
	             "Bricklets/bricklet_tilt_tilted_back_600.jpg",
	             "Tilt Bricklet")
	}}
	{{
	    tfdocimg("Cases/bricklet_tilt_case_tilted_front_100.jpg",
	             "Cases/bricklet_tilt_case_tilted_front_600.jpg",
	             "Tilt Bricklet in Case")
	}} 
	{{
	    tfdocimg("Bricklets/bricklet_tilt_brickv_100.jpg",
	             "Bricklets/bricklet_tilt_brickv.jpg",
	             "Tilt Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/tilt_bricklet_dimensions_100.png",
	             "Dimensions/tilt_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Detects inclination of Bricklet (tilt switch open/closed)
* Detects if Bricklet is vibrating


.. _tilt_bricklet_description:

Description
-----------

The Tilt :ref:`Bricklet <primer_bricklets>` is equipped with a tilt
switch. It can be used by :ref:`Bricks <primer_bricks>` to detect if the 
Bricklet is tilted or if the Bricklet is vibrating.

It is possible to configure events that are triggered if the state of
the Tilt Bricklet changes.

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            25 x 15 x 15mm (0.98 x 0.59 x 0.59")
Weight                            3g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/tilt-bricklet/raw/master/hardware/tilt-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/tilt_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/tilt-bricklet/zipball/master>`__)


.. _tilt_bricklet_test:

Test your Tilt Bricklet
-----------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see the current
state of the Tilt Bricklet.

.. image:: /Images/Bricklets/bricklet_tilt_brickv.jpg
   :scale: 100 %
   :alt: Tilt Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_tilt_brickv.jpg

|test_pi_ref|

.. _tilt_bricklet_case:

Case
----

A `laser-cut case for the Tilt Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-tilt-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_tilt_case_tilted_front_350.jpg
   :scale: 100 %
   :alt: Case for Tilt Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_tilt_case_tilt_front_1000.jpg

.. include:: Tilt.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/tilt_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Tilt Bricklet
   :align: center
   :target: ../../_images/Exploded/tilt_exploded.png

|bricklet_case_hint|


.. _tilt_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Tilt_hlpi.table
