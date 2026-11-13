import json
import os
from datetime import datetime 

FILE_NAME = "database.json"

def load_data():
  if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as file:
      return json.load(file)

return {
  "tasks": []
  "exspenses": []
}

def save_data():
  with open(FILE_NAME, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

data = load_data()

def add_task():
  task = imput("Vazifa nomini kiriting: ")

if task.stript() == "":
  print("Vazifa bo'sh bo'lmasligi kerak!")
  return

new_task = {
  "id": len(data["task"]) + 1,
  "name": task,
  "done": False,
  "date": datetime.now().strftime("%Y-%m-%d")
}

data["tasks"].append(new_task)
save_data()
print("Vazifa muvaffaqiyatli qo'shildi!")

def show_tasks():
  print("\n--- VAZIFALAR ---")

  if not data["tasks"]:
    print("Hozircha vazifalar yo'q.")
    return

for task in data["tasks"]:
  status = "Bajarilgan" if task["done"] else "Bajarilmagan"
  print(f'{task["id"]}. {task["name"]} |
  {status}')

def complate_task(0:
    show_task()

try:
  task_id int(input("Bajarilgan vazifa Id sini kiriting"))

  for task in data["tasks"]:
    if task["id"] == task_id:
      task["done"] = True
      save_data()
      print("vazifa bajarildi!")
      return

print("Bunday ID topilmadi.")

except ValueError:
    print("Faqat raqam kiriting!")

def add_expense():
  name = input("xarajat nomi: ")

  try:
    amount = float(input("Xarajat summasi: "))

    if ammount <= 0:
      print("Summa noldan katta bo'lishi kerak!")
      return

   expense = {
     "name": name,
     "amount": amount,
     "date": datetime.now().strftime("%Y-%m-%d")
   }
data["expense"].append(expense)
save_data()
print("Xarajat  saqlabdi!")

except  ValueError
   print("Hozircha Xarajatlar yo'q.")
   return
total = 0

for expense in data["expenses"]:
  print(
      f"{expense["name"]} - "
      f"{expense["amount"]} so'm "
      f"(expense["date"]})"
)
total += expense["amount"]

  print("---------------------")
  print("Jami xarajat: {total:g} so'm")

def srtatistics():
  total-tasks = len(data["tasks"] if task["done"]

                   )
       print("\n--- STATISTIKA ---")
       print(F"Jami vazifalar: {total_tasks}")
       print(f"Bajarilgan: {compleed}")
       print(f"Bajarilmagan: {pending}")
       print(f"Jami xarajat: {total_expensive:g} so'm")

def main():
  while True:
    print("\n============================")
    print("    PERSANOL MANAGER")
    print("==========================")
    print("1. Vazifa qo'shish")
    print("2. Vazifa ko'rish")
    print("3. Vazifa bajarilgan qilish")
    print("4. Vazifani o'chirish")
    print("5. Xarajat qo'shish")
    print("6. Xarajatlarni ko'rish")
    print("7. Statistikani ko'rish")
    print("0. Chiqish")

    choice = input("\nTanlovingiz: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_task()
       elif choice == "3":
            complate_task()
       elif  choice == "4":
            delete_task()
       elif  choice == "5":
            add_expense()
       elif  choice == "6":
            show_expense()
      elif choice == "7":
            statistics()
       elif  choice == "0":
            print("Dastur tugadi. Xayr!")
            break
        else:
          print("Noto'gri tablov! Qayta urinib ko'ring.")

if __name__ == "__main__":
  main()
      

       

  
