import 'dart:async';
import 'dart:io' show Platform;
import 'package:bloc/bloc.dart';
import 'dart:typed_data';
import 'dart:convert';

import 'package:location_permissions/location_permissions.dart';
import 'package:flutter/material.dart';
import 'package:flutter_reactive_ble/flutter_reactive_ble.dart';

void main() {
  return runApp(
    const MaterialApp(
      home: HomePage(),
      debugShowCheckedModeBanner: false,
    ),
  );
}

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
// Some state management stuff
  bool _foundDeviceWaitingToConnect = false;
  bool _scanStarted = false;
  bool _connected = false;
// Bluetooth related variables
  late DiscoveredDevice _ubiqueDevice;
  final flutterReactiveBle = FlutterReactiveBle();
  late StreamSubscription<DiscoveredDevice> _scanStream;
  late QualifiedCharacteristic _rxCharacteristic;
// These are the UUIDs of your device
  final Uuid serviceUuid = Uuid.parse("12341000-1234-1234-1234-123456789abc");
  final Uuid characteristicUuid = Uuid.parse("2A6E");
  final Uuid characteristicUuid_2 = Uuid.parse("2904");
  final String macAddress =
      'B8:27:EB:BF:42:C0'; // Check new mac address everytime you run the app run hciconfig -a

  void _startScan() async {
// Platform permissions handling stuff
    bool permGranted = false;
    setState(() {
      _scanStarted = true;
    });
    PermissionStatus permission;
    if (Platform.isAndroid) {
      permission = await LocationPermissions().requestPermissions();
      if (permission == PermissionStatus.granted) permGranted = true;
    } else if (Platform.isIOS) {
      permGranted = true;
    }
// Main scanning logic happens here ⤵️
    if (permGranted) {
      print("Starting scan");
      _scanStream = flutterReactiveBle
          .scanForDevices(withServices: [serviceUuid]).listen((device) {
        // Change this string to what you defined in Zephyr
        print(device.name);
        if (device.name == 'Cargo Bot') {
          setState(() {
            _ubiqueDevice = device;
            _foundDeviceWaitingToConnect = true;
          });
        }
      });
    }
  }

  void _connectToDevice() {
    // We're done scanning, we can cancel it
    _scanStream.cancel();
    // Let's listen to our connection so we can make updates on a state change
    Stream<ConnectionStateUpdate> _currentConnectionStream = flutterReactiveBle
        .connectToAdvertisingDevice(
            id: _ubiqueDevice.id,
            prescanDuration: const Duration(seconds: 1),
            withServices: [serviceUuid, characteristicUuid]);
    _currentConnectionStream.listen((event) {
      switch (event.connectionState) {
        // We're connected and good to go!
        case DeviceConnectionState.connected:
          {
            print('Connected to device');
            _rxCharacteristic = QualifiedCharacteristic(
                serviceId: serviceUuid,
                characteristicId: characteristicUuid,
                deviceId: macAddress);
            setState(() {
              _foundDeviceWaitingToConnect = false;
              _connected = true;
            });
            break;
          }
        // Can add various state state updates on disconnect
        case DeviceConnectionState.disconnected:
          {
            print('Disconnected from device');
            break;
          }
        default:
      }
    });
  }

  void _connect() async {
    _scanStream.cancel();
    flutterReactiveBle
        .connectToDevice(
      id: macAddress,
      servicesWithCharacteristicsToDiscover: {
        serviceUuid: [characteristicUuid, characteristicUuid_2]
      },
      connectionTimeout: const Duration(seconds: 2),
    )
        .listen((connectionState) {
      // Handle connection state updates
    }, onError: (Object error) {
      // Handle a possible error
    });
  }

  void _readCharacteristic() async {
    print("reading");
    final characteristic = QualifiedCharacteristic(
        serviceId: serviceUuid,
        characteristicId: characteristicUuid,
        deviceId: macAddress);
    final response =
        await flutterReactiveBle.readCharacteristic(characteristic);
    print(response);
  }

  void _partyTime() async {
    if (_connected) {
      final characteristic = QualifiedCharacteristic(
          serviceId: serviceUuid,
          characteristicId: characteristicUuid,
          deviceId: macAddress);
      final response =
          await flutterReactiveBle.readCharacteristic(characteristic);
      print(response);
      // final characteristic = QualifiedCharacteristic(
      //     serviceId: serviceUuid,
      //     characteristicId: characteristicUuid,
      //     deviceId: macAddress);
      // flutterReactiveBle.subscribeToCharacteristic(characteristic).listen(
      //     (data) {
      //   // code to handle incoming data
      // }, onError: (dynamic error) {
      //   // code to handle errors
      // });
    }
  }

  void _sendDisplayData() async {
    if (_connected) {
      String foo = 'Hello world';
      int bar = 123;
      List<int> bytes = utf8.encode(bar.toString());
      print("writing to characteristic");
      final characteristic = QualifiedCharacteristic(
          serviceId: serviceUuid,
          characteristicId: characteristicUuid,
          deviceId: macAddress);
      flutterReactiveBle.writeCharacteristicWithoutResponse(characteristic,
          value: bytes);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Robo Code',
        ),
        centerTitle: true,
      ),
      backgroundColor: Colors.white,
      body: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                padding: const EdgeInsets.fromLTRB(10, 50, 5, 0),
                child: const Text(
                  "Weight Load",
                  style: TextStyle(
                    fontSize: 16,
                  ),
                ),
              ),
              Container(
                padding: const EdgeInsets.fromLTRB(10, 50, 10, 0),
                width: 100,
                height: 100,
                child: const TextField(
                  style: TextStyle(
                    fontSize: 20,
                  ),
                  decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: '',
                      enabled: false),
                ),
              ),
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                padding: const EdgeInsets.fromLTRB(10, 50, 10, 0),
                child: const Text(
                  "LCD Display",
                  style: TextStyle(
                    fontSize: 16,
                  ),
                ),
              ),
              Container(
                padding: const EdgeInsets.fromLTRB(10, 50, 10, 0),
                width: 200,
                height: 100,
                child: const TextField(
                  style: TextStyle(
                    fontSize: 20,
                  ),
                  decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: '',
                  ),
                ),
              ),
              Container(
                  padding: const EdgeInsets.fromLTRB(0, 50, 0, 0),
                  width: 60,
                  height: 90,
                  child: ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      primary: Colors.blue, // background
                      onPrimary: Colors.white, // foreground
                    ),
                    onPressed: _sendDisplayData,
                    child: const Icon(Icons.mail),
                  )),
            ],
          ),
        ],
      ),
      persistentFooterButtons: [
        // We want to enable this button if the scan has NOT started
        // If the scan HAS started, it should be disabled.
        _scanStarted
            // True condition
            ? ElevatedButton(
                style: ElevatedButton.styleFrom(
                  primary: Colors.grey, // background
                  onPrimary: Colors.white, // foreground
                ),
                onPressed: () {},
                child: const Icon(Icons.search),
              )
            // False condition
            : ElevatedButton(
                style: ElevatedButton.styleFrom(
                  primary: Colors.blue, // background
                  onPrimary: Colors.white, // foreground
                ),
                onPressed: _startScan,
                child: const Icon(Icons.search),
              ),
        _foundDeviceWaitingToConnect
            // True condition
            ? ElevatedButton(
                style: ElevatedButton.styleFrom(
                  primary: Colors.blue, // background
                  onPrimary: Colors.white, // foreground
                ),
                onPressed: _connectToDevice,
                child: const Icon(Icons.bluetooth),
              )
            // False condition
            : ElevatedButton(
                style: ElevatedButton.styleFrom(
                  primary: Colors.grey, // background
                  onPrimary: Colors.white, // foreground
                ),
                onPressed: () {},
                child: const Icon(Icons.bluetooth),
              ),
        _connected
            // True condition
            ? ElevatedButton(
                style: ElevatedButton.styleFrom(
                  primary: Colors.blue, // background
                  onPrimary: Colors.white, // foreground
                ),
                onPressed: _readCharacteristic,
                child: const Icon(Icons.mail),
              )
            // False condition
            : ElevatedButton(
                style: ElevatedButton.styleFrom(
                  primary: Colors.grey, // background
                  onPrimary: Colors.white, // foreground
                ),
                onPressed: _partyTime,
                child: const Icon(Icons.mail),
              ),
      ],
    );
  }
}
