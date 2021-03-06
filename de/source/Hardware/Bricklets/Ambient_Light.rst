
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Ambient Light Bricklet
:shoplink: ../../../shop/bricklets/ambient-light-bricklet.html

.. include:: Ambient_Light.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions


.. _ambient_light_bricklet:

Ambient Light Bricklet
======================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_ambient_light_tilted_350.jpg",
	               "Bricklets/bricklet_ambient_light_tilted_600.jpg",
	               "Ambient Light Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ambient_light_vertical_100.jpg",
	             "Bricklets/bricklet_ambient_light_vertical_600.jpg",
	             "Ambient Light Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ambient_light_horizontal_100.jpg",
	             "Bricklets/bricklet_ambient_light_horizontal_600.jpg",
	             "Ambient Light Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ambient_light_master_100.jpg",
	             "Bricklets/bricklet_ambient_light_master_600.jpg",
	             "Ambient Light Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Cases/bricklet_ambient_light_case_built_up_100.jpg",
	             "Cases/bricklet_ambient_light_case_built_up_600.jpg",
	             "Ambient Light Bricklet in Case")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_ambient_light_brickv_100.jpg",
	             "Bricklets/bricklet_ambient_light_brickv.jpg",
	             "Ambient Light Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/ambient_light_bricklet_dimensions_100.png",
	             "Dimensions/ambient_light_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst Umgebungslicht bis zu 900Lux
* Ausgabe in 0,1Lux Schritten (12Bit Auflösung)


.. _ambient_light_bricklet_description:

Beschreibung
------------

Mit dem Ambient Light :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` die Umgebungshelligkeit messen.
Die gemessene Helligkeit kann in `Lux <http://de.wikipedia.org/wiki/Lux>`__
ausgelesen werden. Mit konfigurierbaren Events ist es möglich auf
Helligkeitsänderungen zu reagieren ohne die Werte laufend abzufragen
(kein Polling notwendig).

Dieses Board kann genutzt werden um z.B. helligkeitsabhängig Beleuchtungen
oder Motoren zu steuern.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            TEMT6000
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Beleuchtungsstärke                0Lux - 900Lux in 0,1Lux Schritten, 12Bit Auflösung
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessungen (B x T x H)           25 x 15 x 5mm (0,98 x 0,59 x 0,19")
Gewicht                           2g
================================  ============================================================


Ressourcen
----------

* TEMT6000 Datenblatt (`Download <https://github.com/Tinkerforge/ambient-light-bricklet/raw/master/datasheets/TEMT6000.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/ambient-light-bricklet/raw/master/hardware/ambient-light-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/ambient_light_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/ambient-light-bricklet/zipball/master>`__)


.. _ambient_light_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect| (siehe folgendes Bild).

.. image:: /Images/Bricklets/bricklet_ambient_light_master_600.jpg
   :scale: 100 %
   :alt: Ambient Light Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_ambient_light_master_1200.jpg

|test_tab|
Wenn alles wie erwartet funktioniert wird die Beleuchtungsstärke in Lux
angezeigt. Der Graph gibt den zeitlichen Verlauf der Beleuchtungsstärke wieder.

Ein guter Test für den Sensor ist es den Raum abzudunkeln und eine Taschenlampe
langsam über den Sensor hinweg zu bewegen. Der resultierende Graph sollte
ungefähr so aussehen wie auf dem folgenden Screenshot.

.. image:: /Images/Bricklets/bricklet_ambient_light_brickv.jpg
   :scale: 100 %
   :alt: Ambient Light Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_ambient_light_brickv.jpg

|test_pi_ref|

.. _ambient_light_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Ambient Light Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-ambient-light-barometer-humidity-temperature-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_ambient_light_case_built_up_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Ambient Light Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_ambient_light_case_built_up_1000.jpg

.. include:: Ambient_Light.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/ambient_light_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Ambient Light Bricklet
   :align: center
   :target: ../../_images/Exploded/ambient_light_exploded.png

|bricklet_case_hint|


.. _ambient_light_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Ambient_Light_hlpi.table
