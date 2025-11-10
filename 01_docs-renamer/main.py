import os 

output_path = f"./output"
items = os.listdir(output_path)

print("Welcome to docs-renamer!")
print("We detected these files inside the output folder")
print("")

for item in items:
  print(item)

print("")
print("Do you wish to rename all files?")
rename_files = True if input("Y/N ") == "Y" or "y" else False
if rename_files:
  rename_value = input("Input string include as rename value: ")
  execute = True if input("Execute rename of files? Y/N ") == "Y" or "y" else False
  if(execute):
    try:
      for item in items:
        name, ext = os.path.splitext(item)
        new_name = f"{name}_{rename_value}{ext}"
        os.rename(f"{output_path}/{item}", f"{output_path}/{new_name}")
        print(new_name)
    except Exception as e:
      print("Error found", e)
