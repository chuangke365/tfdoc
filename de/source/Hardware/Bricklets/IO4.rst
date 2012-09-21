.. include:: IO4.substitutions


.. _io4_bricklet:

IO-4 Bricklet
=============

.. raw:: html

	{% from "macros.html" import tfdocstart, tfdocimg, tfdocend %}
	{{
	    tfdocstart("Bricklets/bricklet_io4_11_tilted_350.jpg",
	               "Bricklets/bricklet_io4_11_tilted_600.jpg",
	               "IO-4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_io4_11_vertical_100.jpg",
	             "Bricklets/bricklet_io4_11_vertical_600.jpg",
	             "IO-4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_io4_11_horizontal_100.jpg",
	             "Bricklets/bricklet_io4_11_horizontal_600.jpg",
	             "IO-4 Bricklet")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_io4_11_master_100.jpg",
	             "Bricklets/bricklet_io4_11_master_600.jpg",
	             "IO-4 Bricklet mit Master Brick")
	}}
	{{
	    tfdocimg("Bricklets/bricklet_io4_brickv_100.jpg",
	             "Bricklets/bricklet_io4_brickv.jpg",
	             "IO-4 Bricklet im Brick Viewer")
	}}
	{{
	    tfdocimg("Dimensions/io4_bricklet_dimensions_100.png",
	             "Dimensions/io4_bricklet_dimensions_600.png",
	             "Umriss und Bohrplan")
	}}
	{{ tfdocend() }}


Features
--------

* 4 digitale Ein- und Ausgänge
* 3,3V Logikspannung
* Konfigurierbare Pull-Ups und Interrupts


Beschreibung
------------

Mit dem IO-4 :ref:`Bricklet <product_overview_bricklets>` können
:ref:`Bricks <product_overview_bricks>` um externe digitale Ein- und Ausgänge
(I/Os) erweitert werden.

Das Bricklet besitzt 4 I/O Pins die unabhängig voneinander als Ein- oder Ausgänge
konfiguriert werden können. Jeder Eingang kann zusätzlich mit einem Pull-Up oder als
Interruptquelle konfiguriert werden. Die I/O Pins sind über Schraubklemmen nach außen
geführt. Zwei zusätzliche Schraubklemmen führen 3,3V und GND nach außen.

In typischen Anwendungen können Schalter, Taster und LEDs angeschlossen werden

Seit Hardwareversion 1.1 sitzt ein GND Pin neben jedem der 4 I/O Pins um den
Zugriff auf GND zu vereinfachen.


Technische Spezifikation
------------------------

================================  =================================================================
Eigenschaft                       Wert
================================  =================================================================
I/O Pins                          4
--------------------------------  -----------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------
I/O Spannung                      3,3V
Maximaler Ausgangsstrom           6mA
Maximale API Aufrufe*             ``set_value`` (1kHz), ``get_value`` (0,5kHz), Callbacks (1kHz)
--------------------------------  -----------------------------------------------------------------
--------------------------------  -----------------------------------------------------------------
Abmessungen (B x T x H)           35 x 35 x 14mm (1,38 x 1,38 x 0,55")
Gewicht                           14g
================================  =================================================================

\* abhängig vom jeweiligen System (Betriebssystem, CPU etc.)


Ressourcen
----------

* Schaltplan (`Download <https://github.com/Tinkerforge/io4-bricklet/raw/master/hardware/io-4-schematic.pdf>`__)
* Umriss und Bohrplan (`Download <../../_images/Dimensions/io4_bricklet_dimensions.png>`__)
* Quelltexte und Platinenlayout (`Download <https://github.com/Tinkerforge/io4-bricklet/zipball/master>`__)


.. _io4_bricklet_test:

Erster Test
-----------

|test_intro|

|test_connect|.
In unserem Testaufbau ist eine LED über einen Vorwiderstand angeschlossen,
mit Anode an Pin 3 und Kathode an einen GND Pin.
Zusätzlich ist noch ein Schiebeschalter angeschlossen der Pin 0 mit GND
verbinden kann (siehe folgendes Bild).

Ab Hardwareversion 1.1 können auch die GND Pins direkt neben den I/O Pins
benutzt werden.

.. image:: /Images/Bricklets/bricklet_io4_master_600.jpg
   :scale: 100 %
   :alt: IO-4 Bricklet verbunden mit Master Brick
   :align: center
   :target: ../../_images/Bricklets/bricklet_io4_master_1200.jpg

|test_tab|

.. image:: /Images/Bricklets/bricklet_io4_brickv.jpg
   :scale: 100 %
   :alt: IO-4 Bricklet im Brick Viewer
   :align: center
   :target: ../../_images/Bricklets/bricklet_io4_brickv.jpg

..
  FIXME: update screenshot and description for monoflop

Hier kann die "Debounce Period" eingestellt werden, dies ist die Entprellperiode
die Interrupt Callbacks. Ein Beispiel: Wenn die Debounce Period auf 100 gestellt
wird, werden Interrupts maximal alle 100ms ausgelöst. Dies ist notwendig wenn
etwas prellendes (z.B. ein Taster) an das IO-4 Bricklet angeschlossen wird.
Der optimale Wert kann im Brick Viewer ermittelt und dann später im eigenen
Programm verwendet werden.

Unter der Einstellung für die Debounce Period können die einzelnen Pins
konfiguriert werden. Jeder Pin kann als Eingang oder Ausgang betrieben werden.
Für Eingangspins kann zusätzlich ein Pull-Up geschaltet werden. Die aktuelle
Konfiguration und der Zustand der Pins ist dann in der Tabelle weiter unten
aufgelistet.

Um die LED leuchten zu lassen muss Pin 3 als Ausgang konfiguriert und auf
logisch 1 (High) gestellt werden. Um den Schiebeschalter zu testen muss Pin 0
als Eingang mit Pull-Up konfiguriert werden. Der Pull-Up ist nötig um einen
stabilen Zustand zu erreichen wenn der Schiebeschalter Pin 0 nicht mit GND
verbindet. In der Tabelle sollte sich jetzt der Zustand des Pins ändern wenn
der Schiebeschalter umgeschaltet wird.

Wenn kein Schalter oder eine LED zu Hand ist kann auch ein Voltmeter verwendet
werden um Änderungen an Ausgangspins zu messen. Interrupts an Eingangspins können
auch mit Hilfe einer Büroklammer erzeugt werden.

|test_pi_ref|


.. _io4_bricklet_programming_interfaces:

Programmierschnittstellen
-------------------------

High Level Programmierschnittstelle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Siehe :ref:`High Level Programmierschnittstelle <pi_hlpi>` für eine detaillierte
Beschreibung.

.. include:: IO4_hlpi.table