
:breadcrumbs: <a href="../../index.html">Home</a> / <a href="../../index.html#starter-kits">Starter Kits</a> / <a href="../../Kits/WeatherStation/WeatherStation.html">Starter Kit: Weather Station</a> / Using PHP to write to LCD 20x4 Bricklet

.. |ref_CALLBACK_ENUMERATE| replace:: :php:member:`CALLBACK_ENUMERATE <IPConnection::CALLBACK_ENUMERATE>`
.. |ref_CALLBACK_CONNECTED| replace:: :php:member:`CALLBACK_CONNECTED <IPConnection::CALLBACK_CONNECTED>`
.. |callback| replace:: callback
.. |ref_enumerate| replace:: :php:func:`enumerate() <IPConnection::enumerate>`
.. |ENUMERATION_TYPE_CONNECTED| replace:: ``ENUMERATION_TYPE_CONNECTED``
.. |ENUMERATION_TYPE_AVAILABLE| replace:: ``ENUMERATION_TYPE_AVAILABLE``
.. |cb_illuminance| replace:: ``cb_illuminance``
.. |cb_humidity| replace:: ``cb_humidity``
.. |cb_air_pressure| replace:: ``cb_airPressure``

.. include:: WriteToLCD.substitutions
   :start-after: >>>substitutions
   :end-before: <<<substitutions

.. _starter_kit_weather_station_php_to_lcd:

Using PHP to write to LCD 20x4 Bricklet
=======================================

.. include:: PHPCommon.substitutions
   :start-after: >>>intro
   :end-before: <<<intro


Goals
-----

.. include:: WriteToLCD.substitutions
   :start-after: >>>goals
   :end-before: <<<goals


Step 1: Discover Bricks and Bricklets
-------------------------------------

|step1_start_off|

.. code-block:: php

    <?php

    const HOST = 'localhost';
    const PORT = 4223;

    ?>

|step1_ip_address|

|step1_register_callbacks|

.. code-block:: php

    <?php

    public function __construct()
    {
        $this->ipcon = new IPConnection();
        $this->ipcon->connect(self::HOST, self::PORT);

        $this->ipcon->registerCallback(IPConnection::CALLBACK_ENUMERATE,
                                       array($this, 'cb_enumerate'));
        $this->ipcon->registerCallback(IPConnection::CALLBACK_CONNECTED,
                                       array($this, 'cb_connected'));

        $this->ipcon->enumerate();
    }

    ?>

|step1_enumerate_callback|

|step1_connected_callback|

.. code-block:: php

    <?php

    function cb_connected($connectedReason)
    {
        if($connectedReason == IPConnection::CONNECT_REASON_AUTO_RECONNECT) {
            $this->ipcon->enumerate();
        }
    }

    ?>

|step1_auto_reconnect_callback|

|step1_put_together|

.. code-block:: php

    <?php

    class WeatherStation
    {
        const HOST = 'localhost';
        const PORT = 4223;

        public function __construct()
        {
            $this->ipcon = new IPConnection();
            $this->ipcon->connect(self::HOST, self::PORT);

            $this->ipcon->registerCallback(IPConnection::CALLBACK_ENUMERATE,
                                           array($this, 'cb_enumerate'));
            $this->ipcon->registerCallback(IPConnection::CALLBACK_CONNECTED,
                                           array($this, 'cb_connected'));

            $this->ipcon->enumerate();
        }

        function cb_connected($connectedReason)
        {
            if($connectedReason == IPConnection::CONNECT_REASON_AUTO_RECONNECT) {
                $this->ipcon->enumerate();
            }
        }
    }

    ?>


Step 2: Initialize Bricklets on Enumeration
-------------------------------------------

|step2_intro|

|step2_enumerate|

