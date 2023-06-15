# Sử dụng VLC như 1 công cụ để tạo luồng http cho stream rtsp của camera  

Giải thích: chạy VLC ở terninal của máy tính nhúng (Raspberry) được đặt nội bộ LAN trong nhà, bằng sử dụng chức năng convert của VLC để tạo 1 luồng stream của camera qua các port của LAN. Lúc này, ID của camera trong DB sẽ là số port được mở của camera đó trong command.  
Điểm yếu:  
  - Mở port của router nên phải có phương pháp an toàn thông tin
  - Phải có máy tính nhúng được đặt on land connect với mạng LAN  

Cách chạy project:  
Bước 1: Mở terminal của máy tính được cài đặt ở mạng LAN (Raspberry,...)  
Bước 2: Nhập các command trong file docx được đính kèm để VLC bắt đầu stream HTTP  
![image](https://github.com/nguyenlegialam/rtsp_to_http_vlc/assets/116132135/1a6c12be-baaf-4f12-ba41-4aadd8b379ea)  

Sau bước này, các luồng stream http của camera đã được VLC thực hiện. Bước tiếp theo sẽ là Redirect lại url để tạo api như mong muốn  
Bước 3: run code trên terminal  
Linux: sudo rtsp_http_vlc.py   









