import time

file_name = input("Enter text file name => ") + ".txt"
try:
  with open(file_name, "r") as file:
    find_word = input("Enter word you want to replace => ")
    replace_word = input("Enter word you want to replace with => ")
    file_data = file.read()
    while True:
      word_index = file_data.find(find_word)
      if word_index == -1:
        print("No more word found")
        with open(file_name,"w") as final_file:
          print(file_data)
          final_file.write(file_data)
          time.sleep(5)
        break
      else:
        file_data = file_data[0:word_index] + replace_word + file_data[word_index+len(find_word):]
except:
  print("File not found !!!")
  time.sleep(5)
