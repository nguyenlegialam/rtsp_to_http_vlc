# Sử dụng VLC như 1 công cụ để tạo luồng http cho stream rtsp của camera  
  
Ngôn ngữ: Python
  
Giải thích: chạy VLC ở terninal của máy tính nhúng (Raspberry) được đặt nội bộ LAN trong nhà, bằng sử dụng chức năng convert của VLC để tạo 1 luồng stream của camera qua các port của LAN. Lúc này, ID của camera trong DB sẽ là số port được mở của camera đó trong command. Các command được lưu lại trong file docx đính kèm, trong đó có ghi rõ các command hoạt động và cách sử dụng. Mỗi camera sẽ stream qua mỗi port khác nhau, trong project gốc thì:  
  - Cam cổng: 9911
  - Cam trệt: 9912
  - Cam tầng 1: 9913
  - ...
  
Yêu cầu:  
  - Link Rtsp của camera
  - Máy tính được đặt chung mạng LAN hoặc VPN đến mạng LAN đó
  - Cài đặt python >3.6 và các thư viện bên ngoài trong requirement
  - Cài đặt VLC media trong máy tính  
  
Điểm yếu:  
  - Thêm camera bằng cách tạo và chạy command trên terminal, cách thêm camera được hướng dẫn trong file docx  
  
# Cách chạy project:  
  
Bước 1: Mở terminal của máy tính được cài đặt ở mạng LAN (Window, Linux(Raspberry),...)  
  
Bước 2: Nhập các command trong file docx được đính kèm để VLC bắt đầu stream HTTP  
![image](https://github.com/nguyenlegialam/rtsp_to_http_vlc/assets/116132135/1a6c12be-baaf-4f12-ba41-4aadd8b379ea)  
  
Sau bước này, các luồng stream http của camera đã được VLC thực hiện. 
  
Bước 3: run rtsp_http_vlc.py  
   
Kiểm tra luồng stream có hoạt động hay không bằng cách gõ url: localhost:6064/cam-cong








