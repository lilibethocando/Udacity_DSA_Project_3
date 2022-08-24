# Problem 5: Autocomplete with Tries

For solving this problem, I implemented a TrieNode and Trie class as requested and then created a 
"suffixes" function that returns a list with all suffixes for a given letter (prefix) if it exists.

For the **TrieNode**, the time complexity and space complexity to insert a character is **O(1)**.

For the **Trie**, the time complexity is **O(n)** and space complexity is **O(n)** for inserting a word. 
Finally, to find a prefix, the time complexity is **O(n)** and space complexity is **O(1)**.