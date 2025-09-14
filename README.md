# CN331 Assignment 2 – Classroom Booking
## Members
- 6710525038 – นางสาวเอมมิตรา แสวงทรัพย์
- 6710535029 – นายวุฒิศักดิ์ บุญกัน

## Features
1. Login/Logout (admin, users)
-  ระบบจะทำการเช็คว่า ID ไหนที่ตรงกับ superuser ระบบจะนำไปยังหน้า admin_dashboard และหากไม่มี ID นั้นใน superuser จะนำทางไปยัง defult ของระบบนั้นก็คือไปฝั่ง user เหมือนเดิม
-  และหากระบบตรวจเจอว่า ID, Password ผิด ระบบจะแจ้งเตือนว่า id, password ที่ท่านกรอกผิด
2 . Admin จัดการห้องเรียนใน Django Admin, admin_dashboard
- Django Admin interface - admin สามารถเพิ่ม ลบ และเปลี่ยนแปลงรายระเอียดของ User, booking (ระบบการจองห้อง), classroom (รหัสห้อง, ชื่อห้อง, กำหนดจำนวนคนที่ห้องนั้นรับได้, กำหนดช่วงเวลาที่เปิดให้จอง, กำหนดสถานะของห้อง) ได้
- admin_dashboard - admin สามารถดูว่า User ไหนที่ทำการจองห้องนั้นไว้ได้ผ่าน admin_dashborad
3. Users จอง/ยกเลิกห้องได้
- User สามารถจองห้องได้โดยมี condition คือ User สามารถจองห้องได้วันละ 1 ชั่วโมงเท่านั้น กล่าวคือ User ไม่สามารถจองสองห้องภายในวันเดียวได้และภายในหนึ่งวันท่านสามารถจองได้แค่ 1 ชั่วโมง
- User สามารถยกเลิกการจองห้องโดยกดที่ปุ่มยกเลิก

## Present
- https://youtu.be/KdhCKFSpDtw?si=AOQIFcIESsU3nbh2
