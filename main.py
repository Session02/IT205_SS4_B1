first_money = int(input("Nhập tổng tiền hóa đơn ban đầu: "))

if first_money > 500000:
    decrease_money = first_money * 0.1
else:
    decrease_money = first_money

print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
print(f"Số tiền được giảm giá: {int(decrease_money)}")
print(f"Tổng tiền khách phải trả: {first_money - int(decrease_money)}")