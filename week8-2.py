x = int(input("請輸入購買飲料數量?"));
total = (x % 12 * 20)+(x // 12 * 200);
print(f"需花費 {total}");
