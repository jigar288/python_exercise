def anon_note_checker(magazine,note):
  counter = 0

  note = note.split()
  magazine = magazine.lower()

  if "this" in magazine:
    magazine = magazine.replace("this","This")
  print(magazine)

  for i in note:
    if i in magazine:
      counter += 1

  if counter == len(note):
    return True
  elif counter != len(note):
    return False
