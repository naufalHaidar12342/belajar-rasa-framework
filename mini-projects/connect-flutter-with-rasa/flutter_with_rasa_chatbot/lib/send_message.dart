import 'package:dio/dio.dart';

Future<String> sendMessage(String message) async {
  const rest = "http://192.168.43.78:5005/webhooks/rest/webhook";

  final request = {"sender": "dimas", "message": message};

  final response = await Dio().post(rest, data: request);
  return response.data[0]["text"];
}
