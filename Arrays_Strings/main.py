from loguru import logger

TARGET_WORD = "the"
paragraph = """ Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
data warehouse and business intelligence industry's thought leader on the dimensional approach. He has educated tens of thousands of IT professionals. The Toolkit 
books written by Ralph and his colleagues have been the industry's best sellers 
since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
coinvented the Star workstation, the first commercial product with windows, icons, 
and a mouse, at Xerox's Palo Alto Research Center (PARC). Ralph has a PhD in 
electrical engineering from Stanford University """

def count_occurrences(paragraph, target_word):
    words = paragraph.lower().split()
    return sum(1 for word in words if word == target_word)

if __name__ == "__main__":
    count = count_occurrences(paragraph, TARGET_WORD)
    logger.info(f"The word '{TARGET_WORD}' occurs {count} times in the paragraph.")





