import 'package:bloc/bloc.dart';

import 'package:equatable/equatable.dart';
import 'package:flutter/rendering.dart';

class CargoBot extends Equatable {
  CargoBot(this.weightLoad, this.lcdText);

  String weightLoad;
  String lcdText;

  @override
  List<Object> get props => [weightLoad, lcdText];
}

class CargoBotCubit extends Cubit<CargoBot> {
  CargoBotCubit() : super(CargoBot('', ''));

  void updateCurrentWeightLoad(newWeightLoad) =>
      state.weightLoad = newWeightLoad;
  void updatelcdScreenText(newLcdText) => state.lcdText = newLcdText;
}
