from datetime import datetime, timedelta

print("\n--- THÊM 5 GIÂY VÀO THỜI GIAN HIỆN TẠI ---")
bay_gio = datetime.now()
thoi_gian_moi = bay_gio + timedelta(seconds=5)

print(f"Thời gian hiện tại: {bay_gio.strftime('%H:%M:%S')}")
print(f"Thời gian sau 5 giây: {thoi_gian_moi.strftime('%H:%M:%S')}")