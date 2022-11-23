import 'package:cargo_bot_mobile_app/bloc/cargo_bot_cubit.dart';
import 'package:cargo_bot_mobile_app/pages/main_screen.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

void main() {
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    home: AppWidget(),
  ));
}

class AppWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey,
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Center(
            child: Container(
              width: 1200,
              height: 830,
              child: BlocProvider<CargoBotCubit>(
                create: (context) => CargoBotCubit(),
                child: const MainScreen(),
              ),
            ),
          )
        ],
      ),
    );
  }
}
