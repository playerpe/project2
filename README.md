# Shuttle Stop Crowd Ranking 
Python App for Merge Sort Algorithm in a visual simulation to solve Shuttle Stop Crowd Ranking.

Merge Sort fits this project well because the app needs to sort shuttle stop records by crowd count and show the sorting process clearly. Each data item has a stop name and a crowd count, so the algorithm can compare the crowd counts while keeping the full record together. Merge Sort is a good choice because its process of splitting the list and merging it back together is easy to visualize step by step, which makes it a strong fit for an educational sorting app.


This app solves the Shuttle Stop Crowd Ranking problem. The user enters shuttle stops and estimated crowd counts. The program sorts the stops by crowd count using Merge Sort so the busiest stops can be identified and ranked.

## Preconditions
First, each record must follow the expected format: a shuttle stop name followed by a crowd count. For example, a valid entry is Albert/Union,45. Second, the crowd count must be a numeric, non-negative integer so that records can be compared consistently during sorting. Third, the stop name cannot be blank. Finally, the user must provide at least one valid shuttle stop entry.

The app enforces these preconditions by validating the input before running Merge Sort. It checks whether the input is empty, whether each line contains exactly one stop name and one crowd count, whether the stop name is present, and whether the crowd count is a valid non-negative integer. If any of these checks fail, the app does not attempt to sort the data. Instead, it displays a clear error message telling the user what needs to be corrected. This ensures that the algorithm only runs on valid and meaningful data.


During the simulation, the user will first see the original list they entered. Then the app will show how the list is split into smaller parts and merged back together in sorted order.

## Demo video/gif/screenshot of test
Screenshots are in the screenshots folder

## Problem Breakdown & Computational Thinking

Decomposition

The algorithm can be broken into smaller steps. First, the app reads the shuttle stop data entered by the user. Then it checks whether the input is valid. After that, the list is split into two smaller halves. Each half is split again until each sublist has only one item. Once that happens, the algorithm starts merging the sublists back together in sorted order by comparing their crowd counts. It keeps repeating this until the full list is merged into one sorted list. Finally, the app shows the ranked shuttle stops to the user.

Pattern Recognition

Merge Sort follows the same pattern over and over. It repeatedly divides the list into smaller parts, compares the first remaining item from two sublists, and places the correct one into a new merged list. In this project, the repeated pattern is comparing shuttle stops by crowd count and rebuilding the list in order from highest crowd count to lowest crowd count.

Abstraction

The app should only show the important sorting actions. For example, it should show how the list is being split, which two values are being compared, and how the merged list is being built. This keeps the simulation clear and easy to understand.

Algorithm Design

The user enters shuttle stop data into the GUI, with each line containing a stop name and a crowd count. The app then validates the input and converts it into a list of records. After that, Merge Sort processes the list by repeatedly splitting and merging it while recording the important steps. The GUI displays these steps so the user can follow the sorting process. At the end, the app shows the final ranked list of shuttle stops and identifies the busiest stop.

Input and Data Structure

The input will be entered as text in the GUI, where each line contains a shuttle stop name and a crowd count separated by a comma. The program will convert this input into a list of records. Each record will store a stop name and its crowd count. The algorithm will sort this list based on the crowd count.


Start
  ↓
User enters shuttle stop data
  ↓
Validate input
  ↓
Convert input into list of records
  ↓
Split list into smaller halves
  ↓
Recursively sort each half
  ↓
Merge halves by comparing crowd counts
  ↓
Repeat until one sorted list is formed
  ↓
Display sorting steps in GUI
  ↓
Show final ranked shuttle stops
  ↓
End

## Steps to Run
1. click run
2. ctrl + click on the link given in terminal

must have gradio installed

## Testing
Tested if all numbers are the same
Tested if number is 0
Tested invalid input

## Hugging Face Link
https://huggingface.co/spaces/Playerpe/Project2 

## Author & AI Acknowledgment
Got inspiration from https://huggingface.co/spaces/RuslanKain/sorting-searching-recognized-gestures this website
ChatGPT was used to explain how to use gradio
