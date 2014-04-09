#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

lang = 'en'

          # display,   uri
bricks = [('DC',      'dc'),
          ('Debug',   'debug'),
          ('IMU',     'imu'),
          ('Master',  'master'),
          ('Servo',   'servo'),
          ('Stepper', 'stepper')]

             # display,                    uri
bricklets = [('Ambient Light',             'ambient_light'),
             ('Analog In',                 'analog_in'),
             ('Analog Out',                'analog_out'),
             ('Barometer',                 'barometer'),
             ('Breakout',                  'breakout'),
             ('Color',                     'color'),
             ('Current12',                 'current12'),
             ('Current25',                 'current25'),
             ('Distance IR',               'distance_ir'),
             ('Distance US',               'distance_us'),
             ('Dual Button',               'dual_button'),
             ('Dual Relay',                'dual_relay'),
             ('GPS',                       'gps'),
             ('Hall Effect',               'hall_effect'),
             ('Heart Rate',                'heart_rate'),
             ('Humidity',                  'humidity'),
             ('Industrial Digital In 4',   'industrial_digital_in_4'),
             ('Industrial Digital Out 4',  'industrial_digital_out_4'),
             ('Industrial Dual 0-20mA',    'industrial_dual_0_20ma'),
             ('Industrial Quad Relay',     'industrial_quad_relay'),
             ('IO-16',                     'io16'),
             ('IO-4',                      'io4'),
             ('Joystick',                  'joystick'),
             ('LCD 16x2',                  'lcd_16x2'),
             ('LCD 20x4',                  'lcd_20x4'),
             ('LED Strip',                 'led_strip'),
             ('Line',                      'line'),
             ('Linear Poti',               'linear_poti'),
             ('Moisture',                  'moisture'),
             ('Motion Detector',           'motion_detector'),
             ('Multi Touch',               'multi_touch'),
             ('Piezo Buzzer',              'piezo_buzzer'),
             ('Piezo Speaker',             'piezo_speaker'),
             ('PTC',                       'ptc'),
             ('Remote Switch',             'remote_switch'),
             ('Rotary Encoder',            'rotary_encoder'),
             ('Rotary Poti',               'rotary_poti'),
             ('Segment Display 4x7',       'segment_display_4x7'),
             ('Sound Intensity',           'sound_intensity'),
             ('Temperature',               'temperature'),
             ('Temperature IR',            'temperature_ir'),
             ('Tilt',                      'tilt'),
             ('Voltage',                   'voltage'),
             ('Voltage/Current',           'voltage_current'),
            ]

ipcon_common = {
'en': """
>>>intro
This is the API description for the |ref_api_bindings| of the IP Connection.
The IP Connection is established between a :ref:`Brick Daemon <brickd>`
or a :ref:`WIFI <wifi_extension>`/:ref:`Ethernet <ethernet_extension>` Extension
and the corresponding programming language API bindings. You need to
create an IP Connection, connect it and add devices, before you can
use them.

An overview of products that are controllable over an IP Connection
can be found :ref:`here <product_overview>`.
<<<intro
""",
'de': """
>>>intro
Dies ist die API Beschreibung für die |ref_api_bindings| der IP Connection.
Die IP Connection wird zwischen einem :ref:`Brick Daemon <brickd>` oder
einer :ref:`WIFI <wifi_extension>`/:ref:`Ethernet <ethernet_extension>` Extension und den API
Bindings der entsprechenden Programmiersprache hergestellt. Bevor Geräte über
deren API angesprochen werden können muss eine IP Connection erzeugt, verbunden
und die Geräte dieser hinzugefügt werden.

Eine Übersicht über die Produkte die über eine IP Connection kontrolliert
werden können ist :ref:`hier <product_overview>` zu finden.
<<<intro
"""
}

brick_test_intro = {
'en':
""".. |test_intro| replace::
 To test the {0} Brick you need to have the
 :ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>` installed
 (for installation guides click :ref:`here <brickd_installation>`
 and :ref:`here <brickv_installation>`) and the Brick Viewer has to be connected
 to the Brick Daemon.
""",
'de':
""".. |test_intro| replace::
 Um den {0} Brick testen zu können müssen der
 :ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
 (für Installationsanleitungen :ref:`hier <brickd_installation>`
 und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
 dem Brick Daemon verbunden sein.

"""
}

brick_test_tab = {
'en':
""".. |test_tab| replace::
 Now connect the Brick to the PC over USB, you should see a new tab named
 "{0} Brick" in the Brick Viewer after a moment. Select this tab.
""",
'de':
""".. |test_tab| replace::
 Wenn der Brick per USB an den PC angeschlossen wird sollte einen Moment später
 im Brick Viewer ein neuer Tab namens "{0} Brick" auftauchen. Wähle diesen Tab
 aus.
"""
}

brick_test_pi_ref = {
'en':
""".. |test_pi_ref| replace::
 After this test you can go on with writing your own application.
 See the :ref:`Programming Interface <{0}_brick_programming_interface>`
 section for the API of the {1} Brick and examples in different programming
 languages.
""",
'de':
""".. |test_pi_ref| replace::
 Nun kann ein eigenes Programm geschrieben werden. Der Abschnitt
 :ref:`Programmierschnittstelle <{0}_brick_programming_interface>` listet die
 API des {1} Bricks und Beispiele in verschiedenen Programmiersprachen auf.
"""
}

