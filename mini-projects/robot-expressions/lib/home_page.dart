import 'package:flutter/material.dart';
import 'package:rive/rive.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  // rive controller and input
  StateMachineController? controller;

  SMIInput<bool>? isChecking;
  SMIInput<double>? numLook;
  SMIInput<bool>? isHandsUp;
  SMIInput<bool>? trigSuccess;
  SMIInput<bool>? trigFail;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromARGB(255, 214, 226, 234),
      body: Column(
        children: [
          const SizedBox(
            height: 32,
          ),
          Expanded(
            child: RiveAnimation.asset(
              "assets/teddy.riv",
              stateMachines: const ["Login Machine"],
              onInit: (artboard) {
                controller = StateMachineController.fromArtboard(
                  artboard,
                  // from rive, you can see it in rive editor
                  "Login Machine",
                );

                if (controller == null) return;

                artboard.addController(controller!);
                isChecking = controller?.findInput("isChecking");
                numLook = controller?.findInput("numLook");
                isHandsUp = controller?.findInput("isHandsUp");
                trigSuccess = controller?.findInput("trigSuccess");
                trigFail = controller?.findInput("trigFail");
              },
            ),
          ),
          const SizedBox(
            height: 32,
          ),
          Row(
            mainAxisSize: MainAxisSize.max,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              ElevatedButton(
                onPressed: () {
                  trigSuccess?.change(true);
                },
                child: const Text("Senyum"),
              ),
              const SizedBox(
                width: 16,
              ),
              ElevatedButton(
                onPressed: () {
                  trigFail?.change(true);
                },
                child: const Text("Sedih"),
              ),
            ],
          ),
          const SizedBox(
            height: 32,
          ),
        ],
      ),
    );
  }
}
