import 'package:flutter/material.dart';
import 'package:flutter_with_rasa_chatbot/send_message.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  TextEditingController messageController = TextEditingController();
  String responseMessage = "Hello World!";

  @override
  void dispose() {
    messageController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(32),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            SafeArea(
              child: Text(responseMessage),
            ),
            const SizedBox(
              height: 32,
            ),
            TextField(
              controller: messageController,
              decoration: const InputDecoration(hintText: "Message"),
            ),
            const SizedBox(
              height: 32,
            ),
            ElevatedButton(
              onPressed: () async {
                final response = await sendMessage(messageController.text);
                setState(() {
                  responseMessage = response;
                  messageController.text = "";
                });
              },
              child: const SizedBox(
                width: double.infinity,
                child: Center(
                  child: Text('Send'),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