.. code-block:: php

    <?php

    function cb_enumerate($uid, $connectedUid, $position, $hardwareVersion,
                          $firmwareVersion, $deviceIdentifier, $enumerationType)
    {
        if($enumerationType == IPConnection::ENUMERATION_TYPE_CONNECTED ||
           $enumerationType == IPConnection::ENUMERATION_TYPE_AVAILABLE) {

    ?>

|step2_lcd_config|

.. code-block:: php

    <?php

    if($deviceIdentifier == BrickletLCD20x4::DEVICE_IDENTIFIER) {
        $this->brickletLCD = new BrickletLCD20x4($uid, $this->ipcon);
        $this->brickletLCD->clearDisplay();
        $this->brickletLCD->backlightOn();
    }

    ?>

|step2_other_config1|

.. code-block:: php

    <?php

    else if($deviceIdentifier == BrickletAmbientLight::DEVICE_IDENTIFIER) {
        $this->brickletAmbientLight = new BrickletAmbientLight($uid, $this->ipcon);
        $this->brickletAmbientLight->setIlluminanceCallbackPeriod(1000);
        $this->brickletAmbientLight->registerCallback(BrickletAmbientLight::CALLBACK_ILLUMINANCE,
                                                      array($this, 'cb_illuminance'));
    } else if($deviceIdentifier == BrickletHumidity::DEVICE_IDENTIFIER) {
        $this->brickletHumidity = new BrickletHumidity($uid, $this->ipcon);
        $this->brickletHumidity->setHumidityCallbackPeriod(1000);
        $this->brickletHumidity->registerCallback(BrickletHumidity::CALLBACK_HUMIDITY,
                                                  array($this, 'cb_humidity'));
    } else if($deviceIdentifier == BrickletBarometer::DEVICE_IDENTIFIER) {
        $this->brickletBarometer = new BrickletBarometer($uid, $this->ipcon);
        $this->brickletBarometer->setAirPressureCallbackPeriod(1000);
        $this->brickletBarometer->registerCallback(BrickletBarometer::CALLBACK_AIR_PRESSURE,
                                                   array($this, 'cb_airPressure'));
    }

    ?>

|step2_other_config2|

|step2_put_together|

.. code-block:: php

    <?php

    function cb_enumerate($uid, $connectedUid, $position, $hardwareVersion,
                          $firmwareVersion, $deviceIdentifier, $enumerationType)
    {
        if($enumerationType == IPConnection::ENUMERATION_TYPE_CONNECTED ||
           $enumerationType == IPConnection::ENUMERATION_TYPE_AVAILABLE) {
            if($deviceIdentifier == BrickletLCD20x4::DEVICE_IDENTIFIER) {
                $this->brickletLCD = new BrickletLCD20x4($uid, $this->ipcon);
                $this->brickletLCD->clearDisplay();
                $this->brickletLCD->backlightOn();
            } else if($deviceIdentifier == BrickletAmbientLight::DEVICE_IDENTIFIER) {
                $this->brickletAmbientLight = new BrickletAmbientLight($uid, $this->ipcon);
                $this->brickletAmbientLight->setIlluminanceCallbackPeriod(1000);
                $this->brickletAmbientLight->registerCallback(BrickletAmbientLight::CALLBACK_ILLUMINANCE,
                                                              array($this, 'cb_illuminance'));
            } else if($deviceIdentifier == BrickletHumidity::DEVICE_IDENTIFIER) {
                $this->brickletHumidity = new BrickletHumidity($uid, $this->ipcon);
                $this->brickletHumidity->setHumidityCallbackPeriod(1000);
                $this->brickletHumidity->registerCallback(BrickletHumidity::CALLBACK_HUMIDITY,
                                                          array($this, 'cb_humidity'));
            } else if($deviceIdentifier == BrickletBarometer::DEVICE_IDENTIFIER) {
                $this->brickletBarometer = new BrickletBarometer($uid, $this->ipcon);
                $this->brickletBarometer->setAirPressureCallbackPeriod(1000);
                $this->brickletBarometer->registerCallback(BrickletBarometer::CALLBACK_AIR_PRESSURE,
                                                           array($this, 'cb_airPressure'));
            }
        }
    }

    ?>


Step 3: Show measurements on display
------------------------------------

|step3_intro|::

 Illuminanc 137.39 lx
 Humidity    34.10 %
 Air Press  987.70 mb
 Temperature 22.64 °C

|step3_format|

.. code-block:: php

    <?php

    $text = sprintf("%6.2f", $value);

    ?>

|step3_printf|

.. code-block:: php

    <?php

    function cb_illuminance($illuminance)
    {
        $text = sprintf("Illuminanc %6.2f lx", $illuminance/10.0);
        $this->brickletLCD->writeLine(0, 0, $text);
    }

    function cb_humidity($humidity)
    {
        $text = sprintf("Humidity   %6.2f %%", $humidity/10.0);
        $this->brickletLCD->writeLine(1, 0, $text);
    }

    function cb_airPressure($airPressure)
    {
        $text = sprintf("Air Press %7.2f mb", $airPressure/1000.0);
        $this->brickletLCD->writeLine(2, 0, $text);
    }

    ?>

|step3_temperature|

.. code-block:: php

    <?php

    function cb_airPressure($airPressure)
    {
        $text = sprintf("Air Press %7.2f mb", $airPressure/1000.0);
        $this->brickletLCD->writeLine(2, 0, $text);

        $temperature = $this->brickletBarometer->getChipTemperature();
        $text = sprintf("Temperature %5.2f %cC", $temperature/100.0, 0xDF);
        $this->brickletLCD->writeLine(3, 0, $text);
    }

    ?>

|step3_put_together|

.. code-block:: php

    <?php

    function cb_illuminance($illuminance)
    {
        $text = sprintf("Illuminanc %6.2f lx", $illuminance/10.0);
        $this->brickletLCD->writeLine(0, 0, $text);
    }

    function cb_humidity($humidity)
    {
        $text = sprintf("Humidity   %6.2f %%", $humidity/10.0);
        $this->brickletLCD->writeLine(1, 0, $text);
    }

    function cb_airPressure($airPressure)
    {
        $text = sprintf("Air Press %7.2f mb", $airPressure/1000.0);
        $this->brickletLCD->writeLine(2, 0, $text);

        $temperature = $this->brickletBarometer->getChipTemperature();
        // 0xDF == ° on LCD 20x4 charset
        $text = sprintf("Temperature %5.2f %cC", $temperature/100.0, 0xDF);
        $this->brickletLCD->writeLine(3, 0, $text);
    }

    ?>

|step3_complete|

|step3_suggestions1| |step3_suggestions2_no_thread|

|step3_robust1|

|step3_robust2|


Step 4: Error handling and Logging
----------------------------------

|step4_intro1|

.. code-block:: php

    <?php

    while(true) {
        try {
            $this->ipcon->connect(self::HOST, self::PORT);
            break;
        } catch(Exception $e) {
            sleep(1);
        }
    }

    ?>

|step4_intro2|

.. code-block:: php

    <?php

    while(true) {
        try {
            $this->ipcon->enumerate();
            break;
        } catch(Exception $e) {
            sleep(1);
        }
    }

    ?>

|step4_connect_afterwards|

|step4_lcd_initialized1|

.. code-block:: php

    <?php

    function cb_illuminance($illuminance)
    {
        if($this->brickletLCD != null) {
            $text = sprintf("Illuminanc %6.2f lx", $illuminance/10.0);
            $this->brickletLCD->writeLine(0, 0, $text);
            echo "Write to line 0: $text\n";
        }
    }

    ?>

|step4_lcd_initialized2|

.. code-block:: php

    <?php

    if($deviceIdentifier == BrickletAmbientLight::DEVICE_IDENTIFIER) {
        try {
            $this->brickletAmbientLight = new BrickletAmbientLight($uid, $this->ipcon);
            $this->brickletAmbientLight->setIlluminanceCallbackPeriod(1000);
            $this->brickletAmbientLight->registerCallback(BrickletAmbientLight::CALLBACK_ILLUMINANCE,
                                                          array($this, 'cb_illuminance'));
            echo "Ambient Light initialized\n";
        } catch(Exception $e) {
            $this->brickletAmbientLight = null;
            echo "Ambient Light init failed: $e\n";
        }
    }

    ?>

|step4_logging1|

|step4_logging2|


Step 5: Everything put together
-------------------------------

|step5_intro|

|step5_put_together| (`download <https://raw.githubusercontent.com/Tinkerforge/weather-station/master/write_to_lcd/php/WeatherStation.php>`__):

.. literalinclude:: ../../../../../weather-station/write_to_lcd/php/WeatherStation.php
 :language: php
 :tab-width: 4
