# CN331 Assignment 3 – Classroom Booking
## Members
- 6710525038 – นางสาวเอมมิตรา แสวงทรัพย์
- 6710535029 – นายวุฒิศักดิ์ บุญกัน

## Features
1. Login/Logout (admin, users)
-  ระบบจะทำการเช็คว่า ID ไหนที่ตรงกับ superuser ถ้าตรงระบบจะนำไปยังหน้า admin_dashboard และหากไม่มีตรงระบบจะนำทางไปยัง defult ของระบบนั่นก็คือไปเข้าฝั่ง user เช่นเดิม
-  และหากระบบตรวจเจอว่า ID, Password ผิด ระบบจะแจ้งเตือนว่า id, password ที่ท่านกรอกผิด
2. Admin จัดการห้องเรียนใน Django Admin, admin_dashboard
- Django Admin interface - admin สามารถเพิ่ม ลบ และเปลี่ยนแปลงรายระเอียดของ User, booking (ระบบการจองห้อง), classroom (รหัสห้อง, ชื่อห้อง, กำหนดจำนวนคนที่ห้องนั้นรับได้, กำหนดช่วงเวลาที่เปิดให้จอง, กำหนดสถานะของห้อง) ได้
- admin_dashboard - admin สามารถดูว่า User ไหนที่ทำการจองห้องนั้นไว้ได้ผ่าน admin_dashborad
3. Users จอง/ยกเลิกห้องได้
- User สามารถจองห้องได้โดยมี condition คือ User สามารถจองห้องได้วันละ 1 ชั่วโมงเท่านั้น กล่าวคือ User ไม่สามารถจองสองห้องภายในวันเดียวได้และภายในหนึ่งวันท่านสามารถจองได้แค่ 1 ชั่วโมง
- User สามารถยกเลิกการจองห้องโดยกดที่ปุ่มยกเลิก

## Present

1. Web Application Booking room
- https://youtu.be/KdhCKFSpDtw?si=AOQIFcIESsU3nbh2
2. สาธิตการใช้งานเว็บ
- https://youtu.be/EvdOQEjnJxI?si=CAmiC07FCi7rXh-J


## Deploy 
- https://cn331-as2-deploywebapp.onrender.com
