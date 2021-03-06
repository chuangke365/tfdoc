
:breadcrumbs: <a href="../../index.html">Startseite</a> / <a href="../../index.html#hardware">Hardware</a> / Voltage/Current Bricklet
:shoplink: ../../../shop/bricklets/voltage-current-bricklet.html

.. include:: Voltage_Current.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _voltage_current_bricklet:

Voltage/Current Bricklet
========================

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_voltage_current_tilted_350.jpg",
	               "Bricklets/bricklet_voltage_current_tilted_600.jpg",
	               "Voltage/Current Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_current_horizontal_100.jpg",
	             "Bricklets/bricklet_voltage_current_horizontal_600.jpg",
	             "Voltage/Current Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_current_vertical_100.jpg",
	             "Bricklets/bricklet_voltage_current_vertical_600.jpg",
	             "Voltage/Current Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_current_setup_100.jpg",
	             "Bricklets/bricklet_voltage_current_setup_600.jpg",
	             "Voltage/Current Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Cases/bricklet_voltage_current_case_100.jpg",
	             "Cases/bricklet_voltage_current_case_600.jpg",
	             "Voltage/Current Bricklet im Gehäuse")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_voltage_current_brickv_100.png",
	             "Bricklets/bricklet_voltage_current_brickv.png",
	             "Voltage/Current Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/voltage_current_bricklet_dimensions_100.png",
	             "Dimensions/voltage_current_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* Misst Leistung, Spannung und Strom bis zu 720W/36V/20A
* Auflösung 1mW, 1mV, 1mA über kompletten Messbereich
* Bidirektionale Strommessung (z.B. Laden/Entladen)
* Konfigurierbare Mittelwertbildung und ADC-Wandlungszeit


.. _voltage_current_bricklet_description:

Beschreibung
------------

Mit dem Voltage/Current :ref:`Bricklet <primer_bricklets>` können
:ref:`Bricks <primer_bricks>` um die Fähigkeit Leistung/Spannung/Strom
zu messen erweitert werden. Das Bricklet wird einfach
zwischen Spannungsversorgung (z.B. Batterie) und Last (z.B. Motor) eingebaut.

In akkubetriebenen Systemen können über die bidirektionale Strommessung
Aussagen über den Ladezustand des Akkus getroffen werden.


Technische Spezifikation
------------------------

================================  ============================================================
Eigenschaft                       Wert
================================  ============================================================
Sensor                            INA226 mit 4m Ohm Shunt Widerstand
Stromverbrauch                    1mA
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Maximaler Strom                   +-20A
Maximale Spannung                 36V
--------------------------------  ------------------------------------------------------------
--------------------------------  ------------------------------------------------------------
Abmessung (B x T x H)             30 x 30 x 18mm (1,18 x 1,18 x 0,67")
Gewicht                           10g
================================  ============================================================


Ressourcen
----------

* INA226 Datenblatt (`Download <https://github.com/Tinkerforge/voltage-current-bricklet/raw/master/datasheets/ina226.pdf>`__)
* Schaltplan (`Download <https://github.com/Tinkerforge/voltage-current-bricklet/raw/master/hardware/voltage-current-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/voltage_current_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/voltage-current-bricklet/zipball/master>`__)


Anschlussmöglichkeit
--------------------

Das Voltage/Current Bricklet wird einfach zwischen Stromversorgung und der 
Last eingebaut. Schließe an die Klemme beschriftet mit "IN" die 
Stromversorgung an. An die Klemme "OUT" die Last. Die Polung ist mit "+" 
und "-" vor der Klemme gekennzeichnet.

.. warning::

 Die Polung beim Anschließen unbedingt beachten! Das Bricklet ist nicht
 verpolungssicher!


Kalibrierung
------------

Die Strommessung des Voltage/Current Bricklet ist bei Raumtemperatur
Werkskalibriert worden. Die Messwerte können um wenige mA
verschieben falls in einer sehr kalten oder sehr warmen Umgebung
gemessen wird. Mit einem präzisen Multimeter kann dies allerdings
leicht behoben werden:

Dazu muss zuerst im Brick Viewer für den "Gain Multiplier" und
"Gain Divisor" 1 eingetragen werden. Dann muss "Save Calibration"
geklickt werden und danach kann dann der reale Strom
vom Multimeter abgelesen werden und im Feld "Gain Multiplier"
eingetragen werden. Im Feld "Gain Divisor" wird der aktuelle
Messwert des Voltage/Current Bricklet eingetragen. Danach
noch einmal "Save Calibration" klicken.

Das Voltage/Current Bricklet ist nun für die neue Umgebung kalibriert.


.. _voltage_current_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.

Als nächstes muss noch eine Last und eine Stromquelle mit dem Bricklet 
verbunden werden.  
Zum Beispiel einen Motor und eine Batterie wie im folgenden Bild.

.. image:: /Images/Bricklets/bricklet_voltage_current_setup_600.jpg
   :scale: 100 %
   :alt: Voltage/Current Bricklet with Battery and Motor connected to Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_setup_1200.jpg

|test_tab|

Wenn alles wie erwartet funktioniert wird die Stromaufnahme des Motors 
angezeigt.
Der Graph gibt den zeitlichen Verlauf der Stromaufnahme wieder. Es ist
zu erkennen, dass die Spannung Aufgrund der hohen Last ein wenig einbricht
und der Motor ungefähr 40W Leistung verbraucht.

.. image:: /Images/Bricklets/bricklet_voltage_current_brickv.png
   :scale: 70 %
   :alt: Voltage/Current Bricklet in Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_voltage_current_brickv.png

|test_pi_ref|

.. _voltage_current_bricklet_case:

Gehäuse
-------

Ein `laser-geschnittenes Gehäuse für das Voltage/Current Bricklet
<https://www.tinkerforge.com/de/shop/cases/case-voltage-current-bricklet.html>`__ ist verfügbar.

.. image:: /Images/Cases/bricklet_voltage_current_case_350.jpg
   :scale: 100 %
   :alt: Gehäuse für Voltage/Current Bricklet
   :align: center
   :target: ../../_images/Cases/bricklet_voltage_current_case_1000.jpg

.. include:: Voltage_Current.substitutions
   :start-after: >>>bricklet_case_steps
   :end-before: <<<bricklet_case_steps

.. image:: /Images/Exploded/voltage_current_exploded_350.png
   :scale: 100 %
   :alt: Explosionszeichnung für Voltage/Current Bricklet
   :align: center
   :target: ../../_images/Exploded/voltage_current_exploded.png

|bricklet_case_hint|


.. _voltage_current_bricklet_programming_interface:

Programmierschnittstelle
------------------------

Siehe :ref:`Programmierschnittstelle <programming_interface>` für eine detaillierte
Beschreibung.

.. include:: Voltage_Current_hlpi.table
