with open("selfLearning/file_handeling/file.txt", "a+") as f:
  # f.write("Hello World\n")
  # f.truncate(20)

  # f.seek(2)
  f.read(5)
  print(f.tell())