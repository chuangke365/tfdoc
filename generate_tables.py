#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import re
import urllib2
import traceback
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring as etreefromstring

sys.path.append(os.path.join(os.getcwd(), '..', '..', 'generators'))
from device_identifiers import device_identifiers

lang = 'en'


class Tool:
    def __init__(self, display_name, url_part):
        self.display_name = display_name
        self.url_part = url_part

tools = [Tool('Brick Daemon', 'brickd'),
         Tool('Brick Viewer', 'brickv')]

binding_tutorials = {
'c': {
    'en': 'http://www.cprogramming.com/',
    'de': 'http://www.cprogramming.com/' # http://www.c-howto.de/
    },
'csharp': {
    'en': 'http://csharp.net-tutorials.com/',
    'de': 'http://csharp.net-tutorials.com/'
    },
'delphi': {
    'en': 'http://www.delphibasics.co.uk/',
    'de': 'http://www.delphi-treff.de/tutorials/grundlagen/'
    },
'java': {
    'en': 'http://docs.oracle.com/javase/tutorial/',
    'de': 'http://docs.oracle.com/javase/tutorial/' # http://openbook.galileocomputing.de/javainsel/
    },
'javascript': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'mathematica': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'matlab': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'perl': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'php': {
    'en': 'http://www.php.net/manual/en/getting-started.php',
    'de': 'http://www.php.net/manual/de/getting-started.php'
    },
'python': {
    'en': 'http://www.python.org/about/gettingstarted/', # http://getpython3.com/diveintopython3/
    'de': 'http://www.python.org/about/gettingstarted/'
    },
'ruby': {
    'en': 'http://www.ruby-lang.org/en/documentation/quickstart/',
    'de': 'http://www.ruby-lang.org/de/documentation/quickstart/'
    },
'shell': {
    'en': '',
    'de': ''
    },
'vbnet': {
    'en': 'http://howtostartprogramming.com/vb-net/',
    'de': 'http://howtostartprogramming.com/vb-net/' # http://openbook.galileocomputing.de/vb_net/index.htm
    }
}

class Binding:
    def __init__(self, display_name, url_part, url_part_for_doc, is_programming_language, is_published):
        self.display_name = display_name
        self.short_display_name = display_name
        self.url_part = url_part
        self.url_part_for_doc = url_part_for_doc
        self.is_programming_language = is_programming_language
        self.is_published = is_published

        # FIXME: remove short_display_name once index table got refactored to other format
        if display_name == 'Visual Basic .NET':
            self.short_display_name = 'VB.NET'

    @property
    def tutorial(self):
        return binding_tutorials[self.url_part][lang]

bindings = [Binding('Modbus',            'modbus',      'Modbus',      False, True),
            Binding('TCP/IP',            'tcpip',       'TCPIP',       False, True),
            Binding('C/C++',             'c',           'C',           True,  True),
            Binding('C#',                'csharp',      'CSharp',      True,  True),
            Binding('Delphi/Lazarus',    'delphi',      'Delphi',      True,  True),
            Binding('Java',              'java',        'Java',        True,  True),
            Binding('JavaScript',        'javascript',  'JavaScript',  True,  True),
            Binding('LabVIEW',           'labview',     'LabVIEW',     True,  True),
            Binding('Mathematica',       'mathematica', 'Mathematica', True,  True),
            Binding('MATLAB/Octave',     'matlab',      'MATLAB',      True,  True),
            Binding('Perl',              'perl',        'Perl',        True,  True),
            Binding('PHP',               'php',         'PHP',         True,  True),
            Binding('Python',            'python',      'Python',      True,  True),
            Binding('Ruby',              'ruby',        'Ruby',        True,  True),
            Binding('Shell',             'shell',       'Shell',       True,  True),
            Binding('Visual Basic .NET', 'vbnet',       'VBNET',       True,  True)]


class Product:
    def __init__(self, display_name, url_part, bindings, is_published, has_firmware=True):
        self.display_name = display_name
        self.url_part = url_part
        self.bindings = bindings
        self.is_published = is_published
        self.has_firmware = has_firmware

    @property
    def url_part_for_hardware_doc(self):
        url_part = self.display_name.replace(' ', '_').replace('/', '_').replace('-', '').replace('2.0', 'V2')

        if url_part == 'StepDown_Power_Supply':
            url_part = 'Step_Down'

        return url_part

    @property
    def url_part_for_software_doc(self):
        return self.display_name.replace(' ', '').replace('/', '').replace('-', '').replace('2.0', 'V2')

    @property
    def url_part_for_git(self):
        return self.url_part.replace('_', '-').replace('/', '-').replace('2.0', 'v2')


brick_descriptions = {
'dc': {
    'en': 'Drives one brushed DC motor with max. 28V and 5A (peak)',
    'de': 'Steuert einen DC Motor mit max. 28V und 5A (Peak)'
    },
'debug': {
    'en': 'For Firmware Developers: JTAG and serial console',
    'de': 'Für Firmware Entwickler: JTAG und serielle Konsole'
    },
'imu': {
    'en': 'Full fledged AHRS with 9 degrees of freedom',
    'de': 'Voll ausgestattetes AHRS mit 9 Freiheitsgraden'
    },
'master': {
    'en': 'Is the basis to build stacks and has 4 Bricklet Ports',
    'de': 'Ist Grundlage um Stapel zu bauen und bietet 4 Bricklet Anschlüsse'
    },
'red': {
    'en': 'Executes user programs and controls other Bricks/Bricklets standalone',
    'de': 'Führt Programme aus und steuert andere Bricks/Bricklets selbständig'
    },
'servo': {
    'en': 'Drives up to 7 RC Servos with max. 3A',
    'de': 'Steuert bis zu 7 RC Servos mit max. 3A'
    },
'stepper': {
    'en': 'Drives one bipolar stepper motor with max. 38V and 2.5A per phase',
    'de': 'Steuert einen bipolaren Schrittmotor mit max. 38V und 2,5A pro Phase'
    }
}

class Brick(Product):
    def __init__(self, *args, **kwargs):
        Product.__init__(self, *args, **kwargs)

    @property
    def description(self):
        return brick_descriptions[self.url_part][lang]

bricks = [Brick('DC',      'dc',      bindings, True),
          Brick('Debug',   'debug',   [],       True),
          Brick('IMU',     'imu',     bindings, True),
          Brick('Master',  'master',  bindings, True),
          Brick('RED',     'red',     bindings, True, has_firmware=False),
          Brick('Servo',   'servo',   bindings, True),
          Brick('Stepper', 'stepper', bindings, True)]


