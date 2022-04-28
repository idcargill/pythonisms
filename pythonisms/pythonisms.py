import time
class Associator:  
  def __init__(self):
    self.storage = {}
    self._size = 0
    self.base = 0
    
  def add(self, name, value=None):
    keys = [key.lower() for key in self.storage.keys()]
    if name.lower() not in keys:
      self.storage[name] = {'associate': [], 'value':value}
      self._size += 1
    else:
      raise KeyError(f'A "{name}" item already exists')

  def add_associate(self, name1, name2):
    if self.storage[name1]:
      self.storage[name1]['associate'].append(name2)
    else:
      raise KeyError(f'{name1} does not exist and can not have any friends')

  def __iter__(self):
    self.base = 0
    return self

  def __next__(self):
    if self._size > self.base:
      current = self.base
      self.base += 1
      contents = [key for key in self.storage.keys()]
      return contents[current]
    else:
      raise StopIteration('No more items :(')
 
  def __bool__(self):
    return self._size > 0

  def __str__(self):
    text = ''
    values =  [(key, self.storage[key]) for key in self.storage.keys()]
    for i in values:
      name = i[0]
      value = i[1]['value']
      associates= i[1]['associate']
      text += f'{name}\n -- Value: ({value})\n -- Associates: {associates}\n'
    return text

  def __repr__(self):
    text = ''
    values =  [f'{key} : {self.storage[key]}' for key in self.storage.keys()]
    for i in values:
      text += f' {i}'
    return text

  def contains(self, name):
    keys = [key.lower() for key in self.storage.keys()]
    if name.lower() not in keys:
      return False
    return True

  def get_items(self):
    keys = [key for key in self.storage.keys()]
    keys.sort()
    return keys

  def get_associates(self, name):
    contents = self.storage[name]['associate']
    return contents

  def get_item(self, name):
    if name in self.storage:
      return (name, self.storage[name])

  def drop_item(self, name):
    if self.contains(name):
      self.storage.pop(name)
      self._size -= 1

  def size(self):
    return self._size

def timing_decorator_delay(func):
  def wrapper(*args, **kwargs):
    # start timer
    start = time.perf_counter()

    # wrapped function call 2 second delay
    time.sleep(2)
    inner_value = func(*args, **kwargs)

    # stop timer    
    done = time.perf_counter()

    seconds = round(( done - start ),4)
    print(f'This function took {seconds} seconds to perform.')
    return inner_value
  return wrapper

@timing_decorator_delay
def do_stuff():
  j = 0
  for i in range(1000000):
    j += i
  return j
