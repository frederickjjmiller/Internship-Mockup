# airwave_api.py
# Origionally by Conner Page
# Re-Written by J.J. Miller, so it has functions and can be called.
# 8/1/2018
# Purpose: Aruba Airwave API calls for Ascension Information Services Device Location Program

import requests


def airwave_api_call(mac):

    # setup and API request
    data = 'credential_0=stvuser&credential_1=K33pitEZ@&destination=/&login=Log In'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Cache-Control': 'no-cache'}
    ampsession = requests.Session()
    loginamp = ampsession.post('https://10.170.11.209/LOGIN', headers=headers, data=data, verify=False)
    # print (loginamp)
    ampsession.cookies
    outamp = ampsession.get('https://10.170.11.209/client_detail.xml?mac=' + mac, headers=headers, verify=False)
    # print (outamp)
    output = outamp.content
    # print (output)
    # Next line is for testing so API call does not need to be called
    # output=b'<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n<amp:amp_client_detail version="1" xmlns:amp="http://www.airwave.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.airwave.com amp_client_detail.xsd">\n  <client mac="40:83:DE:CD:0A:23">\n    <ap id="3849">ININD-IND-CD2A-AP20</ap>\n    <assoc_stat>true</assoc_stat>\n    <association id="327884940">\n      <ap id="3851">ININD-IND-CD2A-AP21</ap>\n      <bytes_used>0</bytes_used>\n      <connect_time>2018-06-12T07:54:50-04:00</connect_time>\n      <disconnect_time>2018-06-12T07:55:46-04:00</disconnect_time>\n      <radio_mode>N</radio_mode>\n      <rssi>50</rssi>\n      <ssid>AH-VOICE</ssid>\n      <vlan>156</vlan>\n    </association>\n    <association id="327884040">\n      <ap id="3850">ININD-IND-CD2A-AP02</ap>\n      <bytes_used>0</bytes_used>\n      <connect_time>2018-06-12T07:54:40-04:00</connect_time>\n      <disconnect_time>2018-06-12T07:54:50-04:00</disconnect_time>\n      <radio_mode>N</radio_mode>\n      <ssid>AH-VOICE</ssid>\n      <vlan>156</vlan>\n    </association>\n    <association id="327883814">\n      <ap id="3839">ININD-IND-CD2A-AP03</ap>\n      <bytes_used>0</bytes_used>\n      <connect_time>2018-06-12T07:54:25-04:00</connect_time>\n      <disconnect_time>2018-06-12T07:54:40-04:00</disconnect_time>\n      <radio_mode>N</radio_mode>\n      <ssid>AH-VOICE</ssid>\n      <vlan>156</vlan>\n    </association>\n    <association id="327883667">\n      <ap id="3840">ININD-IND-CD2A-AP04</ap>\n      <bytes_used>0</bytes_used>\n      <connect_time>2018-06-12T07:53:44-04:00</connect_time>\n      <disconnect_time>2018-06-12T07:54:25-04:00</disconnect_time>\n      <radio_mode>N</radio_mode>\n      <rssi>52</rssi>\n      <ssid>AH-VOICE</ssid>\n      <vlan>156</vlan>\n    </association>\n    <association id="327882890">\n      <ap id="3853">ININD-IND-CD2A-AP17</ap>\n      <bytes_used>0</bytes_used>\n      <connect_time>2018-06-12T07:53:19-04:00</connect_time>\n      <disconnect_time>2018-06-12T07:53:44-04:00</disconnect_time>\n      <radio_mode>N</radio_mode>\n      <rssi>39</rssi>\n      <ssid>AH-VOICE</ssid>\n      <vlan>156</vlan>\n    </association>\n    <auth_stat>false</auth_stat>\n    <connect_time>2018-06-12T07:55:46-04:00</connect_time>\n    <device_type>Android</device_type>\n    <login_time>2017-12-04T10:35:17-05:00</login_time>\n    <logout_time>2017-12-04T10:39:46-05:00</logout_time>\n    <radio_mode>N</radio_mode>\n    <signal>-44</signal>\n    <ssid>AH-VOICE</ssid>\n    <vendor>Zebra Technologies Inc</vendor>\n    <vlan>156</vlan>\n  </client>\n</amp:amp_client_detail>\n'
    output = output.decode("utf-8")

