
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#hardware">Hardware</a> / Moisture Bricklet
:shoplink: ../../../shop/bricklets/moisture-bricklet.html

.. include:: Moisture.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _moisture_bricklet:

Moisture Bricklet
=================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_moisture_tilted_350.jpg",
	               "Bricklets/bricklet_moisture_tilted_600.jpg",
	               "Moisture Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_vertical_100.jpg",
	             "Bricklets/bricklet_moisture_vertical_600.jpg",
	             "Moisture Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_horizontal_100.jpg",
	             "Bricklets/bricklet_moisture_horizontal_600.jpg",
	             "Moisture Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_tilted_back_100.jpg",
	             "Bricklets/bricklet_moisture_tilted_back_600.jpg",
	             "Moisture Bricklet")
	}}
	{{
	    tfdocimg("Cases/bricklet_moisture_case_tilted_front_100.jpg",
	             "Cases/bricklet_moisture_case_tilted_front_600.jpg",
	             "Moisture Bricklet in Case")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_plant1_100.jpg",
	             "Bricklets/bricklet_moisture_plant1_600.jpg",
	             "Moisture Bricklet in Soil of Plant")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_plant2_100.jpg",
	             "Bricklets/bricklet_moisture_plant2_600.jpg",
	             "Moisture Bricklet in Soil of Plant")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_moisture_brickv_100.jpg",
	             "Bricklets/bricklet_moisture_brickv.jpg",
	             "Moisture Bricklet in Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/moisture_bricklet_dimensions_100.png",
	             "Dimensions/moisture_bricklet_dimensions_600.png",
	             "Outline and drilling plan")
	}}
	{{ tfdocend() }}


Features
--------

* Measures moisture between two probes
* 12bit resolution


.. _moisture_bricklet_description:

Description
-----------

The Moisture :ref:`Bricklet <primer_bricklets>` is intended to
measure moisture in soil. It can extend :ref:`Bricks <primer_bricks>` by this
feature.

Current is passed through two probes. With a increasing moisture level the
resistance between the probes will decrease (since water is a better conductor
than soil). The change in resistance is measured and returned as the moisture
value.

You can either stick the Bricklet directly into soil or you can solder two
probes to the Bricklet and put the probes in soil.

It is also possible to use the Moisture Bricklet as a detector for water
filling level. 

Technical Specifications
------------------------

================================  ============================================================
Property                          Value
================================  ============================================================
Current Consumption               1mA (dry) - 20mA (wet)
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Resolution                        12bit
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Dimensions (W x D x H)            20 x 45 x 5mm (0.79 x 1.77 x 0.2")
Weight                            3g
================================  ============================================================


Resources
---------

* Schematic (`Download <https://github.com/Tinkerforge/moisture-bricklet/raw/master/hardware/moisture-schematic.pdf>`__)
* Outline and drilling plan (`Download <../../_images/Dimensions/moisture_bricklet_dimensions.png>`__)
* Source code and design files (`Download <https://github.com/Tinkerforge/moisture-bricklet/zipball/master>`__)


.. _moisture_bricklet_test:

Test your Moisture Bricklet
---------------------------

|test_intro|

|test_connect|.

|test_tab|
If everything went as expected you can now see changes of the moisture
value.

.. image:: /Images/Bricklets/bricklet_moisture_brickv.jpg
   :scale: 100 %
   :alt: Moisture Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_moisture_brickv.jpg

|test_pi_ref|

.. _moisture_bricklet_case:

Case
----

A `laser-cut case for the Moisture Bricklet
<https://www.tinkerforge.com/en/shop/cases/case-moisture-bricklet.html>`__ is available.

.. image:: /Images/Cases/bricklet_moisture_case_tilted_front_350.jpg
   :scale: 100 %
   :alt: Case for Moisture Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_moisture_case_tilted_front_1000.jpg

The assembly is easiest if you follow the following steps:

* Screw spacers to the Bricklet,
* build up side plates and put them around Bricklet,
* screw bottom plate to bottom spacers,
* screw top plate to top spacers.

Below you can see an exploded assembly drawing of the Moisture Bricklet case:

.. image:: /Images/Exploded/moisture_exploded_350.png
   :scale: 100 %
   :alt: Exploded assembly drawing for Moisture Bricklet
   :align: center
   :target: ../../_images/Exploded/moisture_exploded.png

|bricklet_case_hint|


.. _moisture_bricklet_programming_interface:

Programming Interface
---------------------

See :ref:`Programming Interface <programming_interface>` for a detailed description.

.. include:: Moisture_hlpi.table
