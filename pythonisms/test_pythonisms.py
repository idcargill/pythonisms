import pytest
import time
from pythonisms.pythonisms import Associator, timing_decorator_delay

def test_associator_false():
  c = Associator()
  assert bool(c) == False

def test_associator_true():
  c = Associator()
  c.add('kitten')
  assert bool(c) == True

def test_associator_add():
  c = Associator()
  c.add('Fishsticks')
  assert c._size > 0

def test_add_error():
  with pytest.raises(KeyError):
    c = Associator()
    c.add('fish', 100)
    c.add('Fish', 200)

def test_associator_contains():
  c = Associator()
  c.add('kitten')
  c.add('fish')
  assert c.contains('kitten') == True

def test_associator_add_associate():
  c = Associator()
  c.add('kitten', 100)
  c.add('fish')
  c.add_associate('kitten', 'claws')
  assert c.get_item('kitten')[0] == 'kitten' 
  assert c.get_item('kitten')[1] == {'associate': ['claws'], 'value': 100}

def test_associator_drop_item():
  c = Associator()
  c.add('kitten', 100)
  c.add('fish', 200)
  c.drop_item('kitten')
  c.contains('kitten') == False

def test_associator_next():
  c = Associator()
  c.add('apple', 100)
  c.add('bat', 500)
  c.add('cat')
  next(c)
  assert next(c) == 'bat'

def test_timing_delay_decorator_():
  @timing_decorator_delay
  def some_function():
    return 'DONE YO!'

  start = time.perf_counter()
  some_function()
  stop = time.perf_counter()
  assert stop - start > 1.0

def test_sting():
  c = Associator()
  c.add('kitten', 100)
  c.add_associate('kitten', 'Tiger')
  result = repr(c)
  expected = " kitten : {'associate': ['Tiger'], 'value': 100}"
  assert result == expected

def test_get_size():
  c = Associator()
  c.add('kitten', 100)
  c.add('fish')
  c.add_associate('kitten', 'Tiger')
  assert c.size() == 2