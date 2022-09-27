import 'package:bloc/bloc.dart';

import 'package:equatable/equatable.dart';
import 'package:flutter/rendering.dart';

class Device extends Equatable {
  Device(this.name, this.uid);

  String name;
  String uid;

  @override
  List<Object> get props => [name, uid];
}

class DeviceCubit extends Cubit<Device> {
  DeviceCubit() : super(Device('No Device', 'No Device Id'));

  void updateName(newName) => state.name = newName;
  void updateUid(newUid) => state.uid = newUid;
}