bricklet_descriptions = {
'accelerometer': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'ambient_light': {
    'en': 'Measures ambient light up to 900lux',
    'de': 'Misst Umgebungslicht bis zu 900Lux'
    },
'analog_in': {
    'en': 'Measures voltages up to 45V (DC)',
    'de': 'Misst elektrische Spannungen bis zu 45V (DC)'
    },
'analog_in_v2': {
    'en': 'Measures voltages up to 42V (DC)',
    'de': 'Misst elektrische Spannungen bis zu 42V (DC)'
    },
'analog_out': {
    'en': 'Generates configurable voltages up to 5V',
    'de': 'Erzeugt konfigurierbare elektrische Spannungen bis zu 5V'
    },
'analog_out_v2': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'barometer': {
    'en': 'Measures air pressure and altitude changes',
    'de': 'Misst Luftdruck und Höhenänderungen'
    },
'breakout': {
    'en': 'Makes all Bricklet signals available',
    'de': 'Macht alle Bricklet Signale zugänglich'
    },
'color': {
    'en': 'Measures color (RGB value), illuminance and color temperature',
    'de': 'Misst Farbe (RGB Wert), Beleuchtungsstärke und Farbtemperatur'
    },
'current12': {
    'en': 'Bidirectional current sensor for up to 12.5A',
    'de': 'Bidirektionaler Stromsensor für bis zu 12,5A'
    },
'current25': {
    'en': 'Bidirectional current sensor for up to 25A',
    'de': 'Bidirektionaler Stromsensor für bis zu 25A'
    },
'distance_ir': {
    'en': 'Measures distances up to 150cm with IR light',
    'de': 'Misst Entfernungen bis zu 150cm mit IR Licht'
    },
'distance_us': {
    'en': 'Measures distances from 2cm to 400cm with ultrasound',
    'de': 'Misst Entfernungen von 2cm bis 400cm mit Ultraschall'
    },
'dual_button': {
    'en': 'Two tactile buttons with built-in blue LEDs',
    'de': 'Zwei Taster mit eingebauten blauen LEDs'
    },
'dual_relay': {
    'en': 'Two relays to switch AC/DC devices',
    'de': 'Zwei Relais um AC/DC Geräte zu schalten'
    },
'gas_detector': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'gps': {
    'en': 'Determine position, velocity and altitude',
    'de': 'Bestimmt Position, Geschwindigkeit und Höhe'
    },
'hall_effect': {
    'en': 'Detects presence of magnetic field',
    'de': 'Detektiert Magnetfelder'
    },
'heart_rate': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'humidity': {
    'en': 'Measures relative humidity',
    'de': 'Misst relative Luftfeuchtigkeit'
    },
'industrial_digital_in_4': {
    'en': '4 galvanically isolated digital inputs',
    'de': '4 galvanisch getrennte digitale Eingänge'
    },
'industrial_digital_out_4': {
    'en': '4 galvanically isolated digital outputs',
    'de': '4 galvanisch getrennte digitale Ausgänge'
    },
'industrial_dual_0_20ma': {
    'en': 'Senses two currents between 0 and 20mA (IEC 60381-1)',
    'de': 'Misst zwei Stromquellen zwischen 0 und 20mA (IEC 60381-1)'
    },
'industrial_dual_analog_in': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'industrial_quad_relay': {
    'en': '4 galvanically isolated solid state relays',
    'de': '4 galvanisch getrennte Solid State Relais'
    },
'io16': {
    'en': '16-channel digital input/output',
    'de': '16 digitale Ein- und Ausgänge'
    },
'io4': {
    'en': '4-channel digital input/output',
    'de': '4 digitale Ein- und Ausgänge'
    },
'joystick': {
    'en': '2-axis joystick with push-button',
    'de': '2-Achsen Joystick mit Taster'
    },
'laser_range_finder': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'lcd_16x2': {
    'en': '16x2 character alphanumeric display with blue backlight',
    'de': '16x2 Zeichen alphanumerisches Display'
    },
'lcd_20x4': {
    'en': '20x4 character alphanumeric display with blue backlight',
    'de': '20x4 Zeichen alphanumerisches Display'
    },
'led_strip': {
    'en': 'Controls up to 320 RGB LEDs',
    'de': 'Steuert bis zu 320 RGB LEDs'
    },
'line': {
    'en': 'Measures the reflectivity of a surface',
    'de': 'Misst die Reflektivität einer Oberfläche'
    },
'linear_poti': {
    'en': '59mm linear potentiometer',
    'de': '59mm Linear-Potentiometer'
    },
'load_cell': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'moisture': {
    'en': 'Measures moisture between two probes',
    'de': 'Misst Feuchtigkeit zwischen zwei Elektroden'
    },
'motion_detector': {
    'en': 'Passive Infrared Motion Sensor, 7m range',
    'de': 'Passiver Infrarot Bewegungssensor, 7m Reichweite'
    },
'multi_touch': {
    'en': 'Capacitive Touch Sensor for 12 electrodes',
    'de': 'Kapazitiver Touch Sensor für 12 Elektroden'
    },
'nfc_rfid': {
    'en': 'Reads and writes NFC and RFID tags',
    'de': 'Liest und schreibt NFC und RFID Tags'
    },
'piezo_buzzer': {
    'en': 'Creates 1kHz beep',
    'de': 'Erzeugt 1kHz Piepton'
    },
'piezo_speaker': {
    'en': 'Creates beep with configurable frequency',
    'de': 'Erzeugt Piepton mit konfigurierbarer Frequenz'
    },
'ptc': {
    'en': 'Reads temperatures from Pt100/1000 sensors',
    'de': 'Liest Temperaturen von Pt100/1000-Sensoren'
    },
'remote_switch': {
    'en': 'Controls remote mains switches',
    'de': 'Steuert Funksteckdosen'
    },
'rotary_encoder': {
    'en': '360° rotary encoder with push-button',
    'de': '360° Drehgeber / Drehencoder mit Taster'
    },
'rotary_poti': {
    'en': '300° rotary potentiometer',
    'de': '300° Dreh-Potentiometer'
    },
'rs232': {
    'en': 'FIXME',
    'de': 'FIXME'
    },
'segment_display_4x7': {
    'en': 'Four 7-segment displays with switchable colon',
    'de': 'Vier 7-Segment Anzeigen mit schaltbarem Doppelpunkt'
    },
'solid_state_relay': {
    'en': 'Controls AC and DC Solid State Relays',
    'de': 'Schaltet AC und DC Halbleiterrelais (Solid State Relais)'
    },
'sound_intensity': {
    'en': 'Measures sound intensity',
    'de': 'Misst Schallintensität'
    },
'temperature': {
    'en': 'Measures ambient temperature with 0.5°C accuracy',
    'de': 'Misst Umgebungstemperatur mit 0,5°C Genauigkeit'
    },
'temperature_ir': {
    'en': 'Measures contactless object temperature from -70°C to 380°C',
    'de': 'Kontaktlose Objekttemperaturmessung von -70°C bis 380°C'
    },
'tilt': {
    'en': 'Detects inclination of Bricklet (tilt switch open/closed)',
    'de': 'Erkennt Neigung des Bricklets (Neigungsschalter offen/geschlossen)'
    },
'voltage': {
    'en': 'Measures voltages up to 50V (DC)',
    'de': 'Misst Spannungen bis zu 50V (DC)'
    },
'voltage_current': {
    'en': 'Measure power, voltage and current up to 720W/36V/20A',
    'de': 'Misst Leistung, Spannung und Strom bis zu 720W/36V/20A'
    },
}

