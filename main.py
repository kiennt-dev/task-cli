import sys 
import storage

if len(sys.argv) < 2:
  print("Vui long nhap lenh(add, list, done, delete)" )
  sys.exit(1)
if sys.argv[1] == "add":
    if len(sys.argv) < 3:
        print("Chua Nhap Noi Dung")
        sys.exit(1)
    tasks = storage.load_tasks()
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1
    new_task = {"id": new_id, "title": sys.argv[2], "status": "todo"}
    tasks.append(new_task)
    storage.save_tasks(tasks)
    print(f"Da them viec so {new_id}: {sys.argv[2]}")
elif sys.argv[1] == "list":
    tasks=storage.load_tasks()
    if len(tasks) == 0:
        print("Danh sach cong viec dang trong")
    else:
        for task in tasks:
            print(f"[{task['id']}], [{task['title']}], ({task['status']})")
      