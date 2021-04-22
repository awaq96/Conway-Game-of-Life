from enum import Enum
from collections import Counter

class CellState(Enum):
  LIVE = 1
  DEAD = 2

TWO_LIVE_NEIGHBORS = 2
THREE_LIVE_NEIGHBORS = 3

def compute_next_state(CellState, number_of_live_neighbors):
  return CellState.LIVE if number_of_live_neighbors == THREE_LIVE_NEIGHBORS or \
    number_of_live_neighbors == TWO_LIVE_NEIGHBORS and CellState == CellState.LIVE else CellState.DEAD

def generate_signals_for_one_position(row, col):
  return [(i, j) for i in range(row - 1, row + 2) for j in range(col - 1, col + 2) if([i, j] != [row, col])]

def generate_signals_for_multiple_position(live_cells): 
  return [signal for live_cell in live_cells for signal in generate_signals_for_one_position(live_cell[0], live_cell[1])]

def count_signals(live_cells):
  return Counter(live_cells)

def next_generation(live_cells):
  impacted_cells = generate_signals_for_multiple_position(live_cells)
  signal_map = count_signals(impacted_cells)
  next_gen_live_cells = []

  for key in signal_map:
    if signal_map[key] == 3 or signal_map[key] == 2 and key in live_cells:
      next_gen_live_cells.append(key)
  return next_gen_live_cells

  # return set([position for position, signals_count in dict(count_signals(live_cells)).items()
  #   if CellState.LIVE == compute_next_state(CellState.LIVE if position in live_cells else CellState.DEAD, signals_count)])
  #
def get_bounds(live_cells_postions):

  if not live_cells_postions:
    return []

  x_points = []
  y_points = []
    
  for points in live_cells_postions:
    x_points.append(points[0])
    y_points.append(points[1])

  return [(min(x_points),min(y_points)),(max(x_points),max(y_points))]

