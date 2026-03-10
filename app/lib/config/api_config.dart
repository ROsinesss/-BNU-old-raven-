/// API 配置
class ApiConfig {
  // 后端服务地址
  static const String baseUrl = 'http://121.40.17.42:8000';

  // API 端点
  static const String login = '/api/auth/login';
  static const String logout = '/api/auth/logout';
  static const String schedule = '/api/schedule';
  static const String grades = '/api/grades';
  static const String exams = '/api/exams';
  static const String semesterInfo = '/api/semester-info';
}