class Bricklet(Product):
    def __init__(self, *args, **kwargs):
        Product.__init__(self, *args, **kwargs)

    @property
    def description(self):
        return bricklet_descriptions[self.url_part][lang]

bricklets = [Bricklet('Accelerometer',             'accelerometer',             bindings, False),
             Bricklet('Ambient Light',             'ambient_light',             bindings, True),
             Bricklet('Analog In',                 'analog_in',                 bindings, True),
             Bricklet('Analog In 2.0',             'analog_in_v2',              bindings, False),
             Bricklet('Analog Out',                'analog_out',                bindings, True),
             Bricklet('Analog Out 2.0',            'analog_out_v2',             bindings, False),
             Bricklet('Barometer',                 'barometer',                 bindings, True),
             Bricklet('Breakout',                  'breakout',                  [],       True),
             Bricklet('Color',                     'color',                     bindings, True),
             Bricklet('Current12',                 'current12',                 bindings, True),
             Bricklet('Current25',                 'current25',                 bindings, True),
             Bricklet('Distance IR',               'distance_ir',               bindings, True),
             Bricklet('Distance US',               'distance_us',               bindings, True),
             Bricklet('Dual Button',               'dual_button',               bindings, True),
             Bricklet('Dual Relay',                'dual_relay',                bindings, True),
             Bricklet('Gas Detector',              'gas_detector',              bindings, False),
             Bricklet('GPS',                       'gps',                       bindings, True),
             Bricklet('Hall Effect',               'hall_effect',               bindings, True),
             Bricklet('Heart Rate',                'heart_rate',                bindings, False),
             Bricklet('Humidity',                  'humidity',                  bindings, True),
             Bricklet('Industrial Digital In 4',   'industrial_digital_in_4',   bindings, True),
             Bricklet('Industrial Digital Out 4',  'industrial_digital_out_4',  bindings, True),
             Bricklet('Industrial Dual 0-20mA',    'industrial_dual_0_20ma',    bindings, True),
             Bricklet('Industrial Dual Analog In', 'industrial_dual_analog_in', bindings, False),
             Bricklet('Industrial Quad Relay',     'industrial_quad_relay',     bindings, True),
             Bricklet('IO-16',                     'io16',                      bindings, True),
             Bricklet('IO-4',                      'io4',                       bindings, True),
             Bricklet('Joystick',                  'joystick',                  bindings, True),
             Bricklet('Laser Range Finder',        'laser_range_finder',        bindings, False),
             Bricklet('LCD 16x2',                  'lcd_16x2',                  bindings, True),
             Bricklet('LCD 20x4',                  'lcd_20x4',                  bindings, True),
             Bricklet('LED Strip',                 'led_strip',                 bindings, True),
             Bricklet('Line',                      'line',                      bindings, True),
             Bricklet('Linear Poti',               'linear_poti',               bindings, True),
             Bricklet('Load Cell',                 'load_cell',                 bindings, False),
             Bricklet('Moisture',                  'moisture',                  bindings, True),
             Bricklet('Motion Detector',           'motion_detector',           bindings, True),
             Bricklet('Multi Touch',               'multi_touch',               bindings, True),
             Bricklet('NFC/RFID',                  'nfc_rfid',                  bindings, True),
             Bricklet('Piezo Buzzer',              'piezo_buzzer',              bindings, True),
             Bricklet('Piezo Speaker',             'piezo_speaker',             bindings, True),
             Bricklet('PTC',                       'ptc',                       bindings, True),
             Bricklet('Remote Switch',             'remote_switch',             bindings, True),
             Bricklet('Rotary Encoder',            'rotary_encoder',            bindings, True),
             Bricklet('Rotary Poti',               'rotary_poti',               bindings, True),
             Bricklet('RS232',                     'rs232',                     bindings, False),
             Bricklet('Segment Display 4x7',       'segment_display_4x7',       bindings, True),
             Bricklet('Solid State Relay',         'solid_state_relay',         bindings, True),
             Bricklet('Sound Intensity',           'sound_intensity',           bindings, True),
             Bricklet('Temperature',               'temperature',               bindings, True),
             Bricklet('Temperature IR',            'temperature_ir',            bindings, True),
             Bricklet('Tilt',                      'tilt',                      bindings, True),
             Bricklet('Voltage',                   'voltage',                   bindings, True),
             Bricklet('Voltage/Current',           'voltage_current',           bindings, True)]


extension_descriptions = {
'chibi': {
    'en': 'Wireless Chibi Master Extension',
    'de': 'Drahtlose Chibi Master Extension'
    },
'ethernet': {
    'en': 'Cable based Ethernet Master Extension',
    'de': 'Kabelgebundene Ethernet Master Extension'
    },
'rs485': {
    'en': 'Cable based RS485 Master Extension',
    'de': 'Kabelgebundene RS485 Master Extension'
    },
'wifi': {
    'en': 'Wireless WIFI Master Extension',
    'de': 'Drahtlose WIFI Master Extension'
    }
}

class Extension(Product):
    def __init__(self, display_name, url_part, is_published):
        Product.__init__(self, display_name, url_part, [], is_published)

    @property
    def description(self):
        return extension_descriptions[self.url_part][lang]

extensions = [Extension('Chibi Extension',    'chibi',    True),
              Extension('Ethernet Extension', 'ethernet', True),
              Extension('RS485 Extension',    'rs485',    True),
              Extension('WIFI Extension',     'wifi',     True)]


power_supply_descriptions = {
'step_down': {
    'en': 'Powers a stack of Bricks with 5V',
    'de': 'Versorgt einen Stapel von Bricks mit 5V'
    }
}

class PowerSupply(Product):
    def __init__(self, display_name, url_part, is_published):
        Product.__init__(self, display_name, url_part, [], is_published)

    @property
    def description(self):
        return power_supply_descriptions[self.url_part][lang]

power_supplies = [PowerSupply('Step-Down Power Supply', 'step_down', True)]


accessory_descriptions = {
'dc_jack_adapter': {
    'en': 'Adapter between a 5mm DC jack and 2 Pole Black Connector',
    'de': 'Adapter zwischen einem 5mm DC Stecker und 2 Pin Stecker Schwarz'
    }
}

class Accessory(Product):
    def __init__(self, display_name, url_part, is_published):
        Product.__init__(self, display_name, url_part, [], is_published)

    @property
    def description(self):
        return accessory_descriptions[self.url_part][lang]

accessories = [Accessory('DC Jack Adapter', 'dc_jack_adapter', True)]


index_table_head = {
'en':
""".. csv-table::
 :header: "", "API"
 :delim: |
 :widths: 11, 44

{0}
 |
 **Bricks** |
{1}
 |
 **Bricklets** |
{2}
 |
 **Master Extensions** |
{3}
 |
 **Power Supplies** |
{4}
 |
 **Accessories** |
{5}
""",
'de':
""".. csv-table::
 :header: "", "API"
 :delim: |
 :widths: 11, 44

{0}
 |
 **Bricks** |
{1}
 |
 **Bricklets** |
{2}
 |
 **Master Extensions** |
{3}
 |
 **Stromversorgungen** |
{4}
 |
 **Zubehör** |
{5}
"""
}

