.. Tinkerforge documentation master file, created by
   sphinx-quickstart on Fri Apr 29 12:57:06 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

#############
Documentation
#############


.. _index_tutorials:

*****************
Tutorials and FAQ
*****************

A general description of Bricks, Master Extensions Bricklets and concepts
can be found in the :ref:`Primer <primer>`.

These Tutorials are an introduction to the usage of Bricks and Bricklets
and their concepts:

* :ref:`First Steps <tutorial_first_steps>`
* :ref:`Rugged Approach <tutorial_rugged_approach>`
* :ref:`Authentication <tutorial_authentication>`
* :ref:`RED Brick <tutorial_red_brick>`

Answers to frequently asked questions can be found in the :ref:`FAQ <faq>`.

.. toctree::
   :hidden:

   Tutorials/Tutorial_Extending/Tutorial
   Tutorials/Tutorial_Rugged/Tutorial
   Tutorials/Tutorial_Authentication/Tutorial
   Tutorials/Tutorial_RED_Brick/Tutorial
   FAQ


.. _index_hardware:

********
Hardware
********

Our :ref:`products <primer_products>` are divided into five different categories:

* :ref:`primer_bricks`
* :ref:`primer_bricklets`
* :ref:`primer_master_extensions`
* :ref:`primer_power_supplies`
* :ref:`primer_accessories`

This :ref:`Timeline <timeline>` presents an overview of released products and
finished developments.

.. raw:: html
   :file: index_hardware.html

.. toctree::
   :hidden:

   Primer
   Timeline

.. toctree::
   :glob:
   :hidden:

   Hardware/Bricks/*
   Hardware/Bricklets/*
   Hardware/Master_Extensions/*
   Hardware/Power_Supplies/*
   Hardware/Accessories/*


.. _index_software:

********
Software
********

The software includes service and test programs, the API bindings to interact
with Bricks and Bricklets as well as their firmwares and plugins:

* :ref:`brickd`
* :ref:`brickv`
* :ref:`api_bindings`
* :ref:`firmwares_and_plugins`

Those can be downloaded in the :ref:`downloads section <downloads>`. The
:ref:`source code and links for bug trackers <source_code>` can be found in
their own section.

The basics of the programming interface are described :ref:`here
<programming_interface>`.

.. raw:: html
   :file: index_api.html

.. toctree::
   :hidden:

   Software/Brickd
   Software/Brickv
   Software/API_Bindings
   Software/Firmwares_And_Plugins
   Downloads
   Source_Code
   Programming_Interface
   Transitioning_Guide_1To2

.. toctree::
   :glob:
   :hidden:

   Software/*

.. include:: Software/Bricks.toctree

.. include:: Software/Bricklets.toctree


.. _index_kits:

************
Starter Kits
************

We offer kits for different subject areas so you can get started more easily
with Tinkerforge:

* :ref:`starter_kit_weather_station`
* :ref:`starter_kit_hardware_hacking`
* :ref:`starter_kit_server_room_monitoring`
* :ref:`starter_kit_blinkenlights`
* :ref:`starter_kit_iot`

.. toctree::
   :hidden:

   Kits/WeatherStation/WeatherStation
   Kits/HardwareHacking/HardwareHacking
   Kits/ServerRoomMonitoring/ServerRoomMonitoring
   Kits/Blinkenlights/Blinkenlights
   Kits/InternetOfThings/InternetOfThings


.. _index_embedded_boards:

***************
Embedded Boards
***************

Bricks and Bricklets can easily be combined with different embedded boards:

.. toctree::
   :maxdepth: 1
   :glob:

   Embedded/*


.. _index_spec:

**************
Specifications
**************

This specifications include the :ref:`technical data <technical_data>`
for the connectors used on Bricks and Bricklets as well as the different low
level protocols:

* :ref:`llproto_tcpip`
* :ref:`llproto_modbus`

A :ref:`Wireshark dissector <wireshark_dissector>` for TFP
(Tinkerforge Protocol) is available.

.. toctree::
   :hidden:

   Technical_Data
   Low_Level_Protocols/TCPIP
   Low_Level_Protocols/Modbus
   Low_Level_Protocols/Wireshark_Dissector
