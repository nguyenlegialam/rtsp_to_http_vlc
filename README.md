# Sử dụng VLC như 1 công cụ để tạo luồng http cho stream rtsp của camera  

Giải thích: chạy VLC ở terninal của máy tính nhúng (Raspberry) được đặt nội bộ LAN trong nhà, bằng sử dụng chức năng convert của VLC để tạo 1 luồng stream của camera qua các port của LAN. Lúc này, ID của camera trong DB sẽ là port số port được mở của camera đó trong code.
Điểm yếu:  
  - Mở port của router nên phải có phương pháp an toàn thông tin
  - Phải có máy tính nhúng được đặt on land connect với mạng LAN
Bước 1: chạy command VLC trên terminal của Raspberry

Bước 2: tạo url với phương pháp response là RedirectResponse
![image](https://github.com/nguyenlegialam/rtsp_to_http_vlc/assets/116132135/ddac3a8a-9af2-44c0-8525-181109adb98a)


