---
title: Home Systems
type: docs
---

## Networking and Internet

The property has two gigabit fiber internet services available. Brightspeed's 900Mbps up and down service is currently integrated with the home. Spectrum's fiber service is also available on the property.

A 12U size network rack in the lower unfinished area houses the following components:

| ||
|-|-|
|**Internet router**|A rack mount [UniFi Dream Machine Pro](https://store.ui.com/us/en/products/udm-pro) router and switch simplifies management of the home network and wireless access points|
|**Network switch**|Netgear 24-Port gigabit ethernet switch|
|**Network patch panel**|Simplifies connections between network cables and devices mounted in the network rack|
|**Uninterruptable Power Supply (UPS)**|CyberPower BRG1500AVRLCD Intelligent LCD UPS System 1500VA provides back up power and helps protect the equipment in case of power outages and power spikes|
|**Network Video Recorder (NVR)**|See [Outdoor Cameras]({{<ref "#outdoor-cameras" >}})|
{.table .table-striped}

A separate rack in the garage houses the internet fiber modem and other equipment. See [Garage Networking and A/V]({{<ref "05-garage#networking-and-av" >}}) for details.

### Wireless Access Points

All wireless access points were installed in 2022 at about the same time gigabit fiber internet service was established. Depending on your device, the WiFi 6 access points are capable of providing up to ~500Mbps speeds throughout the home and outside.

| ||
|-|-|
|**Dining room ceiling**|[UniFi U6-Pro](https://store.ui.com/us/en/products/u6-pro)|
|**Master suite ceiling**|UniFi U6-Pro|
|**Lower main room ceiling**|[UniFi U6-LR](https://store.ui.com/us/en/products/u6-lr)|
|**Garage ceiling**|UniFi U6-LR|
|**Deck facing lower land**|[UniFi U6-Mesh](https://store.ui.com/us/en/products/u6-mesh)|
|**Lower land light pole near railroad bridge**|UniFi U6-Mesh|
|**Lower land light pole near dock**|UniFi U6-Mesh|
{.table .table-striped}

## TV and Video Streaming

| | |
|-|-|
|**Apple TVs**|Apple TVs combined with the gigabit internet service enable access to video streaming services throughout the home|
|**OTA antenna**|Attic mounted over the air (OTA) HD television antennae enables free access to local TV programming|
|**OTA receiver**|SiliconDust HDHomeRun Flex 4K OTA receiver connects to the OTA antenna and the home network. Via the Channels app, you can view local HD broadcast stations through the Apple TVs and your phones.|
|**Satellite ready**|If you prefer satellite TV, a dish pole mount exists hidden behind the garage. Conduit is already in place to easily run coax from a dish to the garage and main home's lower level.|
{.table .table-striped}

## Security System

| | |
|-|-|
|**Central alarm system**|The central alarm sustem is an ADT Safewatch Pro Security System (Honeywell Ademco Vista 20p security panel). A subscription for ADT to provide remote monitoring is optional, but not necessary to use the security system.|
|**Keypads**|Keypads are located in the mud/laundry room and primary bedroom|
|**Exterior door contact sensors**|All exterior doors have built-in contact sensors|
|**Glass break sensors**|All rooms with windows that are accessible to ground level have glass break sensors|
|**Smoke sensor**|A smoke sensor is integrated with the security system (apart from multiple battery powered smoke and CO2 sensors)|
|**Home automation integration**|An [EyezOn EnvisaLink 4](https://www.eyezon.com/evl4.php) module connects to the security system as a third keypad. This networked module enables the security systems to be integrated with the home automation system. For example, you can control and monitor the system using your phone and automate actions based on events such as exterior doors opening and closing.|
{.table .table-striped}

## Outdoor Cameras

A series of Power Over Ethernet (PoE) network cameras are positioned outside the home to enable you to view the surroundings when you're home and away.

A [Hikvision DS-7616NI-I2/16P](https://www.hikvision.com/au-en/products/IP-Products/Network-Video-Recorders/Pro-Series/ds-7616ni-i2-16p/) Network Video Recorder (NVR) provides local storage for events and recordings. The Hikvison Hik Connect mobile app can be used to receive alerts and access your camera feeds from home and away. Since the NVR is in your home, there are no monthly subscription fees required to access your cameras and recordings.

Cameras cover the following outside areas:

| |
|-|
|Entry road hill|
|Driveway|
|Autocourt and front of home|
|Porch|
|Patio|
|Railroad bridge and creek (with audio)|
|Dock and creek (with audio)|
|Highway (winter only)|
|Entry road fence (winter only)|
{.table .table-striped}

{{< carousel ratio="16x9" class="col-sm-20 col-lg-20 mx-auto" >}}
  {{< img src="img/cameras/camera-driveway.png" >}}
  {{< img src="img/cameras/camera-house-front.png" >}}
  {{< img src="img/cameras/camera-porch.png" >}}
  {{< img src="img/cameras/camera-lower-land.png" >}}
  {{< img src="img/cameras/camera-bridge.png" >}}
  {{< img src="img/cameras/camera-entry-road.png" >}}
  {{< img src="img/cameras/camera-entry-fence.png" >}}
{{< /carousel >}}

## Doorbell and Camera

The main entry has a Ring Video Doorbell Pro 2.

## Weather Station

|||
|-|-|
|**Weather station**|Garage roof mounted [WeatherFlow Tempest](https://tempest.earth/tempest-home-weather-system/) wireless and solar powered weather system. Measures wind speed and direction, temperature, humidity, pressure, light level, and rainfall via a solid state rain gauge|
|**Home automation integration****|Outdoor weather data can be used to help automate home functions. For example, outside light levels help influence lighting decisions.|
|**Weather Underground integration**|Weather station publishes as site [KMODEFIA18](https://www.wunderground.com/dashboard/pws/KMODEFIA18?cm_ven=localwx_pwsdash) on the Weather underground|
{.table .table-striped}

## Home Automation

[Hubitat](https://hubitat.com/) home automation hubs enable control and automation of a wide variety of devices within the home. Three Hubitat devices are meshed and located in the living room (C-8 version), lower level (C-7 version), and garage (C-8 version). The hubs support Z-Wave, Zigbee, Apple HomeKit, and Matter (C-8 only).

Apple TVs distributed throughout the home act as Apple Home hubs. Currently, most of the home's smart switches and other devices are registered with the Hubitat devices. In turn, the Hubitat devices use their built-in support for HomeKit to make the devices available via the Apple Home app on iOS devices.

You have the option to define automations through the Apple Home app, Hubitat, or both.

Examples of remote control and automation already in place include:

| |
|-|
|Voice assistant control of living room fireplace. "Alexa, turn on the fireplace"|
|Voice assistant control of garage doors|
|Automatic early morning and evening inside and outdoor lighting schedules|
|Automatic arming the home security system in the late evening|
|Automatic turning on/off ceiling fans based on inside temperature|
|Automated monitoring of indoor and outdoor humidity levels and control of the whole house humidifier to align with target humidity level|
{.table .table-striped}

## Cable Conduits

PVC conduit has been installed to make it easy to route network, audio, and TV cables throughout the garage and home. Conduit runs are installed between the following areas of the home and garage:

| |
|-|
|Lower level unfinished to attic|
|Lower level unfinished to living room|
|Lower level unfinished to bedrooms|
|Lower level unfinished to lower level main room|
|Lower level unfinished to garage attic |
{.table .table-striped}