bricklet_case_steps = {
'en':
"""
>>>bricklet_case_steps
The assembly is easiest if you follow the following steps:

* Screw spacers to the Bricklet,
* screw bottom plate to bottom spacers,
* build up side plates,
* plug side plates into bottom plate and
* screw top plate to top spacers.

Below you can see an exploded assembly drawing of the {0} Bricklet case:
<<<bricklet_case_steps
""",
'de':
"""
>>>bricklet_case_steps
Der Aufbau ist am einfachsten wenn die folgenden Schritte befolgt werden:

* Schraube Abstandshalter an das Bricklet,
* schraube Unterteil an untere Abstandshalter,
* baue Seitenteile auf,
* stecke zusammengebaute Seitenteile in Unterteil und
* schraube Oberteil auf obere Abstandshalter.

Im folgenden befindet sich eine Explosionszeichnung des {0} Bricklet-Gehäuse:
<<<bricklet_case_steps
"""
}

bricklet_case_hint = {
'en':
""".. |bricklet_case_hint| replace::
 Hint: There is a protective film on both sides of the plates,
 you have to remove it before assembly.
""",
'de':
""".. |bricklet_case_hint| replace::
 Hinweis: Auf beiden Seiten der Platten ist eine Schutzfolie, 
 diese muss vor dem Zusammenbau entfernt werden.
"""
}


bricklet_test_intro = {
'en':
""".. |test_intro| replace::
 To test the {0} Bricklet you need to have the
 :ref:`Brick Daemon <brickd>` and the :ref:`Brick Viewer <brickv>` installed
 (for installation guides click :ref:`here <brickd_installation>`
 and :ref:`here <brickv_installation>`) and the Brick Viewer has to be connected
 to the Brick Daemon.
""",
'de':
""".. |test_intro| replace::
 Um das {0} Bricklet testen zu können müssen der
 :ref:`Brick Daemon <brickd>` und der :ref:`Brick Viewer <brickv>` installiert
 (für Installationsanleitungen :ref:`hier <brickd_installation>`
 und :ref:`hier <brickv_installation>` klicken) und der Brick Viewer muss mit
 dem Brick Daemon verbunden sein.
"""
}

bricklet_test_connect = {
'en':
""".. |test_connect| replace::
 Connect the {0} Bricklet to a :ref:`Brick <product_overview_bricks>`
 with a Bricklet Cable
""",
'de':
""".. |test_connect| replace::
 Als nächstes muss das {0} Bricklet mittels eines Bricklet Kabels mit
 einem :ref:`Brick <product_overview_bricks>` verbunden werden
"""
}

bricklet_test_tab = {
'en':
""".. |test_tab| replace::
 If you connect the Brick to the PC over USB, you should see a new tab named
 "{0} Bricklet" in the Brick Viewer after a moment. Select this tab.
""",
'de':
""".. |test_tab| replace::
 Wenn der Brick per USB an den PC angeschlossen wird sollte einen Moment später
 im Brick Viewer ein neuer Tab namens "{0} Bricklet" auftauchen.
 Wähle diesen Tab aus.
"""
}

bricklet_test_pi_ref = {
'en':
""".. |test_pi_ref| replace::
 After this test you can go on with writing your own application.
 See the :ref:`Programming Interface <{0}_bricklet_programming_interface>`
 section for the API of the {1} Bricklet and examples in different programming
 languages.
""",
'de':
""".. |test_pi_ref| replace::
 Nun kann ein eigenes Programm geschrieben werden. Der Abschnitt
 :ref:`Programmierschnittstelle <{0}_bricklet_programming_interface>` listet
 die API des {1} Bricklets und Beispiele in verschiedenen
 Programmiersprachen auf.
"""
}

def make_ipcon_substitutions():
    substitutions = ''
    substitutions += ipcon_common[lang]

    return substitutions

def make_brick_substitutions(brick):
    substitutions = ''
    substitutions += brick_test_intro[lang].format(brick[0]) + '\n'
    substitutions += brick_test_tab[lang].format(brick[0]) + '\n'
    substitutions += brick_test_pi_ref[lang].format(brick[1], brick[0])

    return substitutions

def make_bricklet_substitutions(bricklet):
    substitutions = ''
    substitutions += '>>>substitutions\n'
    substitutions += bricklet_test_intro[lang].format(bricklet[0]) + '\n'
    substitutions += bricklet_test_connect[lang].format(bricklet[0]) + '\n'
    substitutions += bricklet_test_tab[lang].format(bricklet[0]) + '\n'
    substitutions += bricklet_test_pi_ref[lang].format(bricklet[1], bricklet[0]) + '\n'
    substitutions += bricklet_case_hint[lang] + '\n'
    substitutions += '<<<substitutions\n'
    substitutions += bricklet_case_steps[lang].format(bricklet[0]) + '\n'

    return substitutions

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
        print 'Wrong working directory'
        sys.exit(1)

    write_if_changed(os.path.join(path, 'source', 'Software', 'IPConnection_Common.substitutions'), make_ipcon_substitutions())

    for brick in bricks:
        name = brick[0].replace(' ', '_').replace('-', '').replace('/', '_')

        print 'Generating {0}_Brick.substitutions (Hardware)'.format(name)
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricks', name + '_Brick.substitutions'), make_brick_substitutions(brick))

    for bricklet in bricklets:
        name = bricklet[0].replace(' ', '_').replace('-', '').replace('/', '_')

        print 'Generating {0}.substitutions (Hardware)'.format(name)
        write_if_changed(os.path.join(path, 'source', 'Hardware', 'Bricklets', name + '.substitutions'), make_bricklet_substitutions(bricklet))

if __name__ == "__main__":
    generate(os.getcwd())
