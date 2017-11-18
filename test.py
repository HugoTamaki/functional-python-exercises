import unittest
from map import *
from filter import *
from reduce import *
from animal import Animal

class TestFunctionalPython(unittest.TestCase):

  def test_len_map(self):
    self.assertEqual(len_map(['Bob', 'John', 'William']), [3, 4, 7])

  def test_odd_even_map(self):
    self.assertEqual(odd_even_map([1, 4, 5, 7, 8]), ['impar', 'par', 'impar', 'impar', 'par'])

  def test_objects_to_dic(self):
    animals = [
      Animal('Bob', 'Rabbit'),
      Animal('John', 'Fish'),
      Animal('William', 'Dog')
    ]

    self.assertEqual(
      objects_to_dic(animals),
      [
        {
          'name': 'Bob',
          'type': 'Rabbit'
        },
        {
          'name': 'John',
          'type': 'Fish'
        },
        {
          'name': 'William',
          'type': 'Dog'
        }
      ])

  def test_dic_to_strings(self):
    animals = [
      {
        'name': 'Bob',
        'type': 'Rabbit'
      },
      {
        'name': 'John',
        'type': 'Fish'
      },
      {
        'name': 'William',
        'type': 'Dog'
      }
    ]

    self.assertEqual(dic_to_string(animals), ['Bob is a Rabbit', 'John is a Fish', 'William is a Dog'])

  def test_filter_odd_even(self):
    self.assertEqual(filter_odds([1, 2, 3, 4, 5]), [2, 4])

  def test_only_dic_with_attr(self):
    animals = [
      {
        'name': 'Bob',
        'type': 'Rabbit',
        'age': 10
      },
      {
        'name': 'John',
        'type': 'Fish',
        'age': 15
      },
      {
        'name': 'William',
        'type': 'Dog'
      }
    ]

    self.assertEqual(filter_dic_with('age', animals),
      [
        {
          'name': 'Bob',
          'type': 'Rabbit',
          'age': 10
        },
        {
          'name': 'John',
          'type': 'Fish',
          'age': 15
        }
      ]
    )

  def test_filter_array_with_more_than_x_elements(self):
    array = [
      [1, 2, 3, 4, 5],
      [1, 2, 3],
      ['Bob', 'John', 'William', 'Mack'],
      [2, 3, 4, 5]
    ]

    self.assertEqual(filter_array_with_more_than(4, array), [[1, 2, 3, 4, 5]])

  def test_sum_of_integers(self):
    self.assertEqual(sum_of_integers([3, 7, 8, 9]), 27)

  def test_dic_from_double_array(self):
    array = [
      ['name', 'Bob'],
      ['age', 10],
      ['type', 'Rabbit']
    ]

    self.assertEqual(dic_from_double_array(array),
      {
        'name': 'Bob',
        'age': 10,
        'type': 'Rabbit'
      }
    )

unittest.main()