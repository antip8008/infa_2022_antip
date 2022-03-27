class Stats():
    """отслеживает статистику"""

    def __init__(self):
        """инициализирует статистику"""
        self.resset_stats()

    def resset_stats(self):
        """статистика во время игры"""
        self.guns_left = 3
