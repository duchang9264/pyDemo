inster = 'INSERT INTO iss.bdp_recover_vehicle_log (vin, vehicleNo, vehicle_model_seq, rentType, recover_reson, recover_time, recover_place, shop_seq, lose_time, lose_province, lose_city, lose_district, lose_place, lose_area_id, recover_province, recover_city, recover_district, recover_area_id, risk_vehicle_id, create_time, create_user, update_time, update_user, misc_desc, status, user_phone, images_url) VALUES ("LSJA24034HS179710", "沪AD84970", 188, 0, "", "2020-08-07 09:27:22", "上海汽车城大厦", 3, "2020-07-22 22:43:11", "上海市", "上海市", "浦东新区", "上海市浦东新区华鹏路300弄-1-～16号", 310115, "上海市", "上海市", "嘉定区", 310114, 2156, "2020-08-07 09:27:49", "bdpSystem", "2020-08-07 09:27:49", "", "", 1, "15652062956", "vehicleInfo/riskReport_file/73160d6c-6830-4b53-a79a-c06c637bc076/202008070927426360.jpg");'
a_range= range(30000)
k=[inster for i in a_range]
print(k)
text_file = open("Output.txt", "w")

text_file.write(''.join(k))

text_file.close()