primer_table_head = {
'en':
"""
.. csv-table::
   :header: "Name", "Description"
   :widths: 30, 70

""",
'de':
"""
.. csv-table::
   :header: "Name", "Beschreibung"
   :widths: 30, 70

"""
}

download_tools_source_code = {
'en': 'Source Code',
'de': 'Quelltext'
}

download_tools_archive = {
'en': 'Archive',
'de': 'Archiv'
}

download_tools_table_head = {
'en':
""".. csv-table::
 :header: "Tool", "Downloads", "Version", "Archive", "Changelog"
 :delim: |
 :widths: 17, 32, 5, 5, 8

""",
'de':
""".. csv-table::
 :header: "Tool", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 17, 32, 5, 5, 8

"""
}

download_bindings_bindings_and_examples = {
'en': 'Bindings and Examples',
'de': 'Bindings und Beispiele'
}

download_bindings_archive = {
'en': 'Archive',
'de': 'Archiv'
}

download_bindings_table_head = {
'en':
""".. csv-table::
 :header: "Language", "Downloads", "Version", "Archive", "Changelog"
 :delim: |
 :widths: 17, 32, 5, 5, 8

""",
'de':
""".. csv-table::
 :header: "Sprache", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 17, 32, 5, 5, 8

"""
}

download_firmwares_source_code = {
'en': 'Source Code',
'de': 'Quelltext'
}

download_firmwares_archive = {
'en': 'Archive',
'de': 'Archiv'
}

download_firmwares_table_head = {
'en':
""".. csv-table::
 :header: "", "Downloads", "Version", "Archive", "Changelog"
 :delim: |
 :widths: 17, 32, 5, 5, 8

 **Bricks** | |
{0}
 | |
 **Bricklets** | |
 {1}""",
'de':
""".. csv-table::
 :header: "", "Downloads", "Version", "Archiv", "Changelog"
 :delim: |
 :widths: 17, 32, 5, 5, 8

 **Bricks** | |
{0}
 | |
 **Bricklets** | |
{1}"""
}

source_code_gits_table_head = {
'en':
""".. csv-table::
 :header: "", "Repository", "Bug Tracking"
 :delim: |
 :widths: 20, 23, 12

 **Tools** | |
 Brick Daemon | `brickd.git <https://github.com/Tinkerforge/brickd/>`__ | `Report Bug <https://github.com/Tinkerforge/brickd/issues>`__
 Brick Viewer | `brickv.git <https://github.com/Tinkerforge/brickv/>`__ | `Report Bug <https://github.com/Tinkerforge/brickv/issues>`__
 Brick Bootloader | `brickboot.git <https://github.com/Tinkerforge/brickboot/>`__ | `Report Bug <https://github.com/Tinkerforge/brickboot/issues>`__
 Brick Library | `bricklib.git <https://github.com/Tinkerforge/bricklib/>`__ | `Report Bug <https://github.com/Tinkerforge/bricklib/issues>`__
 Bricklet Library | `brickletlib.git <https://github.com/Tinkerforge/brickletlib/>`__ | `Report Bug <https://github.com/Tinkerforge/brickletlib/issues>`__
 API Generator | `generators.git <https://github.com/Tinkerforge/generators/>`__ | `Report Bug <https://github.com/Tinkerforge/generators/issues>`__
 KiCad Libraries | `kicad-libraries.git <https://github.com/Tinkerforge/kicad-libraries/>`__ | `Report Bug <https://github.com/Tinkerforge/kicad-libraries/issues>`__
 | |
 **Bricks** | |
{0}
 | |
 **Bricklets** | |
{1}
 | |
 **Master Extensions** | |
{2}
 | |
 **Power Supplies** | |
 Step-Down Power Supply | `step-down-powersupply.git <https://github.com/Tinkerforge/step-down-powersupply/>`__ | `Report Bug <https://github.com/Tinkerforge/step-down-powersupply/issues>`__
 | |
 **Accessories** | |
 DC Jack Adapter | `dc-adapter.git <https://github.com/Tinkerforge/dc-adapter/>`__ | `Report Bug <https://github.com/Tinkerforge/dc-adapter/issues>`__
""",
'de':
 """.. csv-table::
 :header: "", "Repository", "Bug Tracking"
 :delim: |
 :widths: 20, 23, 12

 **Tools** | |
 Brick Daemon | `brickd.git <https://github.com/Tinkerforge/brickd/>`__ | `Problem melden <https://github.com/Tinkerforge/brickd/issues>`__
 Brick Viewer | `brickv.git <https://github.com/Tinkerforge/brickv/>`__ | `Problem melden <https://github.com/Tinkerforge/brickv/issues>`__
 Brick Bootloader | `brickboot.git <https://github.com/Tinkerforge/brickboot/>`__ | `Problem melden <https://github.com/Tinkerforge/brickboot/issues>`__
 Brick Library | `bricklib.git <https://github.com/Tinkerforge/bricklib/>`__ | `Problem melden <https://github.com/Tinkerforge/bricklib/issues>`__
 Bricklet Library | `brickletlib.git <https://github.com/Tinkerforge/brickletlib/>`__ | `Problem melden <https://github.com/Tinkerforge/brickletlib/issues>`__
 API Generator | `generators.git <https://github.com/Tinkerforge/generators/>`__ | `Problem melden <https://github.com/Tinkerforge/generators/issues>`__
 KiCad Libraries | `kicad-libraries.git <https://github.com/Tinkerforge/kicad-libraries/>`__ | `Problem melden <https://github.com/Tinkerforge/kicad-libraries/issues>`__
 | |
 **Bricks** | |
{0}
 | |
 **Bricklets** | |
{1}
 | |
 **Master Extensions** | |
{2}
 | |
 **Stromversorgungen** | |
 Step-Down Power Supply | `step-down-powersupply.git <https://github.com/Tinkerforge/step-down-powersupply/>`__ | `Problem melden <https://github.com/Tinkerforge/step-down-powersupply/issues>`__
 | |
 **Zubehör** | |
 DC Jack Adapter | `dc-adapter.git <https://github.com/Tinkerforge/dc-adapter/>`__ | `Problem melden <https://github.com/Tinkerforge/dc-adapter/issues>`__
"""
}

source_code_gits_brick_row_cell = {
'en': ' {0} | `{1}-brick.git <https://github.com/Tinkerforge/{1}-brick/>`__ | `Report Bug <https://github.com/Tinkerforge/{1}-brick/issues>`__',
'de': ' {0} | `{1}-brick.git <https://github.com/Tinkerforge/{1}-brick/>`__ | `Problem melden <https://github.com/Tinkerforge/{1}-brick/issues>`__'
}

source_code_gits_bricklet_row_cell = {
'en': ' {0} | `{1}-bricklet.git <https://github.com/Tinkerforge/{1}-bricklet/>`__ | `Report Bug <https://github.com/Tinkerforge/{1}-bricklet/issues>`__',
'de': ' {0} | `{1}-bricklet.git <https://github.com/Tinkerforge/{1}-bricklet/>`__ | `Problem melden <https://github.com/Tinkerforge/{1}-bricklet/issues>`__',
}

