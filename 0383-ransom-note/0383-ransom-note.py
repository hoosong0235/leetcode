class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteList = list(ransomNote)
        magazineList = list(magazine)

        for i in ransomNoteList:
            if i in magazineList:
                magazineList.remove(i)
            else:
                return False
        
        return True