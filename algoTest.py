
import unittest
import algorithms.bubble as bubble
import algorithms.quick as quick
import algorithms.insertion as insertion
import algorithms.selection as selection
import algorithms.shell as shell
import algorithms.cocktail as cocktail
import tools.toolFunctions as tools

class testSortingAlgorithms(unittest.TestCase):
    
    def testBubbleSort(self):
        self.assertTrue(tools.isSorted(bubble.bubbleSort(
            tools.randomList(50))))
        self.assertTrue(tools.isSorted(bubble.bubbleSort(
            tools.randomList(500))))
        
    def testQuickSort(self):
        self.assertTrue(tools.isSorted(quick.quickSort(tools.randomList(50))))
        self.assertTrue(tools.isSorted(quick.quickSort(tools.randomList(500))))
        
    def testInsertionSort(self):
        self.assertTrue(tools.isSorted(insertion.insertionSort(
            tools.randomList(50))))
        self.assertTrue(tools.isSorted(insertion.insertionSort(
            tools.randomList(500))))
    
    def testSelectionSort(self):
        self.assertTrue(tools.isSorted(selection.selectionSort(
            tools.randomList(50))))
        self.assertTrue(tools.isSorted(selection.selectionSort(
            tools.randomList(500))))

    def testShellSort(self):
        self.assertTrue(tools.isSorted(shell.shellSort(
            tools.randomList(50))))
        self.assertTrue(tools.isSorted(shell.shellSort(
            tools.randomList(500))))
    
    def testCocktailSort(self):
        self.assertTrue(tools.isSorted(cocktail.cocktailSort(
            tools.randomList(30))))
        self.assertTrue(tools.isSorted(cocktail.cocktailSort(
            tools.randomList(500))))

if __name__== '__main__':
    unittest.main()