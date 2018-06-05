import unittest
import boggle
from string import ascii_uppercase

class TestBoggle(unittest.TestCase):
      
    def test_can_create_an_empty_grid(self):
        
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid),0)
        
    def test_grid_size_is_width_times_height(self):
        
        grid = boggle.make_grid(2,3)
        self.assertEqual(len(grid), 6)
        
    def test_grid_coordinates(self):
        grid = boggle.make_grid(2,2)
        self.assertIn((0, 0), grid)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)
        
    def test_grid_is_filled_with_letters(self):
        grid = boggle.make_grid(2,3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
         
    def text_neighbours_of_a_position(self):
        
        coords = (1,2)
        neighbours = boggle.neighbours_of_position(coords)
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)
        
    def test_all_grid_neighbours(self):
        
        grid = boggle.make_grid(2,2)
        neighbours = boggle.all_grid_neighbours(grid)
        self.assertEqual(len(neighbours), len(grid))
        for pos in grid:
            others = list(grid)
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))
            
    def test_converting_a_path_to_a_word(self):
        
        grid = boggle.make_grid(2, 2)
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)])
        twoLetterWord = boggle.path_to_word(grid, [(0, 0), (1, 1)])
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])
        
        
        
        
        
        
        
        
        