source_code_gits_extension_row_cell = {
'en': ' {0} | `{1}-extension.git <https://github.com/Tinkerforge/{1}-extension/>`__ | `Report Bug <https://github.com/Tinkerforge/{1}-extension/issues>`__',
'de': ' {0} | `{1}-extension.git <https://github.com/Tinkerforge/{1}-extension/>`__ | `Problem melden <https://github.com/Tinkerforge/{1}-extension/issues>`__',
}

api_bindings_links_table_head = {
'en':
""".. csv-table::
 :header: "", "API", "Examples"
 :delim: |
 :widths: 20, 10, 10

{0}
 | |
 **Bricks** | |
{1}
 | |
 **Bricklets** | |
{2}
""",
'de':
""".. csv-table::
 :header: "", "API", "Beispiele"
 :delim: |
 :widths: 20, 10, 10

{0}
 | |
 **Bricks** | |
{1}
 | |
 **Bricklets** | |
{2}
"""
}

api_bindings_links_ipcon_row = {
'en': ' :ref:`IP Connection <api_bindings_ip_connection>` | :ref:`API <ipcon_{0}>` | :ref:`Examples <ipcon_{0}_examples>`',
'de': ' :ref:`IP Connection <api_bindings_ip_connection>` | :ref:`API <ipcon_{0}>` | :ref:`Beispiele <ipcon_{0}_examples>`'
}

api_bindings_links_brick_row = {
'en': ' :ref:`{2} <{0}_brick>` | :ref:`API <{0}_brick_{1}_api>` | :ref:`Examples <{0}_brick_{1}_examples>`',
'de': ' :ref:`{2} <{0}_brick>` | :ref:`API <{0}_brick_{1}_api>` | :ref:`Beispiele <{0}_brick_{1}_examples>`'
}

api_bindings_links_bricklet_row = {
'en': ' :ref:`{2} <{0}_bricklet>` | :ref:`API <{0}_bricklet_{1}_api>` | :ref:`Examples <{0}_bricklet_{1}_examples>`',
'de': ' :ref:`{2} <{0}_bricklet>` | :ref:`API <{0}_bricklet_{1}_api>` | :ref:`Beispiele <{0}_bricklet_{1}_examples>`'
}

LATEST_VERSIONS_URL = 'http://download.tinkerforge.com/latest_versions.txt'

tool_versions = {}
bindings_versions = {}
firmware_versions = {}
plugin_versions = {}

def get_latest_version_info():
    print 'Discovering latest versions on tinkerforge.com'

    try:
        response = urllib2.urlopen(LATEST_VERSIONS_URL)
        latest_versions_data = response.read()
    except urllib2.URLError:
        raise Exception('Latest version information on tinkerforge.com is not available (error code 1)')

    for line in latest_versions_data.split('\n'):
        line = line.strip()

        if len(line) < 1:
            continue

        parts = line.split(':')

        if len(parts) != 3:
            raise Exception('Latest version information on tinkerforge.com is malformed (error code 2)')

        latest_version_parts = parts[2].split('.')

        if len(latest_version_parts) != 3:
            raise Exception('Latest version information on tinkerforge.com is malformed (error code 3)')

        try:
            latest_version = int(latest_version_parts[0]), int(latest_version_parts[1]), int(latest_version_parts[2])
        except:
            raise Exception('Latest version information on tinkerforge.com is malformed (error code 4)')

        if parts[0] == 'tools':
            tool_versions[parts[1]] = latest_version
        elif parts[0] == 'bindings':
            bindings_versions[parts[1]] = latest_version
        elif parts[0] == 'bricks':
            firmware_versions[parts[1]] = latest_version
        elif parts[0] == 'bricklets':
            plugin_versions[parts[1]] = latest_version

def make_primer_table(devices, category, add_category_to_name=True):
    table_head = primer_table_head[lang]

    if add_category_to_name:
        row_head = '   ":ref:`{0} <{1}_' + category + '>`", "{2}"'
        row_cell = '":ref:`{0} <{1}_' + category + '_{2}>`"'
    else:
        row_head = '   ":ref:`{0} <{1}>`", "{2}"'
        row_cell = '":ref:`{0} <{1}_{2}>`"'

    rows = []

    for device in devices:
        if device.is_published:
            rows.append(row_head.format(device.display_name, device.url_part, device.description))

    return table_head + '\n'.join(rows) + '\n'

def make_download_tools_table():
    source_code = download_tools_source_code[lang]
    archive = download_tools_archive[lang]
    table_head = download_tools_table_head[lang]
    row_multi_cell = ' :ref:`{0} <{1}>` | Linux (`amd64 <http://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}_amd64.deb>`__, `i386 <http://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}_i386.deb>`__, `armhf <http://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}_armhf.deb>`__), `Mac OS X <http://download.tinkerforge.com/tools/{1}/macos/{1}_macos_{4}_{5}_{6}.dmg>`__, `Windows <http://download.tinkerforge.com/tools/{1}/windows/{1}_windows_{4}_{5}_{6}.exe>`__, `{2} <https://github.com/Tinkerforge/{1}/archive/v{4}.{5}.{6}.zip>`__ | {4}.{5}.{6} | `{3} <http://download.tinkerforge.com/tools/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{1}/master/changelog>`__'
    row_all_cell = ' :ref:`{0} <{1}>` | `Linux <http://download.tinkerforge.com/tools/{1}/linux/{1}-{4}.{5}.{6}_all.deb>`__, `Mac OS X <http://download.tinkerforge.com/tools/{1}/macos/{1}_macos_{4}_{5}_{6}.dmg>`__, `Windows <http://download.tinkerforge.com/tools/{1}/windows/{1}_windows_{4}_{5}_{6}.exe>`__, `{2} <https://github.com/Tinkerforge/{1}/archive/v{4}.{5}.{6}.zip>`__ | {4}.{5}.{6} | `{3} <http://download.tinkerforge.com/tools/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{1}/master/changelog>`__'
    rows = []

    for tool in tools:
        if tool.url_part == 'brickd':
            row_cell = row_multi_cell
        else:
            row_cell = row_all_cell

        rows.append(row_cell.format(tool.display_name, tool.url_part, source_code, archive, *tool_versions[tool.url_part]))

    return table_head + '\n'.join(rows) + '\n'

def make_download_bindings_table():
    bindings_and_examples = download_bindings_bindings_and_examples[lang]
    archive = download_bindings_archive[lang]
    table_head = download_bindings_table_head[lang]
    row_cell = ' `{0} <http://www.tinkerforge.com/' + lang + '/doc/Software/API_Bindings_{2}.html>`__ | `{4} <http://download.tinkerforge.com/bindings/{1}/tinkerforge_{1}_bindings_{5}_{6}_{7}.zip>`__ | {5}.{6}.{7} | `{3} <http://download.tinkerforge.com/bindings/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/generators/master/{1}/changelog.txt>`__'
    rows = []

    for binding in bindings:
        if not binding.is_programming_language or not binding.is_published:
            continue

        rows.append(row_cell.format(binding.display_name, binding.url_part, binding.url_part_for_doc, archive, bindings_and_examples, *bindings_versions[binding.url_part]))

    return table_head + '\n'.join(rows) + '\n'

