.. _ipcon_python:

Python - IP Connection
======================

This is the API description for the Python bindings of the IP Connection.
The IP Connection is established between the Brick Daemon
and the corresponding programming language API bindings. You need to
create an IP Connection to brickd and add devices, before you can
use them.

An overview of products that are controllable over an IP Connection
can be found :ref:`here <product_overview>`.


.. _ipcon_python_examples:

Example
--------

The example code below is public domain.

`Download <https://github.com/Tinkerforge/doc/raw/master/source/Software/example.py>`__

.. literalinclude:: example.py
 :language: python
 :linenos:
 :tab-width: 4


.. _ipcon_python_api:

API
---

Basic Functions
^^^^^^^^^^^^^^^

.. py:function:: IPConnection(host, port)

 :param host: str
 :param port: int

 Creates an IP Connection to the Brick Daemon with the given *host*
 and *port*. With the IP Connection itself it is possible to enumerate the
 available devices. Other then that it is only used to add Bricks and
 Bricklets to the connection.

.. py:function:: IPConnection.add_device(device)

 :param device: Device
 :rtype: None

 Adds a device (Brick or Bricklet) to the IP Connection. Every device
 has to be added to an IP Connection before it can be used. Examples for
 this can be found in the API documentation for every Brick and Bricklet.

.. py:function:: IPConnection.join_thread()

 :rtype: None

 Joins the threads of the IP Connection. The call will block until the
 IP Connection is :py:func:`destroyed <IPConnection.destroy>`.

 This is useful if you relies solely on callbacks for events or if
 the IP Connection was created in a threads.

.. py:function:: IPConnection.destroy()
 
 :rtype: None

 Destroys the IP Connection. The socket to the Brick Daemon will be closed
 and the threads of the IP Connection terminated.


Callback Configuration Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:function:: IPConnection.enumerate(callback)

 :param callback: callable(uid, name, stack_id, is_new)
 :rtype: None

 This method registers a callback that receives four parameters:

 * *uid* - str: The UID of the device.
 * *name* - str: The name of the device (includes "Brick" or "Bricklet" and a version number).
 * *stack_id* - int: The stack ID of the device (you can find out the position in a stack with this).
 * *is_new* - bool: *True* if the device is added, *False* if it is removed.

 There are three different possibilities for the callback to be called.
 Firstly, the callback is called with all currently connected devices
 (with *is_new* set to *True*). This is triggered by the call to
 :py:func:`enumerate <IPConnection.enumerate>`. Secondly, the callback is called if
 a new Brick is plugged in via USB (with *is_new* set to *True*) and lastly it is
 called if a Brick is unplugged (with *is_new* set to *False*).

 It should be possible to implement "plug 'n play" functionality with this
 (as is done in Brick Viewer).