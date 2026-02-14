import os
import time

LAB_FOLDER = "lab"
BASE_NAME = "فيروس تعليمي"

print("To jest EDUKACYJNY SYMULATOR 'WIRUSA'.")
print("Program jest nieszkodliwy i działa tylko w folderze projektu.\n")

# Utwórz folder lab, jeśli nie istnieje
if not os.path.exists(LAB_FOLDER):
    os.mkdir(LAB_FOLDER)
    print(f"Utworzono folder testowy: {LAB_FOLDER}")

# Utwórz kilka plików o nazwie 'فيروس تعليمي'
for i in range(5):
    filename = os.path.join(LAB_FOLDER, f"{BASE_NAME} {i+1}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("To jest plik utworzony przez edukacyjny symulator.\n")
        f.write("Nie jest to prawdziwy wirus.\n")
    print(f"Utworzono plik: {filename}")
    time.sleep(0.5)

print("\nSymulacja zakończona.")
print("Aby 'naprawić' wszystko, usuń folder 'lab' albo po prostu zamknij program.")