def make_download_firmwares_table():
    archive = download_firmwares_archive[lang]
    source_code = download_firmwares_source_code[lang]
    table_head = download_firmwares_table_head[lang]
    brick_row_cell = ' :ref:`{0} <{1}_brick>` | `Firmware <http://download.tinkerforge.com/firmwares/bricks/{1}/brick_{1}_firmware_{5}_{6}_{7}.bin>`__, `{3} <https://github.com/Tinkerforge/{2}-brick/archive/v{5}.{6}.{7}.zip>`__ | {5}.{6}.{7} | `{4} <http://download.tinkerforge.com/firmwares/bricks/{1}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{2}-brick/master/software/changelog>`__'
    bricklet_row_cell = ' :ref:`{0} <{1}_bricklet>` | `Plugin <http://download.tinkerforge.com/firmwares/bricklets/{3}/bricklet_{3}_firmware_{6}_{7}_{8}.bin>`__, `{4} <https://github.com/Tinkerforge/{2}-bricklet/archive/v{6}.{7}.{8}.zip>`__ | {6}.{7}.{8} | `{5} <http://download.tinkerforge.com/firmwares/bricklets/{3}/>`__ | `Changelog <https://raw.githubusercontent.com/Tinkerforge/{2}-bricklet/master/software/changelog>`__'
    brick_rows = []
    bricklet_rows = []

    for brick in bricks:
        if len(brick.bindings) > 0 and brick.is_published and brick.has_firmware:
            brick_rows.append(brick_row_cell.format(brick.display_name, brick.url_part, brick.url_part_for_git, source_code, archive, *firmware_versions[brick.url_part]))

    def handle_bricklet(name, common_url_part, plugin_url_part):
        bricklet_rows.append(bricklet_row_cell.format(name, common_url_part, common_url_part.replace('_', '-').replace('/', '-'), plugin_url_part, source_code, archive, *plugin_versions[plugin_url_part]))

    for bricklet in bricklets:
        if len(bricklet.bindings) > 0 and bricklet.is_published and bricklet.has_firmware:
            if bricklet.url_part == 'lcd_20x4':
                handle_bricklet(bricklet.display_name + ' 1.1', bricklet.url_part, bricklet.url_part + '_v11')
                handle_bricklet(bricklet.display_name + ' 1.2', bricklet.url_part, bricklet.url_part + '_v12')
            else:
                handle_bricklet(bricklet.display_name, bricklet.url_part, bricklet.url_part)

    return table_head.format('\n'.join(brick_rows), '\n'.join(bricklet_rows)) + '\n'

def make_api_bindings_bindings_table():
    row = '* :ref:`{0} <ipcon_{1}>`'
    rows = []

    for binding in bindings:
        if binding.is_programming_language and binding.is_published:
            rows.append(row.format(binding.display_name, binding.url_part))

    return '\n'.join(rows) + '\n'

def make_api_bindings_links_table(binding):
    ipcon_line = api_bindings_links_ipcon_row[lang].format(binding.url_part)

    brick_lines = []
    for brick in bricks:
        if brick.is_published and len(brick.bindings) > 0: # published and has bindings
            brick_lines.append(api_bindings_links_brick_row[lang].format(brick.url_part, binding.url_part, brick.display_name))

    bricklet_lines = []
    for bricklet in bricklets:
        if bricklet.is_published and len(bricklet.bindings) > 0: # published and has bindings
            bricklet_lines.append(api_bindings_links_bricklet_row[lang].format(bricklet.url_part, binding.url_part, bricklet.display_name))

    return api_bindings_links_table_head[lang].format(ipcon_line,
                                                      '\n'.join(brick_lines),
                                                      '\n'.join(bricklet_lines))

def make_source_code_gits_table():
    table_head = source_code_gits_table_head[lang]
    brick_row_cell = source_code_gits_brick_row_cell[lang]
    bricklet_row_cell = source_code_gits_bricklet_row_cell[lang]
    extension_row_cell = source_code_gits_extension_row_cell[lang]
    brick_rows = []
    bricklet_rows = []
    extension_rows = []

    for brick in bricks:
        if brick.is_published:
            brick_rows.append(brick_row_cell.format(brick.display_name, brick.url_part_for_git))

    for bricklet in bricklets:
        if bricklet.is_published:
            bricklet_rows.append(bricklet_row_cell.format(bricklet.display_name, bricklet.url_part_for_git))

    for extension in extensions:
        if extension.is_published:
            extension_rows.append(extension_row_cell.format(extension.display_name, extension.url_part_for_git))

    return table_head.format('\n'.join(brick_rows), '\n'.join(bricklet_rows), '\n'.join(extension_rows)) + '\n'

def make_index_table_block(devices, category, add_category_to_name=True):
    if add_category_to_name:
        row_head = ' :ref:`{0} <{1}_' + category + '>` | '
        row_cell = ' :ref:`{0} <{1}_' + category + '_{2}>`'
    else:
        row_head = ' :ref:`{0} <{1}>` | '
        row_cell = ' :ref:`{0} <{1}_{2}>`'

    rows = []

    for device in devices:
        if not device.is_published:
            continue

        cells = []

        for binding in device.bindings:
            if binding.is_published:
                cells.append(row_cell.format(binding.short_display_name, device.url_part, binding.url_part))

        row = row_head.format(device.display_name, device.url_part) + ', '.join(cells)
        rows.append(row)

    return '\n'.join(rows)

def make_index_table():
    ipcon_head = ' :ref:`IP Connection <api_bindings_ip_connection>` | '
    ipcon_cell = ':ref:`{0} <ipcon_{1}>`'
    ipcon_cell_llproto = ':ref:`{0} <llproto_{1}>`'
    ipcon_cells = []

    for binding in bindings:
        if not binding.is_published:
            continue

        if binding.is_programming_language:
            ipcon_cells.append(ipcon_cell.format(binding.short_display_name, binding.url_part))
        else:
            ipcon_cells.append(ipcon_cell_llproto.format(binding.short_display_name, binding.url_part))

    return index_table_head[lang].format(ipcon_head + ', '.join(ipcon_cells),
                                         make_index_table_block(bricks, 'brick'),
                                         make_index_table_block(bricklets, 'bricklet'),
                                         make_index_table_block(extensions, 'extension'),
                                         make_index_table_block(power_supplies, 'power_supply'),
                                         make_index_table_block(accessories, 'accessory', False))



