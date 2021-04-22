import unittest

from game_of_life import compute_next_state
from game_of_life import CellState
from game_of_life import generate_signals_for_one_position
from game_of_life import generate_signals_for_multiple_position, count_signals
from game_of_life import next_generation, get_bounds


class TestGameOfLife(unittest.TestCase):

  def test_canary(self):
    self.assertTrue(True)

  def test_compute_next_state_zero_neighbor(self):
    self.assertEqual(compute_next_state(CellState.DEAD, 0), CellState.DEAD)

  def test_compute_next_state_one_neighbor_dead(self):
    self.assertEqual(compute_next_state(CellState.DEAD, 1), CellState.DEAD)

  def test_compute_next_state_two_neighbor_dead(self):
    self.assertEqual(compute_next_state(CellState.DEAD, 2), CellState.DEAD)

  def test_compute_next_state_five_neighbor_dead(self):
    self.assertEqual(compute_next_state(CellState.DEAD, 5), CellState.DEAD)

  def test_compute_next_state_eight_neighbor_dead(self):
    self.assertEqual(compute_next_state(CellState.DEAD, 8), CellState.DEAD)

  def test_compute_next_state_three_neighbor_dead(self):
    self.assertEqual(compute_next_state(CellState.DEAD, 3), CellState.LIVE)

  def test_compute_next_state_one_neighbor_live(self):
    self.assertEqual(compute_next_state(CellState.LIVE, 1), CellState.DEAD)

  def test_compute_next_state_four_neighbor_live(self):
    self.assertEqual(compute_next_state(CellState.LIVE, 4), CellState.DEAD)

  def test_compute_next_state_eight_neighbor_live(self):
    self.assertEqual(compute_next_state(CellState.LIVE, 8), CellState.DEAD)

  def test_compute_next_state_three_neighbor_live(self):
    self.assertEqual(compute_next_state(CellState.LIVE, 3), CellState.LIVE)

  def test_compute_next_state_two_neighbor_live(self):
    self.assertEqual(compute_next_state(CellState.LIVE, 2), CellState.LIVE)

  def test_generate_signals_for_one_position(self):
    self.assertEqual(generate_signals_for_one_position(2, 3),
      [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)])

  def test_generate_signals_for_one_position_three_three(self):
    self.assertEqual(generate_signals_for_one_position(3, 3),
      [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)])

  def test_generate_signals_for_one_position_two_four(self):
    self.assertEqual(generate_signals_for_one_position(2, 4),
      [(1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)])

  def test_generate_signals_for_one_position_zero_zero(self):
    self.assertEqual(generate_signals_for_one_position(0, 0),
      [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])

  def test_generate_signals_for_multiple_postions_given_no_position(self):
    live_cells = []
    self.assertEqual(generate_signals_for_multiple_position(live_cells), [])

  def test_generate_signals_for_multiple_postions_given_one_position(self):
    live_cells = [(2, 3)]
    self.assertEqual(generate_signals_for_multiple_position(live_cells),
      [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4)])

  def test_generate_signals_for_multiple_postions_given_two_position(self):
    live_cells = [(2, 3), (3, 3)]
    self.assertEqual(generate_signals_for_multiple_position(live_cells),
      [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4),
      (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)])

  def test_generate_signals_for_multiple_postions_given_three_position(self):
    live_cells = [(2, 3), (3, 3), (2, 4)]
    self.assertEqual(generate_signals_for_multiple_position(live_cells),
      [(1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 2), (3, 3), (3, 4),
      (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4),
      (1, 3), (1, 4), (1, 5), (2, 3), (2, 5), (3, 3), (3, 4), (3, 5)])

  def test_count_signals_none(self):
    live_cells = []
    self.assertEqual(count_signals(live_cells), {})

  def test_count_signals_one(self):
    live_cells = [(2, 3)]
    self.assertEqual(count_signals(live_cells), {(2, 3): 1})


  def test_count_signals_two(self):
    live_cells = [(2, 3), (2, 3)]
    self.assertEqual(count_signals(live_cells), {(2, 3): 2})

  def test_count_signals_three(self):
    live_cells = [(2, 3), (3, 3), (2, 3)]
    self.assertEqual(count_signals(live_cells),{(2, 3): 2, (3, 3): 1})

  def test_next_generation_zero(self):
    live_cells = []
    self.assertEqual(next_generation(live_cells), [])

  def test_next_generation_one(self):
    live_cells = [(2, 3)] 
    self.assertEqual(next_generation(live_cells),[])
    
  def test_next_generation_two(self):
    live_cells = [(2, 3), (2, 4)]
    self.assertEqual(next_generation(live_cells),[])
    
  def test_next_generation_three_one(self):
    live_cells = [(1, 1), (1, 2), (3, 0)]
    self.assertEqual(next_generation(live_cells),[(2, 1)])

  def test_next_generation_three_two(self):
    live_cells = [(1, 1), (1, 2), (2, 2)]
    self.assertEqual(sorted(next_generation(live_cells)),[(1, 1), (1, 2), (2, 1), (2, 2)])

  def test_next_generation_block(self):
    live_cells = [(1, 1),(1, 2),(2, 1),(2, 2)]
    self.assertEqual(sorted(next_generation(live_cells)), [(1, 1), (1, 2), (2, 1), (2, 2)])

  def test_next_generation_bee_hive(self):
    live_cells = [(0, 3), (1, 4), (2, 4), (3, 3), (2, 2), (1, 2)]
    self.assertEqual(next_generation(live_cells), [(1, 2), (1, 4), (0, 3), (2, 4), (3, 3), (2, 2)])

  def test_next_generation_horizontal_blinker_to_vertical(self):
    live_cells = [(1, 3), (1,2), (1, 1)]
    self.assertEqual(next_generation(live_cells),  [(0, 2), (1, 2), (2, 2)])

  def test_next_generation_vertical_blinker_to_horizontal(self):
    live_cells = [(0, 2),(1, 2),(2, 2)]
    self.assertEqual(next_generation(live_cells), [(1, 1), (1, 2), (1, 3)])

  def test_next_generation_glider(self):
    live_cells = [(0, 3), (1, 2), (2, 2), (0, 1), (1, 1)]
    self.assertEqual(next_generation(live_cells),[(1, 3), (0, 1), (1, 1), (2, 1), (2, 2)] )

  def test_get_bound_no_points(self):
    live_cells = []
    self.assertEqual(get_bounds(live_cells),[])

  def test_get_bound_one_point(self):
    live_cells = [(1,2)]
    self.assertEqual(get_bounds(live_cells),[(1, 2), (1, 2)])

  def test_get_bound_two_point(self):
    live_cells = [(1, 2), (4, 0)]
    self.assertEqual(get_bounds(live_cells),[(1, 0), (4, 2)])

  def test_get_bound_three_points(self):
    live_cells = [(1, 1), (2,3 ), (5, 9)]
    self.assertEqual(get_bounds(live_cells),[(1, 1), (5, 9)])

  def test_get_bound_four_points(self):
    live_cells = [(0, 0), (4, 2),(7, 1),(9, 9)]
    self.assertEqual(get_bounds(live_cells),[(0, 0), (9, 9)])

if __name__ == '__main__':
  unittest.main()
