CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0  # Починаємо з першого каналу (індекс 0)

    def first_channel(self):
        self.current_channel_index = 0
        return self.channels[0]

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.channels[-1]

    def turn_channel(self, N):
        # N починається з 1, а індекси з 0
        if 1 <= N <= len(self.channels):
            self.current_channel_index = N - 1
            return self.channels[self.current_channel_index]
        return "No"

    def next_channel(self):
        # Переходимо на наступний канал або на перший, якщо ми на останньому, так як показували у прикладі на занятті з сторінками книги
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def previous_channel(self):
        # Переходимо на попередній канал або на останній, якщо ми на першому
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.channels[self.current_channel_index]

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def exists(self, channel):
        # Перевіряємо чи це число або назва каналу
        if isinstance(channel, int):
            # Якщо число - перевіряємо чи є такий номер каналу
            return "Yes" if 1 <= channel <= len(self.channels) else "No"
        elif isinstance(channel, str):
            # Якщо рядок - перевіряємо чи є такий канал в списку
            return "Yes" if channel in self.channels else "No"
        return "No"


# Тестування
controller = TVController(CHANNELS)
print(controller.first_channel())  # "BBC"
print(controller.last_channel())  # "TV1000"
print(controller.turn_channel(1))  # "BBC"
print(controller.next_channel())  # "Discovery"
print(controller.previous_channel())  # "BBC"
print(controller.current_channel())  # "BBC"
print(controller.exists(4))  # "No"
print(controller.exists("BBC"))  # "Yes"