def make_index_hardware_device(devices, category_url, use_category_content=True, use_category_in_name=True):
    hardware_li = """<li><a class="reference internal" href="Hardware/{1}s/{2}{3}.html">{0}</a></li>"""
    lis = []

    for device in devices:
        if not device.is_published:
            continue

        category_name = ''
        if use_category_in_name:
            category_name = '_' + category_url
        lis.append(hardware_li.format(device.display_name, category_url, device.url_part_for_hardware_doc, category_name))

    if category_name == '_Bricklet':
        split = int(len(lis) / 3 + 0.5)
    else:
        split = 15

    ret = ''
    while len(lis) > 0:
        li_part = lis[:split]
        lis = lis[split:]
        if use_category_content:
            ret += '\n<div class="category_content_inner">\n<ul>' +'\n'.join(li_part) + '</ul>\n</div>'
        else:
            ret += '\n<ul>' +'\n'.join(li_part) + '</ul>\n'

    return ret


def make_index_hardware():
    index_html = {'en': """
<div class="category_hardware_outer">
    <div class="category_body">
        <div class="category_content">
            <h3>Bricks</h3>
            {0}
        </div>
        <div class="category_content">
            <h3>Bricklets</h3>
            {1}
        </div>
        <div class="category_content">
            <h3>Master Extensions</h3>
            {2}
            <h3>Power Supplies</h3>
            {3}
            <h3>Accesories</h3>
            {4}
        </div>
    </div>
</div>
<div style="clear: both;"></div>
"""}
    index_html['de'] = index_html['en'].replace('Power Supplies', 'Stromversorgungen').replace('Accesories', 'Zubehör')

    return index_html[lang].format(make_index_hardware_device(bricks, 'Brick'),
                                   make_index_hardware_device(bricklets, 'Bricklet', use_category_in_name=False),
                                   make_index_hardware_device(extensions, 'Master_Extension', False, False),
                                   make_index_hardware_device(power_supplies, 'Power_Supplie', False, False),
                                   make_index_hardware_device(accessories, 'Accessorie', False, False))


def make_index_api_device(devices, category_url, language, use_category_content=True, use_category_in_name=True):
    software_li = """<li><a class="reference internal" href="Software/{1}s/{2}{3}_{4}.html">{0}</a></li>"""
    lis = []

    for device in devices:
        if not device.is_published:
            continue

        if device.bindings == []:
            continue

        category_name = ''
        if use_category_in_name:
            category_name = '_' + category_url
        lis.append(software_li.format(device.display_name, category_url, device.url_part_for_software_doc, category_name, language))

    ret = ''
    while lis != []:
        li_part = lis[:11]
        lis = lis[11:]
        if use_category_content:
            ret += '\n<div class="category_content_inner">\n<ul>' +'\n'.join(li_part) + '</ul>\n</div>'
        else:
            ret += '\n<ul>' +'\n'.join(li_part) + '</ul>\n'

    return ret

def make_index_api_misc(binding, lang):
    misc_html = {'en': """
<ul>
    <li><a class="reference internal" href="Software/IPConnection_{0}.html">IP Connection</a></li>
    <li><a class="reference internal" href="Software/API_Bindings_{0}.html">Usage</a></li>
    {1}
</ul>
"""}
    misc_html['de'] = misc_html['en'].replace('Usage', 'Benutzung')

    llp_html = {'en': """
<ul>
    <li><a class="reference internal" href="Low_Level_Protocols/{0}.html">Specification</a></li>
</ul>
"""}
    llp_html['de'] = llp_html['en'].replace('Specification', 'Spezifikation')


    add = ''

    additional_li = {'en': '<li><a class="reference internal" href="Software/API_Bindings_{0}_{1}.html">Usage ({2})</a></li>'}
    additional_li['de'] = additional_li['en'].replace('Usage', 'Benutzung')

    language = binding.url_part_for_doc
    if not binding.is_programming_language:
        return llp_html[lang].format(language)
    else:
        if language == 'C':
            add = additional_li[lang].format(language, 'iOS', 'iOS')
        elif language == 'CSharp':
            add = additional_li[lang].format(language, 'Windows_Phone', 'Windows Phone')
        elif language == 'Java':
            add = additional_li[lang].format(language, 'Android', 'Android')

        return misc_html[lang].format(language, add)

    return ''

def make_index_api():
    index_html = {'en': """
<div class="category_api">
    <div class="category_head btn-more btn-more-down">
        <a name="software-{4}"></a>
        {3}
    </div>
    <div class="category_body" {5}>
        <div class="category_content">
            <h3>Bricks</h3>
            {0}
            <h3>Misc</h3>
            {1}
        </div>
        <div class="category_content">
            <h3>Bricklets</h3>
            {2}
        </div>
    </div>
</div>
<div style="clear: both;"></div>
"""}
    index_html['de'] = index_html['en']

    script_html = """
<script type="text/javascript">
    var togglingContent = false;

    $(document).ready(function () {
        $(".category_head").click(function() {
            toggleContent($(this).parent(), 100);
        });

        updateContent(0);
    });

    $(window).on("hashchange", function () {
        if (!togglingContent) {
            updateContent(100);
        }
    });

    function updateContent(duration) {
        anchorName = location.hash.replace(/^[^#]*#/, '').replace(/^#+|#+$/, '').replace(/^\/*/, '').replace(/-open$/, '')

        if (anchorName.length > 0 && anchorName.substring(0, 9) === "software-" && anchorName !== "software-none") {
            a = $("a[name="+anchorName+"]")

            if (a.length > 0) {
                toggleContent(a.parent().parent(), duration, true);
                return;
            }
        }

        $(".btn-more").parent().find(".category_body").slideUp(duration);
        $(".btn-more").removeClass("btn-more-up").addClass("btn-more-down");
    }

    function toggleContent(parent, duration, forceShow) {
        togglingContent = true;

        categoryBody = parent.find(".category_body")
        btnMore = parent.find(".btn-more")

        if (categoryBody.is(":hidden") || forceShow === true) {
            anchorName = categoryBody.parent().find(".category_head a").attr("name")

            // only set hash, if it doesn't point to the current category already
            if (location.hash.indexOf(anchorName) < 0) {
                location.hash = "/" + anchorName + "-open";
            }

            $(".btn-more").parent().find(".category_body").slideUp(duration);
            $(".btn-more").removeClass("btn-more-up").addClass("btn-more-down");

            btnMore.removeClass("btn-more-down").addClass("btn-more-up");

            // this has to be the last line and after the hash change
            categoryBody.slideDown(duration, function() { togglingContent = false });
        }
        else {
            btnMore.removeClass("btn-more-up").addClass("btn-more-down");

            if (/software-/.test(location.hash)) {
                location.hash = "/software-none-open";
            }

            // this has to be the last line and after the hash change
            categoryBody.slideUp(duration, function() { togglingContent = false });
        }
    }
</script>
"""

    html = '<div class="category_api_outer">'
    first = True

    for binding in bindings:
        if binding.is_published:
            if first:
                style = ''
            else:
                style = ' style="display: none;"'

            first = False

            html += index_html[lang].format(make_index_api_device(bricks, 'Brick', binding.url_part_for_doc, False),
                                            make_index_api_misc(binding, lang),
                                            make_index_api_device(bricklets, 'Bricklet', binding.url_part_for_doc),
                                            binding.display_name,
                                            binding.url_part,
                                            style)

    html += '</div>'

    return html + script_html

hlpi_table_head = {
'en':
"""
.. csv-table::
   :header: "Language", "API", "Examples", "Installation"
   :widths: 25, 10, 10, 10

""",
'de':
"""
.. csv-table::
   :header: "Sprache", "API", "Beispiele", "Installation"
   :widths: 25, 10, 10, 10

"""
}

hlpi_row_source = {
'en': '   "{0}", ":ref:`API <{1}_{2}_{3}_api>`", ":ref:`Examples <{1}_{2}_{3}_examples>`", ":ref:`Installation <api_bindings_{3}>`"',
'de': '   "{0}", ":ref:`API <{1}_{2}_{3}_api>`", ":ref:`Beispiele <{1}_{2}_{3}_examples>`", ":ref:`Installation <api_bindings_{3}>`"'
}

hlpi_row = {
'en': '   "{0}", ":ref:`API <{1}_{2}_{3}_api>`"',
'de': '   "{0}", ":ref:`API <{1}_{2}_{3}_api>`"'
}

def make_hlpi_table(device, category):
    table_head = hlpi_table_head[lang]
    row_source = hlpi_row_source[lang]
    row = hlpi_row[lang]
    rows = []

    for binding in device.bindings:
        if not binding.is_published:
            continue

        if binding.is_programming_language:
            rows.append(row_source.format(binding.display_name, device.url_part, category, binding.url_part))
        else:
            rows.append(row.format(binding.display_name, device.url_part, category, binding.url_part))

    return table_head + '\n'.join(rows) + '\n'

device_identifier_table_head = {
'en':
"""
.. csv-table::
   :header: "Device Identifier", "Device Name"
   :widths: 30, 100

""",
'de':
"""
.. csv-table::
   :header: "Device Identifier", "Device Name"
   :widths: 30, 100

"""
}

device_identifier_row = {
'en': '   "{0}", "{1}"',
'de': '   "{0}", "{1}"'
}

def make_device_identifier_table():
    table_head = device_identifier_table_head[lang]
    row = device_identifier_row[lang]
    rows = []

    for device_identifier in device_identifiers:
        rows.append(row.format(device_identifier[0], device_identifier[1]))

    return table_head + '\n'.join(rows) + '\n'

def make_authentication_tutorial_examples_table():
    row = '* :ref:`{0} <ipcon_{1}_examples>`'
    rows = []

    for binding in bindings:
        if binding.is_programming_language and binding.is_published:
            rows.append(row.format(binding.display_name, binding.url_part))

    return '\n'.join(rows) + '\n'

def make_devices_toctree(devices, category):
    prefix = """
.. toctree::
   :hidden:

"""
    line = '   Software/{0}s/{1}_{0}_{2}'
    lines = []

    for binding in bindings:
        if binding.is_published:
            for device in devices:
                if len(device.bindings) > 0:
                    lines.append(line.format(category, device.url_part_for_software_doc, binding.url_part_for_doc))

    return prefix + '\n'.join(lines) + '\n'

def write_if_changed(path, content):
    if os.path.exists(path):
        f = open(path, 'rb')
        existing = f.read()
        f.close()
        if existing == content:
            return

    f = open(path, 'wb')
    f.write(content)
    f.close()

def generate(path):
    global lang

    if path.endswith('/en'):
        lang = 'en'
    elif path.endswith('/de'):
        lang = 'de'
    else:
        print('Wrong working directory')
        sys.exit(1)

    get_latest_version_info()

    print('Generating index_hardware.html')
    write_if_changed(os.path.join(path, 'source', 'index_hardware.html'), make_index_hardware())

    print('Generating index_api.html')
    write_if_changed(os.path.join(path, 'source', 'index_api.html'), make_index_api())

    print('Generating index_links.table')
    write_if_changed(os.path.join(path, 'source', 'index_links.table'), make_index_table())

    print('Generating Primer_bricks.table')
    write_if_changed(os.path.join(path, 'source', 'Primer_bricks.table'), make_primer_table(bricks, 'brick'))

    print('Generating Primer_bricklets.table')
    write_if_changed(os.path.join(path, 'source', 'Primer_bricklets.table'), make_primer_table(bricklets, 'bricklet'))

    print('Generating Primer_extensions.table')
    write_if_changed(os.path.join(path, 'source', 'Primer_extensions.table'), make_primer_table(extensions, 'extension'))

    print('Generating Primer_power_supplies.table')
    write_if_changed(os.path.join(path, 'source', 'Primer_power_supplies.table'), make_primer_table(power_supplies, 'power_supply'))

    print('Generating Primer_accessories.table')
    write_if_changed(os.path.join(path, 'source', 'Primer_accessories.table'), make_primer_table(accessories, 'accessory', False))

    print('Generating Downloads_tools.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_tools.table'), make_download_tools_table())

    print('Generating Downloads_bindings.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_bindings.table'), make_download_bindings_table())

    print('Generating Downloads_firmwares.table')
    write_if_changed(os.path.join(path, 'source', 'Downloads_firmwares.table'), make_download_firmwares_table())

    print('Generating API_Bindings_bindings.table')
    write_if_changed(os.path.join(path, 'source', 'Software', 'API_Bindings_bindings.table'), make_api_bindings_bindings_table())

    print('Generating Source_Code_gits.table')
    write_if_changed(os.path.join(path, 'source', 'Source_Code_gits.table'), make_source_code_gits_table())

    for brick in bricks:
        if len(brick.bindings) == 0:
            continue

        name = brick.url_part_for_hardware_doc

        print('Generating {0}_Brick_hlpi.table'.format(name))
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricks', name + '_Brick_hlpi.table'), make_hlpi_table(brick, 'brick'))

    for bricklet in bricklets:
        if len(bricklet.bindings) == 0:
            continue

        name = bricklet.url_part_for_hardware_doc

        print('Generating {0}_hlpi.table'.format(name))
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricklets', name + '_hlpi.table'), make_hlpi_table(bricklet, 'bricklet'))

    print('Generating Device_Identifier.table')
    write_if_changed(os.path.join(path, 'source', 'Software', 'Device_Identifier.table'), make_device_identifier_table())

    print('Generating Device_Identifier.table')
    write_if_changed(os.path.join(path, 'source', 'Tutorials', 'Tutorial_Authentication', 'Tutorial_authenticate_examples.table'), make_authentication_tutorial_examples_table())

    for binding in bindings:
        if not binding.is_programming_language:
            continue

        print('Generating API_Bindings_{0}_links.table'.format(binding.url_part_for_doc))
        write_if_changed(os.path.join(path, 'source', 'Software', 'API_Bindings_{0}_links.table'.format(binding.url_part_for_doc)), make_api_bindings_links_table(binding))

    print('Generating Bricks.toctree')
    write_if_changed(os.path.join(path, 'source', 'Software', 'Bricks.toctree'), make_devices_toctree(bricks, 'Brick'))

    print('Generating Bricklets.toctree')
    write_if_changed(os.path.join(path, 'source', 'Software', 'Bricklets.toctree'), make_devices_toctree(bricklets, 'Bricklet'))

if __name__ == "__main__":
    generate(os.getcwd())
